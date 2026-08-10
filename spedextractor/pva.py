# Copyright 2026 - TODAY, KMEE - Luis Felipe Mileo <mileo@kmee.com.br>
"""Build the module CSVs from the official PVA descriptor instead of the pdf.

Every SPED validator (PVA) ships the layout it actually enforces as XML
descriptors inside its own jars:

    <pva>/lib/**/*.jar
        descritor/escrituracao/[ato<NNN>/]estrutura<ID>/v<N>/descritor.xml

Each field comes with its position, code, type, size, decimal places,
mandatoriness and valid values, and the register nesting in the XML is the
hierarchy itself. This is the structure the validator applies, so it cannot
lag the layout the way the Guia Pratico pdf does, and nothing has to be
scraped or patched by hand.

The descriptor to use is the one the PVA prints in its status bar right after
importing a file of the target period ("ID do Descritor: ... Versao do
Descritor: ..."). Picking the highest number is a guess: every PVA carries all
its historical layouts.

Usage:

    python -m spedextractor.pva <pva_dir> --mod efd_icms_ipi --layout 20 \
        --structure 001 --ato 020 --descriptor-version 2

`<pva_dir>` may also be a descriptor.xml already extracted; in that case the
selection options are not needed. Without options on a PVA dir, the available
descriptors are listed.

The command writes `accurate_fields.csv` (same format the pdf pipeline
produces, with "pva" in the Page column) and `registers_pva.csv` next to it.
From there the regular pipeline works unchanged: `get_fields`,
`get_registers`, `build_usable_fields_csv`, `build_registers_csv` and
`gen_odoo` read the same files.
"""

import csv
import logging
import pathlib
import re
import unicodedata
import xml.etree.ElementTree as ET
import zipfile

import click

from .constants import MODULE_HEADER, MODULES, SPECS_PATH, RegisterDict

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

DESCRIPTOR_PATH = re.compile(
    r"descritor/escrituracao/"
    r"(?:ato(?P<act>\w+)/)?"
    r"estrutura(?P<structure>\w+)/v(?P<version>\w+)/descritor\.xml"
)

# An attribute NAME with an accent in it, which some descriptors carry
# (`descrição=` instead of `descricao=` in the EFD ICMS/IPI one) and which the
# stdlib XML parser refuses. Only attribute names are normalized; values keep
# every character they had.
_ACCENTED_ATTRIBUTE = re.compile(r"(?<=[\s])([A-Za-z_][\w-]*[^\x00-\x7f][\w-]*)=")

# how the descriptor writes mandatoriness: 1 = required, 2 = conditionally
# required, 0 = optional. Same vocabulary the pdf uses in the Obrig column.
_SPEC_REQUIRED = {"1": "O", "2": "OC"}

# how the descriptor writes occurrence: 0 = once, 1 = at most once, 2 = many.
# Confirmed against the block opening registers (0) and conditional child
# registers (1) of the EFD descriptors.
_CARD = {"0": "1:1", "1": "1:1", "2": "1:N"}


def _ascii_attribute_name(match: re.Match) -> str:
    name = match.group(1)
    plain = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return f"{plain or name}="


def _sanitize(raw: bytes) -> str:
    text = raw.decode("utf-8", errors="replace")
    return _ACCENTED_ATTRIBUTE.sub(_ascii_attribute_name, text)


def find_descriptors(pva_dir: pathlib.Path) -> list[dict]:
    """Every descriptor inside a PVA installation."""
    found = []
    for jar in sorted(pva_dir.rglob("*.jar")):
        try:
            with zipfile.ZipFile(jar) as archive:
                for member in archive.namelist():
                    match = DESCRIPTOR_PATH.fullmatch(member)
                    if match:
                        found.append(
                            {
                                "act": match.group("act") or "",
                                "structure": match.group("structure"),
                                "version": match.group("version"),
                                "jar": jar,
                                "member": member,
                            }
                        )
        except zipfile.BadZipFile:
            continue
    return sorted(found, key=lambda d: (d["act"], d["structure"], d["version"]))


def _read_descriptor(descriptor: dict) -> bytes:
    with zipfile.ZipFile(descriptor["jar"]) as archive:
        return archive.read(descriptor["member"])


def _spec_values(field: ET.Element) -> str:
    values = field.find("valores-validos")
    if values is None or not values.get("valores"):
        return ""
    codes = []
    for item in values.get("valores", "").split(";"):
        code = item.partition("=")[0].strip()
        if code:
            codes.append(code)
    if len(codes) < 2:
        return ""  # a single value is the fixed content of a REG field
    return "[" + ";".join(codes) + "]"


def _length(raw: str) -> str:
    """The descriptor's size in the pdf Tam convention.

    `[N]` is an exact size and `N` a maximum; the pdf writes them `00N*`
    and `00N`, which is what the interpretation layer already expects.
    """
    fixed = raw.startswith("[") and raw.endswith("]")
    digits = raw.strip("[]")
    if not digits.isdigit():
        return ""
    return f"{int(digits):03d}" + ("*" if fixed else "")


def _field_rules(field: ET.Element) -> str:
    return "".join(
        f"[{rule.get('id')}]" for rule in field.iter("validador") if rule.get("id")
    )


def _field_row(register: ET.Element, field: ET.Element, mod: str) -> list[str] | None:
    """One accurate_fields.csv row, in the module's own column layout."""
    code = field.get("id")
    position = re.sub(r"\D", "", field.get("n") or "")  # positions like `31'` show up
    if not code or not position:
        return None
    if code == "REG":
        # the REG row carries the REGISTER's own mandatoriness, which is how
        # the interpretation layer reads register-level requiredness
        required = _SPEC_REQUIRED.get(register.get("obrigatorio", ""), "")
    else:
        required = _SPEC_REQUIRED.get(field.get("obrigatorio", ""), "")
    known = {
        "index": position,
        "code": code,
        "desc": field.get("descricao") or field.get("rotulo") or "",
        "spec_type": field.get("tipo") or "C",
        "length": _length(field.get("tamanho", "")),
        "decimal": field.get("casasdecimais", ""),
        "spec_required": required,
        "spec_values": _spec_values(field),
        "rules": _field_rules(field),
        # the descriptor does not split mandatoriness by direction
        "spec_in": "",
        "spec_out": "",
    }
    reg_code = register.get("id", "")
    return [reg_code, "pva"] + [known.get(key, "") for _, key in MODULE_HEADER[mod]]


def _level(node: ET.Element, code: str, depth: int) -> int:
    """The register's hierarchy level.

    Some descriptors carry it as the `nivel` attribute (EFD ICMS/IPI, EFD
    PIS/COFINS, ECF); the ECD one does not, and there the nesting depth of
    the <registro> elements IS the hierarchy: a register hanging directly off
    its <bloco> is a level 1 opener, and each nesting adds one. The 0000 is
    the level 0 declaration in every layout, and in the ECD it WRAPS the rest
    of its block, so it does not count as a nesting level for its children
    (the caller keeps the depth unchanged below it).
    """
    if node.get("nivel"):
        return int(node.get("nivel", "0"))
    if code == "0000":
        return 0
    return depth


def build_from_descriptor(mod: str, layout: int, xml_bytes: bytes) -> None:
    """Write accurate_fields.csv and registers_pva.csv from one descriptor."""
    root = ET.fromstring(_sanitize(xml_bytes))
    base = SPECS_PATH / mod / str(layout)
    base.mkdir(parents=True, exist_ok=True)

    registers: list[RegisterDict] = []
    field_rows: list[list[str]] = []
    seen: set[str] = set()

    def visit(node: ET.Element, depth: int) -> None:
        """Document order, so registers come out in layout order and a parent
        always comes before its children. Only <registro> adds depth: the
        <bloco> wrappers some descriptors use are transparent."""
        code = node.get("id")
        if not code or code in seen:
            return
        seen.add(code)
        register: RegisterDict = {
            "block": code[0],
            "code": code,
            "desc": node.get("descricao") or node.get("rotulo") or "",
            "level": _level(node, code, depth),
            "card": _CARD.get(node.get("ocorrencia", "2"), "1:N"),
        }
        if node.get("obrigatorio") == "1":
            register["required"] = True
        registers.append(register)

        rows = []
        for field in node.findall("campo"):
            row = _field_row(node, field, mod)
            if row is not None:
                rows.append(row)
        # the file is positional: keep the fields in their declared position
        rows.sort(key=lambda r: int(r[2]))
        field_rows.extend(rows)

        # the 0000 wrapper is transparent: its children are level 1 openers
        child_depth = depth if code == "0000" else depth + 1
        for child in node.findall("registro"):
            visit(child, child_depth)

    def descend(element: ET.Element, depth: int) -> None:
        for child in element:
            if child.tag == "registro":
                visit(child, depth + 1)
            else:
                descend(child, depth)

    descend(root, 0)

    accurate_file = base / "accurate_fields.csv"
    with open(accurate_file, "w", newline="") as accurate_csv:
        writer = csv.writer(
            accurate_csv,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        writer.writerow(["Register", "Page"] + [name for name, _ in MODULE_HEADER[mod]])
        writer.writerows(field_rows)
    logger.info(f"> {accurate_file} written from the PVA descriptor")

    registers_file = base / "registers_pva.csv"
    with open(registers_file, "w", newline="") as registers_csv:
        writer = csv.writer(
            registers_csv,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        writer.writerow(["block", "code", "desc", "level", "card", "required"])
        for register in registers:
            writer.writerow(
                [
                    register["block"],
                    register["code"],
                    register["desc"],
                    register["level"],
                    register["card"],
                    register.get("required") and "True" or "",
                ]
            )
    logger.info(f"> {registers_file} written ({len(registers)} registers)")


def read_registers_csv(path: pathlib.Path) -> list[RegisterDict]:
    """The registers list of a descriptor-generated layout."""
    registers: list[RegisterDict] = []
    with open(path, newline="") as registers_csv:
        rows = csv.DictReader(registers_csv)
        for row in rows:
            register: RegisterDict = {
                "block": row["block"],
                "code": row["code"],
                "desc": row["desc"],
                "level": int(row["level"]),
                "card": row["card"],
            }
            if row.get("required") == "True":
                register["required"] = True
            registers.append(register)
    return registers


@click.command()
@click.argument("source", type=click.Path(exists=True, path_type=pathlib.Path))
@click.option("--mod", required=True, type=click.Choice(list(MODULES.keys())))
@click.option("--layout", required=True, type=int, help="Layout version (specs dir).")
@click.option("--structure", default="", help="estrutura<ID> of the descriptor.")
@click.option("--ato", default="", help="ato<NNN> of the descriptor, when present.")
@click.option(
    "--descriptor-version", default="", help="v<N> of the descriptor, NOT the layout."
)
def main(
    source: pathlib.Path,
    mod: str,
    layout: int,
    structure: str,
    ato: str,
    descriptor_version: str,
) -> None:
    """Build the CSVs of MOD from the official PVA descriptor in SOURCE.

    SOURCE is the install dir of the PVA (the descriptor is pulled from its
    jars) or a descriptor.xml already extracted.
    """
    if source.is_file():
        build_from_descriptor(mod, layout, source.read_bytes())
        return
    descriptors = find_descriptors(source)
    if not descriptors:
        raise click.ClickException(f"no descriptor found under {source}")
    wanted = [
        d
        for d in descriptors
        if (not structure or d["structure"] == structure)
        and (not ato or d["act"] == ato)
        and (not descriptor_version or d["version"] == descriptor_version)
    ]
    if len(wanted) != 1:
        for d in descriptors:
            act = d["act"] and f"ato{d['act']} " or ""
            logger.info(f"  {act}estrutura{d['structure']} v{d['version']}")
        raise click.ClickException(
            "pick ONE descriptor with --structure/--ato/--descriptor-version, "
            "the one the PVA prints in the status bar after importing a file "
            f"of the target period ({len(wanted or descriptors)} candidates)"
        )
    build_from_descriptor(mod, layout, _read_descriptor(wanted[0]))


if __name__ == "__main__":
    main()

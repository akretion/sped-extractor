"""
This module is divided in 5 steps in order to build usable CSV files from the raw CSV
extracted by extract_tables.py :

1.  `extract_registers_list` extracts a list of the module's registers
    from the module's blocks registers lists.
2.  `extract_register_fields` extracts fields rows from one register's table as they
    appear in the raw CSV files.
3.  Using this method and the module's registers list, `build_accurate_fields_csv`
    creates a CSV file named 'MODULE_accurate_fields.csv' listing the fields rows
    for each module as they appear in the original pdf.
4.  From these 'accurate CSV files', two methods `get_fields` and `get_registers` are
    defined and return lists of the module's fields and registers made as usable python
    dictionaries with 'interpreted' information (field's type, booleans for required
    fields, register's level...)
5. `build_registers_csv` and `build_usable_fields_csv` finally create CSV files listing
    the module's registers and fields from these 'interpreted' dictionaries.

"""

import csv
import logging
import re
from unidecode import unidecode

import click

from . import extract_tables
from .constants import MODULE_HEADER, MODULES, SPECS_PATH

logger = logging.getLogger(__name__)
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.INFO)


def _get_mod_header(mod):
    # Override this method if the hard code MODULE_HEADER is not wanted
    return MODULE_HEADER.get(mod)


# used to sort csv files
def _atoi(text):
    return int(text) if text.isdigit() else text


# used to sort csv files
def natural_keys(file):
    """
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    """
    return [_atoi(c) for c in re.split(r"(\d+)", file.name)]


def get_raw_rows(mod, layout):
    """Walk through ./specs/MODULE/LAYOUT/raw_camelot_csv/ and return a big dictionary
    of all the raw rows found in raw CSV files extracted by ./extract_tables.py,
    gathered by their page number :

    raw_rows = {
        12: [
            ["Empresas  Obrigad...", "Devem  produzir  o  livro  “Z”..."],
            ["Nº", "Campo", "Descrição", "Tipo", "Tamanho", "Decimal"],
            ["01", "REG", "Identificador do registro: I510", "C", "004", "-"],
            ["02", "NAT_SUB_CNT", "Natureza  da  subconta", "C", "002", "-"],
            ["03", "COD_SUB_CNT", "Código da subco....", "C", "020", "-"],
            ...
        ],
        13: [[...], [...]],
        ...
    }
    """
    raw_rows = {}
    path_raw = SPECS_PATH / mod / str(layout) / "raw_camelot_csv"

    if not path_raw.exists():
        extract_tables.extract_mod_tables(mod)
        # After potential extraction, check again.
        if (
            not path_raw.exists()
        ):  # If still not exists (e.g. download failed or extract_tables failed)
            logger.error(
                f"Raw CSV directory {path_raw} not found and could not be created/populated by extract_tables."
            )
            return {}  # Return empty to avoid crashing on iterdir

    # If path_raw exists but is not a directory, also return empty.
    if not path_raw.is_dir():
        logger.warning(f"Path {path_raw} exists but is not a directory.")
        return {}

    csv_files = sorted([file for file in path_raw.iterdir()], key=natural_keys)

    for csv_file in csv_files:
        parts = csv_file.name.split("-")
        # Expecting names like "ecd-page-5-table-1.csv"
        # At least 4 parts: [mod, "page", pagenum, tableinfo.csv]
        if len(parts) >= 4 and parts[1] == "page" and parts[2].isdigit():
            try:
                page = int(parts[2])
                with open(csv_file, "r", encoding="utf-8") as csvfile_content:
                    reader = csv.reader(csvfile_content, delimiter=",", quotechar='"')
                    for row_content in reader:
                        raw_rows.setdefault(page, []).append(row_content)
            except ValueError:  # Handles if parts[2] is not an int after all
                logger.warning(
                    f"Could not parse page number from filename: {csv_file.name}"
                )
            except (
                Exception
            ) as e:  # Catch other potential errors during file read/parse
                logger.warning(f"Could not read or parse CSV file {csv_file}: {e}")
        else:
            logger.warning(
                f"Skipping file with unexpected name format: {csv_file.name}"
            )

    return raw_rows


def clean_row(row):
    """Clean row's content"""
    row = [str(x) for x in row]
    for index, cell in enumerate(row):
        # replace all the whitespaces ("  ", \n, \r...)
        clean_cell = " ".join(cell.split())
        # e.g. change "Entr." to "Entr" in fields table's headers
        if re.match(r"^[a-zA-Z]+\.$", clean_cell):
            clean_cell = clean_cell[:-1]
        # e.g. change "N’" to "N" in column "Tipo"
        if re.match(r"^[a-zA-Z]+\’$", clean_cell):
            clean_cell = clean_cell[:-1]
        row[index] = clean_cell

    return row


# 1. `extract_registers_list`
# ===========================


def _is_register_code(code):
    if not code:
        return False
    return len(code) == 4 and code[1:3].isdigit()


def _map_register_row(mod, row):
    """Extracts register's row information for each kind of module"""
    # TODO : Join rows content when they are from the same register's line but
    # splited in two because of page break.
    # Example : EFD ICMS IPI pdf Outubro 2019 p20-21
    register = {}
    if len(row) > 2:
        if mod == "ecd":
            if len(row[0]) == 1 and row[0] != "":
                register = {
                    "block": row[0],
                    "code": row[2],
                    "desc": row[1],
                    "level": row[3],
                    "card": row[4],
                }
        elif mod == "ecf":
            if len(row[0]) == 4:
                register = {
                    "block": row[0][0],
                    "code": row[0],
                    "desc": row[2],
                    "level": row[1],
                    "card": row[5],
                }
        elif mod == "efd_pis_cofins":
            code = row[2][:-4] if row[2].endswith(" (*)") else row[2]
            if len(code) == 4 and len(row) >= 5:
                register = {
                    "block": row[0],
                    "code": code,
                    "desc": row[1],
                    "level": row[3],
                    "card": row[4],
                }

        elif mod == "efd_icms_ipi":
            if len(row[0]) == 1 and row[0] != "":
                register = {
                    "block": row[0],
                    "code": row[2],
                    "desc": row[1],
                    "level": row[3],
                    "card": row[4],
                }

    if register.get("code") and _is_register_code(register["code"]):
        if str(register["level"]).isdigit():
            register["level"] = int(register["level"])
        else:
            return False
    else:
        return False

    return register


def extract_registers_list(mod, layout, raw_rows=None):
    """Scans the raw csv rows and return 'registers', a list of dictionaries giving
    all the information about the module's registers (block, code, description,
    hierarchy level and card) found in the block's registers lists."""
    registers = []
    in_block = False
    if not raw_rows:
        raw_rows = get_raw_rows(mod, layout)

    for page in raw_rows:
        for row in raw_rows[page]:
            if (
                ("BLOCO" in row or "Bloco" in row or "Registro" in row)
                and (
                    "NÍVEL" in row
                    or "Nível" in row
                    or r"N\xc3\xadvel" in row
                    or "Nome do Registro" in row
                    or "Reg." in row
                )
                or "BLOCO  DESCRIÇÃO" in row  # ecf
            ):  # ecd
                in_block = True
                continue
            if in_block:
                if "".join(row) == "":
                    continue  # empty line
                reg = _map_register_row(mod, clean_row(row))
                if reg and reg["code"] not in [r["code"] for r in registers]:
                    registers.append(reg)

                    if reg["code"] == "9999":
                        return registers

    return registers


# 2. `extract_register_fields`
# ============================


def _is_joined_index(row, c):
    """Checks if row's column 'c' start with row's index and need to be split"""
    if len(row) > 4 and row[c][0:1].isdigit() and len(row[c]) > 3 and " " in row[c]:
        return True
    return False


def _split_code_desc(row, c):
    """Checks if row's column 'c' is a joined code and description and return 2 split
    items to be used if true"""
    i_end = 0
    code = []
    desc = []
    for i, part_cell in enumerate(row[c].split(" ")):
        if not re.match(r"\b[A-Z_ÇÃÕÍÚe0-9]+\b", part_cell):
            i_end = i
            break
    if i_end != 0:
        split = row[c].split(" ")
        code = " ".join(split[:i_end])
        desc = " ".join(split[i_end:])
        return code, desc
    else:
        return None


def _format_row(row):
    """Separates columns joined together"""

    # change ["04  VL_BC_RET", ""] into ["04","VL_BC_RET"]
    if _is_joined_index(row, 0) and row[1] == "":
        split = row[0].split(" ")
        row = [split[0], " ".join(split[1:])] + row[2:]
    # change ["", "04  VL_BC_RET"] into ["04","VL_BC_RET"] or ["", "1 REG"] into ["1", "REG"]
    if _is_joined_index(row, 1) and row[0] == "":
        split = row[1].split(" ")
        row = [split[0], " ".join(split[1:])] + row[2:]

    # change ["02","NUM_ITEM  Número seqüencial do item no documento fiscal","", "N"]
    # into ["02","NUM_ITEM", "Número seqüencial do item no documento fiscal", "N"]
    if _split_code_desc(row, 1) and row[2] == "":
        row[1], row[2] = _split_code_desc(row, 1)

    # fix ["02","", "NUM_ITEM  Número seqüencial do item no documento fiscal", "N"]
    if _split_code_desc(row, 2) and row[1] == "":
        row[1], row[2] = _split_code_desc(row, 2)

    # fix ["02", "NUM_ ITEM  Número seqüencial do item no documento fiscal", "N"]
    if _split_code_desc(row, 1) and row[2] != "":
        row[1], desc = _split_code_desc(row, 1)
        row.insert(2, desc)

    # Sommetimes the description cell (=row[2]) itself is split and override type's cell
    # (=row[3])
    if len(row[3]) > 2:
        row[2] = row[2] + " " + row.pop(3)

    return row


def _map_row_mod_header(row, mod):
    """Inserts empty column when needed to align with module's header columns order"""
    len_header = len(_get_mod_header(mod))
    if row and mod == "efd_icms_ipi":
        if len(row) == len_header - 1:
            # i.e. row has the columns 'Entr' and 'Saída' but not 'Obrig'
            row.insert(6, "")
    # Add empty cells in row if incomplete
    if row and len(row) < len_header:
        extension = [""] * (len_header - len(row))
        row.extend(extension)

    return row


def _is_reg_row(row):
    if "REG" in row[1] and "Texto" in row[2]:
        return True
    return False


def _apply_camelot_patch(mod, layout, register, row):
    """Catches patched row in ./camelot_patch/ and return override current row"""
    patch_file = SPECS_PATH / mod / str(layout) / "camelot_patch" / "camelot_patch.csv"

    try:
        with open(patch_file, "r") as patch_csv:
            patch_rows = csv.reader(patch_csv, delimiter=",", quotechar='"')
            for patch_row in patch_rows:
                # N-B : A patch can be applied twice if a row which is not a register's
                # field match this condition (e.g. field TIP_ENT in ECF register 0010).
                # But it is not a problem as the non-field row will be ignore after.
                if patch_row[0] == register and patch_row[2] == row[0]:
                    # FIXME
                    row = patch_row[2:]
                    logger.info(f"    PATCH : field {row[1]} in register {register}")
    except FileNotFoundError:
        return row
    return row


# def _is_field_row(row, last_field_index=0): # last_field_index is effectively unused for sequence check
#
#     """Returns True if the row match a series of condition to be a register's field"""
#     if (
#         len(row) > 1 and row[1] != "" # "Campo" column has content
#         and len(row[1]) < 32
#         and len(row[1]) > 1
#         and not row[1][0].isdigit() # "Campo" does not start with a digit
#         and "RZ_CONT" not in row[1] # Specific exclusion
#         and (row[0].isdigit() or row[0] == "*") # "Nº" column is a digit or '*'
#         and row[1] != "REG" # "Campo" is not "REG"
#     ):
#         return True
#     return False


def _is_field_row(row, last_field_index):
    """Returns True if the row match a series of condition to be a register's field"""
    if (
        row[1] != ""
        and len(row[1]) < 32
        and len(row[1]) > 1
        and not row[1][0].isdigit()
        and "RZ_CONT" not in row[1]  # in ECD, doesn't look like a real data field
        and (
            row[0].isdigit()
            and row[1] != "REG"
            and int(row[0]) == last_field_index + 1
            or row[0] == "*"
        )
    ):
        return True
    else:
        return False


def extract_register_fields(mod, layout, register_name, raw_rows=None, patch=True):
    """Scans the raw_rows to find the rows describing the fields
    of a given register."""
    in_register = False
    last_field_index = 1
    reg_fields = []

    if not raw_rows:
        raw_rows = get_raw_rows(mod, layout)

    for page in raw_rows:
        for row in raw_rows[page]:
            if "".join([str(x) for x in row]) == "" or len(row) < 4:
                continue  # empty line

            row = _format_row(clean_row(row))
            row = _map_row_mod_header(row, mod)
            # N-B : We assume losing performance by cleaning and aligning every row
            # instead of only the worthy ones in order to simplify the identification
            # of register's fields rows (realized by _is_reg_row and _is_field_row).

            if not in_register and _is_reg_row(row) and register_name in row[2]:
                # We found the register's table first row describing the register
                # itself
                in_register = True
                # Add register's name and page columns
                row.insert(0, page)
                row.insert(0, register_name)
                reg_fields.append(row)
                continue

            if in_register:
                if _is_reg_row(row) and register_name not in row[2]:
                    # next register table found -> stopping
                    return reg_fields

                if patch:
                    row = _apply_camelot_patch(mod, layout, register_name, row)

                # TODO : handle instances where the field's row is split in two by a
                # page break. (=all the fields are empty except Description - 3rd
                # column). Example : EFD PIS COFINS page 78 Registro 0200
                if _is_field_row(row, last_field_index):
                    last_field_index = int(row[0])

                    # Add register's name and page columns
                    row.insert(0, page)
                    row.insert(0, register_name)
                    reg_fields.append(row)

    return reg_fields


# 3. `build_accurate_fields_csv`
# ==============================


def build_accurate_fields_csv(
    mod, layout, raw_rows=None, extracted_registers=None, patch=True
):
    """Build a CSV file with the module's fields rows as they appear in the original
    pdf.

    If the registers list is passed as an argument, it avoids to make the extraction
    another time."""
    accurate_file = SPECS_PATH / mod / str(layout) / "accurate_fields.csv"
    reg_with_no_field = []
    if not extracted_registers:
        extracted_registers = extract_registers_list(mod, layout, raw_rows)

    logger.info(f"> Building {mod}_accurate_fields.csv")

    # Catch all the module's fields
    mod_fields = []
    for register in extracted_registers:
        reg_fields = extract_register_fields(
            mod, layout, register["code"], raw_rows, patch
        )

        mod_fields.extend(reg_fields)
        # Catch registers with no fields for information.
        # N-B : A register table must have at least two rows (the first row describes
        # the register itself)
        if len(reg_fields) < 2:
            reg_with_no_field.append(register["code"])

    if reg_with_no_field:
        logger.info(
            f"    /!\\ {len(reg_with_no_field)} registers with no field "
            f"catched by camelot : {reg_with_no_field}"
        )

    with open(accurate_file, "w") as accurate_csv:
        # Delete actual fields_file's datas before writing
        accurate_csv.seek(0)
        accurate_csv.truncate()

        accurate_rows = csv.writer(
            accurate_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )
        # Write module's header
        mod_header = ["Register", "Page"] + [c[0] for c in _get_mod_header(mod)]
        accurate_rows.writerow(mod_header)
        # Write module's fields
        for row in mod_fields:
            accurate_rows.writerow(row)


# 4. `get_fields` and `get_registers`
# ===================================


def _normalize_field_code(code):
    """
    The pdf SPED specification has plenty of typing errors. We fix them here.
    This method can be completed in an incremental form: logging warnings
    during the generation and then creating an exception for them.
    """

    code = code.replace("  ", "").replace(" ", "").replace("__", "_")
    code = code.replace(";", "")  # example COD_SIT; in efd_pis_cofins
    code = code.replace("*", "")  # example  MES_REF* in efd_icms_ipi
    code = code.replace("-", "_")  # example tp_ct-e in efd_pis_cofins
    code = code.replace("/", "_")  # example tp_ct-e in efd_pis_cofins
    code = unidecode(code)  # example NÍVEL in efd_icms_ipi
    new_code = ""
    for char in code:
        if char.isalpha() or char.isdigit() or char == "_":
            new_code += char
        else:  # likely a pdf error
            logger.warning(
                f"field code {code} has bad char '{char}'! '{char}' has been skipped!"
            )
            continue
    return new_code.upper()


def _convert_field_type(field):
    """Return a string giving the 'interpreted' field's type :
    'char', 'int', 'float' or 'date'."""
    spec_type = field.get("spec_type")
    if spec_type:
        code = field["code"]
        if spec_type == "D" or code.startswith("DT_") or code.startswith("DATA_"):
            field["type"] = "date"
        elif spec_type == "N":
            if (
                "*" in field.get("length", "")
                or code.startswith("IND_")
                or code.startswith("COD_")
                or code.startswith("TIPO")
                or "CPF" in code
                or "CNPJ" in code
                or (
                    isinstance(field.get("length", 0), int)
                    or field.get("length", "0").isdigit()
                )
                and not field.get("decimal")
                and int(field.get("length", 0)) > 1
            ):
                # for _IND and COD_ the issue is the Integer Odoo widget sucks
                # so it's better to have a Char field.
                # as for lengths with *, it's a bit the same. These fields can also be void in Odoo
                # without the need to have 0 by default such as True integers.
                field["type"] = "char"
                field["xsd_type"] = "numeric_code"
            elif field.get("decimal") or code.startswith("VL_"):
                field["type"] = "float"
            else:
                field["type"] = "int"
        # If no given type, define it as "character"
        # "NS" ("Numérico Com Sinal") means that the field's value must be "+" ou "-"
        # cf. ECF pdf page 26
        elif not spec_type or spec_type in ["C", "NS"]:
            field["type"] = "char"
        else:
            logger.warning(
                f"    Could not define field {field['code']} type in register "
                f"{field['register']}"
            )
    return field


def _convert_field_required(field):
    """Return field with additional required boolean keys if necessary"""
    spec_required = field.get("spec_required")
    if spec_required in ["O", "S", "Sim", "Sm", "sim"]:
        field["required"] = True
    elif spec_required in ["N", "Não"]:
        field["required"] = False
    elif spec_required == "OC":
        field["conditional_required"] = True
    elif field.get("register") and field.get("spec_required"):
        logger.warning(
            f"    Could not define if field {field['code']} is required in register "
            f"{field['register']}"
        )
    elif field.get("spec_required"):
        # In this case we are converting a register item not a field
        logger.warning(f"    Could not define if register {field['code']} is required")
    return field


def _convert_field_in_out(field):
    # TODO : interpret field["spec_in"] when it is an integer
    # (cf register C170 in EFD_ICMS_IPI page 71)
    spec_in = field.get("spec_in")
    if spec_in == "O":
        field["in_required"] = True
    elif spec_in == "OC":
        field["conditional_in_required"] = True

    spec_out = field.get("spec_out")
    if spec_out == "O":
        field["out_required"] = True
    elif spec_out == "OC":
        field["conditional_out_required"] = True
    return field


def _convert_values(field):
    """Add a 'values' keys if field["spec_values"] can be interpreted as a list of items"""
    values = field.get("spec_values")
    if values:
        # Remove unnecessary quotes
        values = field["spec_values"].replace("”", "").replace("“", "").replace('"', "")
        if values[0] == "[" and values[-1] == "]":
            values = values[1:-1]
        if "," in values:
            values = values.split(",")
        elif ";" in values:
            values = values.split(";")
        if isinstance(values, list):
            field["values"] = [v.replace(" ", "").replace("''", "") for v in values]
        if field.get("spec_type") and field["spec_type"] == "NS":
            field["values"] = ["+", "-"]  # cf. ECF pdf page 26
    # TODO : There is still around 30 fields with "spec_values" which is not easily
    # convertible into a list
    return field


def _convert_rules(field):
    """Convert rules string in a iterable list"""
    rules = field.get("rules")
    if rules:
        field["rules"] = rules[:-1].replace(" ", "").replace("[", "").split("]")
    return field


def _map_field_row(row, mod):
    """Return a field dictionary with interpreted information"""
    field = {}
    mod_keys = [c[1] for c in _get_mod_header(mod)]

    # Catch raw datas from row
    field["register"] = row[0]
    for index, key in enumerate(mod_keys):
        if index + 2 < len(row) and row[index + 2] not in ["-", ""]:
            field[key] = row[index + 2]

    # Interpret raw datas
    field["index"] = int(
        field.get("index", "0").replace("*", "0")
    )  # TODO check * cases
    field["code"] = _normalize_field_code(field["code"])

    field = _convert_field_type(field)
    field = _convert_field_required(field)
    field = _convert_field_in_out(field)
    field = _convert_values(field)
    field = _convert_rules(field)

    return field


def get_fields(mod, layout, with_reg=False):
    """Returns a list of the module's fields recorded as dictionaries with interpreted
    values.

    :param mod: The module from which are catched the fields.
    :type mod: str

    :param layout: The module's layout version.
    :type layout: int

    :param with_reg: An optional argument to add the REG field (opening every registers
    tables) to this list of dictionaries.
    :type with_reg: bool
    """
    # TODO add "Valores Válidos" (ECD), "Regras de Validação do Campo" (ECD), "Entr" (ICMS/IPI), "Saídas" (ICMS/IPI)

    if mod not in MODULES:
        raise ValueError(
            f"'{mod}' is not a valid module name. Choose between {MODULES.keys()}"
        )
    accurate_file = SPECS_PATH / mod / str(layout) / "accurate_fields.csv"
    fields = []

    # Build MODULE_accurate_fields.csv if empty or not existing
    if not accurate_file.exists() or accurate_file.stat().st_size == 0:
        build_accurate_fields_csv(mod, layout)

    # Open the CSV with the accurate fields list
    with open(accurate_file, "r") as accurate_csv:
        accurate_rows = csv.reader(accurate_csv, delimiter=",", quotechar='"')
        # Avoid CSV header
        next(accurate_rows)
        for row in accurate_rows:
            row = _apply_camelot_patch(mod, layout, row[0], row)
            if row[3] != "REG" or with_reg:
                fields.append(_map_field_row(row, mod))

    logger.info(f"    {len(fields)} fields catched in {mod.upper()}")
    return fields


def get_registers(mod, layout, raw_rows=None, extracted_registers=None):
    """Add the `required` and `field_in_out` attributes (calculated from the
    MODULE_accurate_fields.csv file) to the registers extracted by
    `extract_registers_list()` and return this registers list.

    If the `extracted_registers` is passed as an argument, it avoids to make the
    extraction another time."""
    if mod not in MODULES:
        raise ValueError(
            f"'{mod}' is not a valid module name. Choose between {MODULES.keys()}"
        )
    accurate_file = SPECS_PATH / mod / str(layout) / "accurate_fields.csv"
    mod_keys = [c[1] for c in _get_mod_header(mod)]

    if not raw_rows:
        raw_rows = get_raw_rows(mod, layout)
    if extracted_registers:
        registers = extracted_registers
    else:
        registers = extract_registers_list(mod, layout, raw_rows)

    # Build MODULE_accurate_fields.csv if empty or not existing
    if not accurate_file.exists() or accurate_file.stat().st_size == 0:
        build_accurate_fields_csv(mod, layout, raw_rows, registers)

    # Open the CSV with the accurate fields list
    with open(accurate_file, "r") as accurate_csv:
        accurate_rows = csv.reader(accurate_csv, delimiter=",", quotechar='"')
        # Avoid CSV header
        next(accurate_rows)
        for row in accurate_rows:
            if row[3] == "REG":
                for register in registers:
                    if register["code"] == row[0]:
                        # Catch row's 'spec_required', 'spec_in' and 'spec_out'
                        for spec in ["spec_required", "spec_in", "spec_out"]:
                            if spec in mod_keys:
                                index = mod_keys.index(spec) + 2
                                if index < len(row) and row[index] not in ["-", ""]:
                                    register[spec] = row[index]

                        register = _convert_field_required(register)
                        register = _convert_field_in_out(register)
                        break

    logger.info(f"    {len(registers)} registers catched in {mod.upper()}")
    return registers


# 5. `build_usable_fields_csv` and `build_registers_csv`
# ======================================================


def _sort_header_order(key):
    """Reorder hearder's keys"""
    header_base = [
        "register",
        "index",
        "block",
        "code",
        "type",
        "required",
        "in_required",
        "out_required",
        "values",
        "rules",
    ]
    if key == "desc":
        return 99
    elif key.startswith("spec_"):
        return 90
    elif key.startswith("conditional_"):
        return 10
    elif key in header_base:
        return header_base.index(key)
    else:
        return 50


def _get_usable_csv_header(fields):
    """Return a list of all the different keys available in fields"""
    header = []
    for field in fields:
        for key in field.keys():
            if key not in header:
                header.append(key)
    header.sort(key=_sort_header_order)
    return header


def build_usable_fields_csv(mod, layout):
    fields_file = SPECS_PATH / mod / str(layout) / "fields.csv"
    fields = get_fields(mod, layout)
    logger.info(f"> Building {mod} {layout} fields.csv")

    # Open the CSV with the accurate fields list
    with open(fields_file, "w") as f_file:
        # Delete actual usable_file's datas before writing
        f_file.seek(0)
        f_file.truncate()

        fields_csv = csv.writer(
            f_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )

        header = _get_usable_csv_header(fields)
        fields_csv.writerow(header)
        for field in fields:
            row = []
            # Add missing keys with empty values to field
            for col in header:
                if col not in field.keys():
                    field[col] = ""
                row.append(field[col])
            fields_csv.writerow(row)


def build_registers_csv(mod, layout, raw_rows=None, extracted_registers=None):
    """Generate a csv with the Registers specifications. One line for each register.
    If no registers argument is passed, the registers list extraction will be made by
    `get_registers`.
    """
    registers_file = SPECS_PATH / mod / str(layout) / "registers.csv"
    registers = get_registers(mod, layout, raw_rows, extracted_registers)
    header = _get_usable_csv_header(registers)

    logger.info(f"> Building {mod}_registers.csv")

    with open(registers_file, "w") as reg_file:
        # Delete actual reg_file's datas before writing
        reg_file.seek(0)
        reg_file.truncate()

        reg_csv = csv.writer(
            reg_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )
        # First line is columns titles
        reg_csv.writerow(header)
        for register in registers:
            row = []
            # Add missing keys with empty values to field
            for col in header:
                if col not in register.keys():
                    register[col] = ""
                row.append(register[col])
            reg_csv.writerow(row)


# 6. BONUS : `get_blocks` to get module's blocks list
# ======================================================


def extract_blocks(mod, layout, raw_rows=None):
    """Return a list of the module's blocks rows as found in path_raw"""
    extracted_blocks = []
    in_block_list = False

    if not raw_rows:
        raw_rows = get_raw_rows(mod, layout)

    for page in raw_rows:
        for row in raw_rows[page]:
            if (
                len(row) in [2, 3]
                and row[0] == "Bloco"
                and row[1] in ["Descrição", "Nome do Bloco"]
            ):
                in_block_list = True
                continue
            if in_block_list and row[0] != "Bloco":
                extracted_blocks.append(row)
                if row[0] == "9":
                    return extracted_blocks
    if not extracted_blocks:
        logger.warning(f"    /!\\ No Blocks list catched in {mod.upper()}")
        return []


def get_blocks(mod, layout, raw_rows=None, extracted_blocks=None):
    """Return a list of dictionaries representing module's blocks."""
    if mod not in MODULES:
        raise ValueError(
            f"'{mod}' is not a valid module name. Choose between {MODULES.keys()}"
        )
    blocks = []
    if not extracted_blocks:
        extracted_blocks = extract_blocks(mod, layout, raw_rows)
    for row in extracted_blocks:
        block = {}
        block["code"] = row[0].replace("*", "")
        block["desc"] = " ".join(row[1].split())
        if len(row) == 3:  # in ECF
            block["info"] = row[2]
        blocks.append(block)
    return blocks


#  main()
# =========================


@click.command()
@click.option(
    "--patch/--no-patch",
    default=True,
    help="Override fields rows extracted by camelot with rows listed in folder "
    "'..specs/MODULE/LAYOUT/camelot_patch/'",
    show_default=True,
)
def main(patch):
    """Build 3 CSV files for each SPED modules (ECD, ECF, EFD_ICMS_IPI and
    EFD_PIS_COFINS) :

    - MODULE_accurate_fields.csv : list all the module's registers fields as they appear
    in the original pdf tables (useful to check the extracted CSV reliability).

    - MODULE_registers.csv : list the module's registers with its useful information.

    - MODULE_fields.csv : list all the module's registers fields with unified and
    'usable' interpreted values (useful to create python objects from these fields)."""

    for mod in MODULES:
        logger.info(f"\n==== Building CSV files for {mod.upper()} ====")
        layout = MODULES[mod][0]

        patch_file = (
            SPECS_PATH / mod / str(layout) / "camelot_patch" / f"camelot_patch.csv"
        )
        if patch and not patch_file.is_file():
            logger.warning(
                f"    No CSV patch 'camelot_patch.csv' found for {mod.upper()} "
                f"in './specs/{mod}/{layout}/'"
            )

        raw_rows = get_raw_rows(mod, layout)
        extracted_registers = extract_registers_list(mod, layout, raw_rows)

        build_accurate_fields_csv(mod, layout, raw_rows, extracted_registers, patch)
        build_registers_csv(mod, layout, raw_rows, extracted_registers)
        build_usable_fields_csv(mod, layout)

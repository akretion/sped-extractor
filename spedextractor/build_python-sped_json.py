#!/usr/bin/env python3

import csv
import json
import logging

import click
from build_csv import get_blocks, get_fields, get_registers
from years import MOST_RECENT_YEAR, OLDEST_YEAR

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _convert_length(f):
    """Convert field's length in integer when it is possible"""
    tamanho = f.get("length")
    if tamanho:
        try:
            tamanho = int(tamanho)
        except ValueError:
            pass
    return tamanho


def _build_pythonsped_json(mod, year):
    """Build a module dictionary organized with nested registers and fields following
    the structure and the keys for python-sped leiautes and save it as a JSON file"""
    json_path = f"../specs/{year}/{mod}/{mod}_python-sped.json"
    blocks = get_blocks(mod, year)
    registers = get_registers(mod, year)
    fields = get_fields(mod, year, with_reg=True)

    # 1) Initiate dictionary with module's name, date and pdf version taken from the
    # module's download_info.csv file
    module = {}
    module["tipo"] = mod
    with open(f"../specs/{year}/download_info.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        header = next(reader)
        col_mod = header.index("module")
        col_version = header.index("version")
        col_date = header.index("date_init")
        for row in reader:
            if row[col_mod] == mod:
                module["versao"] = row[col_version]
                module["data_inicio"] = row[col_date]

    # 2) Add module's blocks list
    module["blocos"] = []
    for b in blocks:
        block = {}
        block["nome"] = b["code"]
        block["descricao"] = b["desc"]
        module["blocos"].append(block)

    # 3) Add module's registers list
    module["registros"] = []
    for r in registers:
        reg = {}
        reg["codigo"] = r["code"]
        reg["nome"] = r["desc"]
        reg["regras"] = []  # Filled after catching 'campos'
        reg["nivel"] = r.get("level")
        reg["ocorrencia"] = r.get("card") if r.get("card") != "1" else "1:1"
        reg["campos_chave"] = []  # TODO Looks like it is part of the fields codes...
        reg["campos"] = []
        for f in fields:
            if f["register"] == r["code"]:
                campo = {}
                campo["indice"] = f["index"]
                campo["nome"] = f["code"]
                campo["descricao"] = f["desc"]
                # Use spec_type not interpreted f["type"]
                campo["tipo"] = f.get("spec_type", "C")
                campo["tamanho"] = _convert_length(f)
                campo["decimal"] = f.get("decimal")
                # Use spec_values not interpreted f["values"]
                campo["valores"] = f.get("spec_values", "-")
                campo["obrigatorio"] = f.get("required", False)
                campo["regras"] = f.get("rules", [])
                # Append campo
                reg["campos"].append(campo)
        # 4) reg['regras']  gathering all the register fields rules
        # TODO it looks like the python-sped leiaute is not following this idea to fill
        # this reg["regras"] item...
        for c in reg["campos"]:
            if c.get("regras"):
                reg["regras"].extend(c.get("regras"))
        # Append reg
        module["registros"].append(reg)

    with open(json_path, "w") as json_file:
        # Delete actual json_file's datas before writing
        json_file.seek(0)
        json_file.truncate()

        json.dump(module, json_file, ensure_ascii=False, indent=2)


@click.command()
@click.option(
    "--year",
    default=MOST_RECENT_YEAR,
    show_default=True,
    type=click.IntRange(OLDEST_YEAR, MOST_RECENT_YEAR),
    help="Operate on a specific year's folder, "
    f"can be between {OLDEST_YEAR} and {MOST_RECENT_YEAR}",
)
def main(year):
    """Build a JSON file with the module's fields for each module."""
    logger.info("Building JSON files for each modules...\n")
    for mod in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        _build_pythonsped_json(mod, year)
        logger.info(f"> {mod}_python-sped.json\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
This module defines 3 methods in order to build clean CSV files from the CSV
extracted by extract_csv.py :

1. `build_registers_csv` creates CSV files listing module's registers (one CSV
    for each module)
2. `build_accurate_fields_csv` creates CSV files listing register's fields with
    no modification of the fields cells values (also one CSV for each module)
3. `build_usable_fields_csv` creates CSV listing the register's fields but interpreting
    the fields cells values in order to be usable by a third party application.

"""

import csv
import logging
import re
from os import walk

import click

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

# Hard-coding module fields headers because it looks easier to actualize than
# heuristic coding based on observation.
# - Defined "manually" after runing `./get_all_headers.py` script which display all the
# possible headers for a module.
# - Used in _get_mod_header() method.
MODULE_HEADER = {
    "ecd": [
        ("Nº", "index"),
        ("Campo", "code"),
        ("Descrição", "desc"),
        # key "type" reserved for the interpreted field dictionary
        ("Tipo", "spec_type"),
        ("Tamanho", "length"),
        ("Decimal", "decimal"),
        ("Valores Válidos", "spec_values"),
        # key "required" reserved for the interpreted field dictionary
        ("Obrigatório", "spec_required"),
        ("Regras de Validação do Campo", "rules"),
    ],
    "ecf": [
        ("Nº", "index"),
        ("Campo", "code"),
        ("Descrição", "desc"),
        ("Tipo", "spec_type"),
        ("Tamanho", "length"),
        ("Decimal", "decimal"),
        ("Valores Válidos", "spec_values"),
        ("Obrigatório", "spec_required"),
    ],
    "efd_icms_ipi": [
        ("Nº", "index"),
        ("Campo", "code"),
        ("Descrição", "desc"),
        ("Tipo", "spec_type"),
        ("Tam", "length"),
        ("Dec", "decimal"),
        ("Obrig", "spec_required"),
        ("Entr", "spec_in"),
        ("Saídas", "spec_out"),
    ],
    "efd_pis_cofins": [
        ("Nº", "index"),
        ("Campo", "code"),
        ("Descrição", "desc"),
        ("Tipo", "spec_type"),
        ("Tam", "length"),
        ("Dec", "decimal"),
        ("Obrig", "spec_required"),
    ],
}


def _get_mod_header(mod):
    """Override this method if the hard code MODULE_HEADER is not wanted"""
    return MODULE_HEADER.get(mod)


# used to sort csv files
def _atoi(text):
    return int(text) if text.isdigit() else text


# used to sort csv files
def natural_keys(text):
    """
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    """
    return [_atoi(c) for c in re.split(r"(\d+)", text)]


def clean_row(row):
    # Clean content
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


# 1. build_registers_csv
# ===========================


def _is_register_code(code):
    return code and len(code) == 4 and code[1:3].isdigit()


def _map_register_row(mod, row):
    """Extracts register's row information for each kind of file"""
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
        # the most problematic pdf
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
            return register
        else:
            return False
    else:
        return False


def extract_registers(mod):
    """Scans the raw csv tables and return 'registers', a list of dictionaries giving
    all the information about the module's registers (block, code, description,
    hierarchy level and card)."""
    path = "../specs/{}/raw_camelot_csv/".format(mod)
    files = []
    registers = []
    in_block = False

    for (_dirpath, _dirnames, filenames) in walk(path):
        files = sorted(filenames, key=natural_keys)
    for csv_file in files:
        with open(path + "{}".format(csv_file), "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in reader:
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
                    register = _map_register_row(mod, clean_row(row))
                    if register:
                        registers.append(register)
                        if register["code"] == "9999":
                            return registers

    return registers


# TODO : Add in-out required properties to registers CSV
# def _define_register_in_out_required(reg_row, header, register_name, rule_col):
#     """Return if the Register has "Entr"-"Saída" columns (returning `in_out`)
#     and their values given by `in_required` and `out_required`"""
#     in_out = None
#     in_required = None
#     out_required = None
#     cols = len(header)
#     if register_name in reg_row[cols - 2] or register_name in ["Y681"]:  # ECF error
#         in_out = False  # because only 1 col left
#         values_col = cols - 2
#     elif register_name in reg_row[cols - 3]:
#         values_col = cols - 3
#         if reg_row[cols - 1] == reg_row[cols - 2] == "O":
#             in_out = True
#             in_required = True
#             out_required = True
#         elif rule_col is None or rule_col < values_col:
#             in_out = True  # but it never happens
#         else:
#             in_out = False
#     else:
#         if reg_row[cols - 1] == reg_row[cols - 2] == "O":
#             in_out = True
#             in_required = True
#             out_required = True
#         if len(header) == 8 and "Entr" in header[6]:
#             in_out = True
#             if reg_row[cols - 2] == "O":
#                 in_required = True
#             else:
#                 in_required = False
#             if reg_row[cols - 1] == "O":
#                 out_required = True
#             else:
#                 out_required = False
#         else:
#             in_out = False
#     return in_out, in_required, out_required


def build_registers_csv(mod):
    """Generate a csv with the Registers specifications. One line for each register.
    """
    filename = mod + "_registers.csv"
    path = "../specs/{}/{}".format(mod, filename)
    registers = extract_registers(mod)
    header = list(registers[0].keys())

    with open(path, "w") as reg_file:
        # Delete actual reg_file's datas before writing
        reg_file.seek(0)
        reg_file.truncate()

        reg_csv = csv.writer(
            reg_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )
        # First line is columns titles
        reg_csv.writerow(header)
        for row in registers:
            reg_csv.writerow(list(row.values()))


# 2. build_accurate_fields_csv
# ===========================


def _is_reg_row(row):
    if len(row) > 5 and (
        row[1].replace(" ", "") == "REG"
        or row[2].replace(" ", "") == "REG"
        or " REG" in row[0]
    ):
        return True
    return False


def _is_reg_row_match(register_name, row):
    if register_name in "".join(row) and "Texto" in "".join(row):
        return True
    return False


def _apply_camelot_patch(mod, register, row, pdf_year):
    """Catch patched row in ./camelot_patch/ and return override current row"""
    patch_path = "./camelot_patch/" + str(pdf_year) + "/" + mod + "_camelot_patch.csv"

    try:
        with open(patch_path, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for patch_row in reader:
                # N-B : A patch can be applied twice if a row which is not a register's
                # field match this condition (e.g. field TIP_ENT in ECF register 0010).
                # But it is not a problem as the non-field row will be ignore after.
                if patch_row[0] == register and patch_row[2] == row[0]:
                    row = patch_row[2:]
                    logger.info(
                        "    PATCH : field {} in register {}".format(row[1], register)
                    )
    except FileNotFoundError:
        return row
    return row


def _is_joined_index(row, c):
    """ Check if row's column 'c' start with row's index and need to be split"""
    if len(row) > 4 and row[c][0:2].isdigit() and len(row[c]) > 5 and " " in row[c]:
        return True
    return False


def _split_code_desc(row, c):
    """Check if row's column 'c' is a joined code and description and return 2 split
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
    """Separate columns joined together"""
    # change ["04  VL_BC_RET", ""] into ["04","VL_BC_RET"]
    if _is_joined_index(row, 0) and row[1] == "":
        split = row[0].split(" ")
        row = [split[0], " ".join(split[1:])] + row[2:]
    # change ["", "04  VL_BC_RET"] into ["04","VL_BC_RET"]
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


def _is_field_row(row, last_field_index):
    """Return True if the row match a series of condition to be a register's field"""
    if (
        len(row) > 4
        and row[1] != ""
        and len(row[1]) < 32
        and len(row[1]) > 1
        and not row[1][0].isdigit()
        and "RZ_CONT" not in row[1]  # in ECD, doesn't look like a real data field
        and (
            row[0].isdigit()
            and row[1].replace(" ", "") != "REG"
            and int(row[0]) == last_field_index + 1
            or row[0] == "*"
        )
    ):
        return True
    else:
        return False


def _map_row_mod_header(row, mod):
    """Insert empty column when needed to align with module's header columns order"""
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


def extract_accurate_fields(mod, register_name, patch=True):
    """Scans the csv files to find the rows describing the fields
    of a given register."""
    # TODO map back into register: required, in_required, out_required
    path = "../specs/{}/raw_camelot_csv/".format(mod)
    files = []
    in_register = False
    last_field_index = 1
    reg_rows = []

    for (_dirpath, _dirnames, filenames) in walk(path):
        files = sorted(filenames, key=natural_keys)
    for csv_file in files:
        page = int(csv_file.split("-")[2])
        with open(path + csv_file, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in reader:
                if (
                    not in_register
                    and _is_reg_row(row)
                    and _is_reg_row_match(register_name, row)
                ):
                    in_register = True

                if in_register:
                    if "".join(row) == "" or len(row) < 4:
                        continue  # empty line
                    elif _is_reg_row(row) and not _is_reg_row_match(register_name, row):
                        # next register table found -> stopping
                        return reg_rows
                    # TODO : handle instances where the field's row is split in two by a
                    # page break. (=all the fields are empty except Description - 3rd
                    # column). Example : EFD PIS COFINS page 78 Registro 0200

                    row = clean_row(row)
                    row = _format_row(row)
                    if patch:
                        # TODO : Add option to apply patch dependind on the pdf year
                        row = _apply_camelot_patch(mod, register_name, row, 2020)

                    if _is_field_row(row, last_field_index):
                        # Align row cells under module's header
                        row = _map_row_mod_header(row, mod)
                        last_field_index = int(row[0])

                        # Add register's name and page columns
                        row.insert(0, page)
                        row.insert(0, register_name)

                        reg_rows.append(row)

    return reg_rows


def build_accurate_fields_csv(mod, patch=True):
    reg_path = "../specs/{}/{}_registers.csv".format(mod, mod)
    fields_path = "../specs/{}/{}_accurate_fields.csv".format(mod, mod)
    reg_with_no_field = []

    # Open the CSV created by 'build_registers_csv' with the module's
    # registers list
    with open(reg_path, "r") as reg_file, open(fields_path, "w") as fields_file:
        registers = csv.reader(reg_file, delimiter=",", quotechar='"')
        # Pass reg_file header
        next(registers)
        # Delete actual fields_file's datas before writing
        fields_file.seek(0)
        fields_file.truncate()

        fields = csv.writer(
            fields_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )

        mod_rows = []
        mod_header = ["Register", "Page"] + [c[0] for c in _get_mod_header(mod)]
        fields.writerow(mod_header)
        for reg_line in registers:
            reg_name = reg_line[1]
            reg_rows = extract_accurate_fields(mod, reg_name, patch)
            mod_rows.extend(reg_rows)
            if not reg_rows:
                reg_with_no_field.append(reg_name)

        logger.info("    Fields number in {} : {}".format(mod.upper(), len(mod_rows)))
        logger.info(
            "    /!\\ {} registers with no field catched by camelot : {}".format(
                len(reg_with_no_field), reg_with_no_field
            )
        )
        for row in mod_rows:
            fields.writerow(row)


# 3. build_usable_fields_csv
# ===========================


def _normalize_field_code(code):
    # TODO return original_name attr if need to remove accents
    return code.replace("  ", "").replace(" ", "").replace("__", "_")
    # .replace('ÇÃO', 'CAO')


def _convert_field_type(field):
    """Return a string giving the 'interpreted' field's type :
    'char', 'int', 'float' or 'date'. """
    spec_type = field["spec_type"]
    code = field["code"]

    if spec_type == "D" or code.startswith("DT_") or code.startswith("DATA_"):
        return "date"
    elif spec_type == "N":
        return "float" if field.get("decimal") else "int"
    # If no given type, define it as "character"
    # "NS" ("Numérico Com Sinal") means that the field's value must be "+" ou "-"
    # cf. ECF pdf page 26
    elif not spec_type or spec_type in ["C", "NS"]:
        return "char"
    else:
        logger.warning(
            "Could not define field {} type in register {}".format(
                field["code"], field["register"]
            )
        )
        return "undefined"


def _convert_field_required(field):
    """Return field with additional required boolean keys if necessary"""
    spec_required = field["spec_required"]
    if spec_required in ["O", "S", "Sim", "Sm", "sim"]:
        field["required"] = True
    elif spec_required in ["N", "Não"]:
        field["required"] = False
    elif spec_required == "OC":
        field["conditional_required"] = True
    else:
        logger.warning(
            "Could not define if field {} is required in register {}".format(
                field["code"], field["register"]
            )
        )
    return field


def _convert_field_in_out(field):
    # TODO : interpret field["spec_in"] when it is an integer
    # (cf register C170 in EFD_ICMS_IPI page 71)
    spec_in = field.get("spec_in")
    if spec_in == "0":
        field["in_required"] = True
    elif spec_in == "OC":
        field["conditional_in_required"] = True

    spec_out = field.get("spec_out")
    if spec_out == "0":
        field["out_required"] = True
    elif spec_out == "OC":
        field["conditional_out_required"] = True
    return field


def _convert_values(field):
    """Add a 'values' keys if field["spec_values"] can be interpreted as a list of items
    """
    # Remove unnecessary quotes
    values = field["spec_values"].replace("”", "").replace("“", "").replace('"', "")
    if values[0] == "[" and values[-1] == "]":
        values = values[1:-1]
    if "," in values:
        values = values.split(",")
    elif ";" in values:
        values = values.split(";")
    if type(values) == list:
        field["values"] = [v.replace(" ", "").replace("''", "") for v in values]
    # TODO : There is still around 30 fields with "spec_values" which is not easily
    # convertible into a list
    return field


def _convert_rules(rules):
    """Convert rules string in a iterable list"""
    return rules[:-1].replace(" ", "").replace("[", "").split("]")


def _map_field_row(row, mod):
    """Return a field dictionary with its interpreted row information given by the
    accurate csv file"""
    field = {}
    mod_keys = [c[1] for c in _get_mod_header(mod)]

    # Catch raw datas from row
    field["register"] = row[0]
    for index, key in enumerate(mod_keys):
        if index + 2 < len(row) and row[index + 2] not in ["-", ""]:
            field[key] = row[index + 2]

    # Interpret raw datas
    field["index"] = int(field["index"].replace("*", "0"))  # TODO check * cases
    field["code"] = _normalize_field_code(field["code"])
    if field.get("spec_type"):
        field["type"] = _convert_field_type(field)
    if field.get("spec_required"):
        field = _convert_field_required(field)
    if field.get("spec_in") or field.get("spec_out"):
        field = _convert_field_in_out(field)
    if field.get("spec_values"):
        field = _convert_values(field)
    if field.get("rules"):
        field["rules"] = _convert_rules(field["rules"])

    return field


def extract_fields(mod):
    """Return the list of the module's fields recorded as dictionaries which keys
    are given by the MODULE_HEADER tuples"""
    accurate_path = "../specs/{}/{}_accurate_fields.csv".format(mod, mod)
    fields = []

    # Open the CSV with the accurate fields list
    with open(accurate_path, "r") as accurate_file:
        accurate_fields = csv.reader(accurate_file, delimiter=",", quotechar='"')
        # Avoid CSV header
        next(accurate_fields)
        for row in accurate_fields:
            fields.append(_map_field_row(row, mod))

    return fields


def _get_usable_csv_header(fields):
    """Return a list of all the different keys available in fields"""
    header = []
    for field in fields:
        for key in field.keys():
            if key not in header:
                header.append(key)
    # Reorder hearder's keys
    header_base = ["register", "index", "code", "type", "required", "values", "rules"]

    def sort_order(key):
        if key == "desc":
            return 99
        elif key.startswith("spec_"):
            return 90
        elif key.startswith("conditional_"):
            return 5
        elif key in header_base:
            return header_base.index(key)
        else:
            return 50

    header.sort(key=sort_order)
    return header


def build_usable_fields_csv(mod):
    usable_path = "../specs/{}/{}_fields.csv".format(mod, mod)
    fields = extract_fields(mod)

    # Open the CSV with the accurate fields list
    with open(usable_path, "w") as usable_file:
        # Delete actual usable_file's datas before writing
        usable_file.seek(0)
        usable_file.truncate()

        usable_fields = csv.writer(
            usable_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )

        header = _get_usable_csv_header(fields)
        usable_fields.writerow(header)
        for field in fields:
            row = []
            # Add missing keys with empty values to field
            for col in header:
                if col not in field.keys():
                    field[col] = ""
                row.append(field[col])
            usable_fields.writerow(row)


@click.command()
# TODO : Add argument to this patch option in order to choose the folder with the right
# year's patches
@click.option(
    "--patch/--no-patch",
    default=True,
    help="Override fields rows extracted by camelot with rows listed in folder "
    "'./camelot_patch/2019/'",
    show_default=True,
)
def main(patch):
    """Build 3 CSV files for each SPED modules (ECD, ECF, EFD_ICMS_IPI and
    EFD_PIS_COFINS) :

    - MODULE_registers.csv : list the module's registers with its useful information.

    - MODULE_accurate_fields.csv : list all the module's registers fields as they appear
    in the original pdf tables (useful to check the extracted CSV reliability).

    - MODULE_fields.csv : list all the module's registers fields with unified and
    'usable' interpreted values (useful to create python objects from these fields)."""

    for module in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        logger.info("\nBuilding CSV files for {}...".format(module.upper()))
        logger.info("> {}_registers.csv".format(module))
        build_registers_csv(module)

        logger.info("> {}_accurate_fields.csv".format(module))
        build_accurate_fields_csv(module, patch)

        logger.info("> {}_fields.csv".format(module))
        build_usable_fields_csv(module)


if __name__ == "__main__":
    main()

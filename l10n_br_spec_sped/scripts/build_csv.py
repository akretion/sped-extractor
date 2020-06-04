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

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

# Hard-coding module fields headers because it looks easier to actualize than
# heuristic coding based on observation.
# - Defined "manually" after runing `get_all_headers()` method which display all the
# possible headers for a module.
# - Used in _get_mod_header() method.
MODULE_HEADER = {
    "ecd": [
        "Nº",
        "Campo",
        "Descrição",
        "Tipo",
        "Tamanho",
        "Decimal",
        "Valores Válidos",
        "Obrigatório",
        "Regras de Validação do Campo",
    ],
    "ecf": [
        "Nº",
        "Campo",
        "Descrição",
        "Tipo",
        "Tamanho",
        "Decimal",
        "Valores Válidos",
        "Obrigatório",
    ],
    "efd_icms_ipi": [
        "Nº",
        "Campo",
        "Descrição",
        "Tipo",
        "Tam",
        "Dec",
        "Obrig",
        "Entr",
        "Saídas",
    ],
    "efd_pis_cofins": ["Nº", "Campo", "Descrição", "Tipo", "Tam", "Dec", "Obrig"],
}

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


def _is_joined_columns(row, c):
    """ Check if row's column 'c' need to be split"""
    if len(row) > 4 and row[c][0:2].isdigit() and len(row[c]) > 5 and " " in row[c]:
        return True
    return False


def clean_row(row):
    # Separate the 2 first columns joined together
    # Change ["04  VL_BC_RET", ""] into ["04","VL_BC_RET"]
    if _is_joined_columns(row, 0) and row[1] == "":
        split = row[0].split(" ")
        row = [row[0][0:2], split[len(split) - 1]] + row[2 : len(row) - 1]
    # Change ["", "04  VL_BC_RET"] into ["04","VL_BC_RET"]
    if _is_joined_columns(row, 1) and row[0] == "":
        split = row[1].split(" ")
        row = [row[1][0:2], split[len(split) - 1]] + row[2 : len(row) - 1]

    # Clean content
    for index, cell in enumerate(row):
        clean_cell = cell
        if "\n" in cell:
            clean_cell = cell.replace("\n", "").replace("  ", " ").replace("  ", " ")
        # Change "Entr." to "Entr" in fields table's headers
        if re.match(r"^[a-zA-Z]+\.$", cell):
            clean_cell = cell[:-1]
        if clean_cell != cell:
            row[index] = clean_cell
    return row


# 1. build_registers_csv
# ===========================


def _is_register_code(code):
    return code and len(code) == 4 and code[1:3].isdigit()


def _map_register_row(mod, row):
    """extracts register's row information for each kind of file, deal with CSV errors"""
    # TODO : Join rows content when they are from the same register's line but
    # splited in two because of page break.
    # Example : EFD ICMS IPI pdf Outubro 2019 p20-21
    v = {}
    if len(row) > 2:
        if mod == "ecd":
            if len(row[0]) == 1 and row[0] != "":
                v = {
                    "block": row[0],
                    "code": row[2],
                    "desc": row[1],
                    "level": row[3],
                    "card": row[4],
                }
        elif mod == "ecf":
            if len(row[0]) == 4:
                v = {
                    "block": row[0][0],
                    "code": row[0],
                    "desc": row[2],
                    "level": row[1],
                    "card": row[5],
                }
        # the most problematic pdf
        elif mod == "efd_pis_cofins":
            if len(row[2]) == 4 and len(row) >= 5:
                v = {
                    "block": row[0],
                    "code": row[2],
                    "desc": row[1],
                    "level": row[3],
                    "card": row[4],
                }

        elif mod == "efd_icms_ipi":
            if len(row[0]) == 1 and row[0] != "":
                v = {
                    "block": row[0],
                    "code": row[2],
                    "desc": row[1],
                    "level": row[3],
                    "card": row[4],
                }

    if v.get("code") and _is_register_code(v["code"]):
        if str(v["level"]).isdigit():
            v["level"] = int(v["level"])
            return v
        else:
            return False
    else:
        return False


def extract_registers(mod):
    """Scans the raw csv tables and return 'rows', a list of dictionaries giving all the
    information about the module's registers (block, code, description, hierarchy level
    and card)."""
    path = "../specs/{}/raw/".format(mod)
    files = []
    rows = []
    in_register = False

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
                    in_register = True
                    continue
                if in_register:
                    if "".join(row) == "":
                        continue  # empty line
                    v = _map_register_row(mod, clean_row(row))
                    if v:
                        rows.append(v)
                        if v["code"] == "9999":
                            return rows

    return rows


def build_registers_csv(mod):
    """Generate a csv with the Registers specifications. One line for each register.
    """
    filename = mod + "_registers.csv"
    path = "../specs/{}/{}".format(mod, filename)
    rows = extract_registers(mod)
    header = list(rows[0].keys())

    with open(path, "w") as reg_file:
        # Delete actual reg_file's datas before writing
        reg_file.seek(0)
        reg_file.truncate()

        # Write rows
        reg_csv = csv.writer(
            reg_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )
        # First line is columns titles
        reg_csv.writerow(header)
        for row in rows:
            reg_csv.writerow(list(row.values()))


# 2. build_accurate_fields_csv
# ===========================


def _is_field_row(row, last_field_index, register):
    """Return True if the row match a series of condition to be a register's field"""
    if (
        len(row) > 4
        and row[1].upper() == row[1]
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


def apply_camelot_patch(mod, register, row, pdf_year):
    """Catch patched row in ./camelot_patch/ and return override current row"""
    patch_path = "./camelot_patch/" + str(pdf_year) + "/" + mod + "_camelot_patch.csv"

    try:
        with open(patch_path, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for patch_row in reader:
                if patch_row[0] == register and patch_row[2] == row[0]:
                    row = patch_row[2:]
                    logger.info(
                        "PATCHED ROW in register {} :\n{}".format(register, row)
                    )
    except FileNotFoundError:
        return row
    return row


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


def _get_mod_header(mod):
    """Override this method if the hard code MODULE_HEADER is not wanted"""
    return MODULE_HEADER.get(mod)


def _map_row_mod_header(row, mod):
    len_header = len(_get_mod_header(mod))

    if row and mod == "efd_icms_ipi":
        if len(row) == len_header - 1:
            # i.e. row has the columns 'Entr' and 'Saída' but not 'Obrig'
            row.insert(6, "")

    return row


def get_all_headers(mod):
    """Return a list of all the different fields headers found in the module.
    Used to define module's header hard-coded at the beginning of this script."""
    path = "../specs/{}/raw/".format(mod)
    files = []
    previous_row = False
    headers = []

    for (_dirpath, _dirnames, filenames) in walk(path):
        files = sorted(filenames, key=natural_keys)
    for csv_file in files:
        with open(path + csv_file, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in reader:
                if _is_reg_row(row) and previous_row not in headers:
                    headers.append(previous_row)
                previous_row = row
    return headers


def extract_fields_rows(mod, register_name):
    """scans the csv files to find the rows describing the fields
    of a given register."""
    # TODO map back into register: required, in_required, out_required
    path = "../specs/{}/raw/".format(mod)
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
                    row = apply_camelot_patch(mod, register_name, row, 2019)

                    if _is_field_row(row, last_field_index, register_name):
                        # Align row cells under module's header
                        row = _map_row_mod_header(row, mod)
                        last_field_index = int(row[0])

                        # Add register's name and page columns
                        row.insert(0, page)
                        row.insert(0, register_name)

                        reg_rows.append(row)

    return reg_rows


def build_accurate_fields_csv(mod):
    reg_path = "../specs/{}/{}_registers.csv".format(mod, mod)
    fields_path = "../specs/{}/{}_fields.csv".format(mod, mod)

    # Open the CSV created by 'build_registers_csv' with the module's
    # registers list
    with open(reg_path, "r") as reg_file, open(fields_path, "w") as fields_file:
        registers = csv.reader(reg_file, delimiter=",", quotechar='"')
        # Delete actual fields_file's datas before writing
        fields_file.seek(0)
        fields_file.truncate()

        fields = csv.writer(
            fields_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )

        mod_rows = []
        mod_header = ["Register", "Page"] + _get_mod_header(mod)
        fields.writerow(mod_header)
        for reg_line in registers:
            reg_name = reg_line[1]
            reg_rows = extract_fields_rows(mod, reg_name)
            mod_rows.extend(reg_rows)

        logger.info("Fields number in {} : {}".format(mod.upper(), len(mod_rows)))
        for row in mod_rows:
            fields.writerow(row)


# 3. build_usable_fields_csv
# ===========================


def normalize_field_code(code):
    # TODO lookup table for manual name patches
    # TODO return original_name attr if need to remove accents
    return (
        (code.replace("  ", " ").replace("__", "_").replace(" _", "_"))
        .replace("_ ", "_")
        .replace(" ", "_")
        .replace(r"\r", "")
    )
    # .replace('ÇÃO', 'CAO')


def infer_field_type(name, spec_type, row):
    # TODO use more and refine with values (Boolean) + Monetary/Dec
    if name.startswith("DT_") or name.startswith("DATA_"):
        return "D"
    elif spec_type == "D":  # Date
        return "D"
    elif spec_type and "N" in spec_type:  # Numeric
        return "N"
    elif spec_type == "C":  # Char
        return "C"
    else:
        for i in row[1 : len(row) - 1]:
            if i.isdigit() and int(i) > 16:  # char size assumed
                return "C"
        return None


def map_field_row(mod, page, register, row, headers, in_out):
    "extracts field information from its row in the csv file"
    # TODO extract possible values (valores)
    # TODO extract rules to mention them (to suggest overrides)
    v = {
        "index": int(row[0].replace("*", "0")),  # TODO check * cases
        "code": normalize_field_code(row[1]),
        "page": page,
        "desc": row[2],
    }

    # past this point, iteration is required to find the field type
    # while dealing with pissible blank columns.
    items = iter(row[3:50])
    index = 2
    for item in items:
        if item in ("C", "N", "NS", "N’", "D"):  # all known types
            v["spec_type"] = item  # keep original value for reference
            if item == "D":  # Date
                v["type"] = "D"
            elif "N" in item:  # Numeric
                v["type"] = "N"
            else:  # Char
                v["type"] = "C"
            try:
                while True:  # hunt for size, digits, values and required
                    i = next(items)
                    index += 1
                    if i.replace("*", "").isdigit():
                        if v["type"] == "N":
                            if v.get("int_size"):
                                # TODO can it be Decimal with no int_size?
                                # -> yes it can!! TODO
                                v["digits"] = int(i.replace("*", ""))
                            else:
                                v["int_size"] = int(i.replace("*", ""))
                        else:
                            v["length"] = i
                    if i in ["O", "S", "Sim", "OC"]:
                        if not in_out:
                            # O "OC" significa que o campo deve ser preenchido
                            # sempre que houver a informação.
                            if i == "OC":
                                v["conditional_required"] = True
                            else:
                                v["required"] = True
                            break
                        else:  # in and out case:
                            j = next(items)
                            if j in ["O", "S", "Sim", "OC"]:
                                if i == "OC":
                                    v["conditional_required_in"] = True
                                if j == "OC":
                                    v["conditional_required_out"] = True
                                else:
                                    v["required"] = True
                                break
                            # TODO deal with in not required and out required
            except StopIteration:
                break
            break
        elif item != "":
            pass
            # TODO print and ensure all cases are dealt with (some
            # are properly dealt when type is discovered later, but check)
            #    row[2] = 'desc (skipped here)'
            #    print("BBBBBBBBBBBBBB", row)
    if not v.get("type"):
        f_type = infer_field_type(v["code"], None, row)
        if f_type is not None:
            v["type"] = f_type
    show_problematic_field_rows(row, page, v)
    return v


def show_problematic_field_rows(row, page, v):
    if not v.get("type") or v["type"] is None:
        row[2] = "desc (skipped here)"
        logger.info("page {}, field type cannot be resolved:{}".format(page, row))


def _define_register_in_out_required(reg_row, header, register_name, rule_col):
    """Return if the Register has "Entr"-"Saída" columns (returning `in_out`)
    and their values given by `in_required` and `out_required`"""
    in_out = None
    in_required = None
    out_required = None
    cols = len(header)
    if register_name in reg_row[cols - 2] or register_name in ["Y681"]:  # ECF error
        in_out = False  # because only 1 col left
        values_col = cols - 2
    elif register_name in reg_row[cols - 3]:
        values_col = cols - 3
        if reg_row[cols - 1] == reg_row[cols - 2] == "O":
            in_out = True
            in_required = True
            out_required = True
        elif rule_col is None or rule_col < values_col:
            in_out = True  # but it never happens
        else:
            in_out = False
    else:
        if reg_row[cols - 1] == reg_row[cols - 2] == "O":
            in_out = True
            in_required = True
            out_required = True
        if len(header) == 8 and "Entr" in header[6]:
            in_out = True
            if reg_row[cols - 2] == "O":
                in_required = True
            else:
                in_required = False
            if reg_row[cols - 1] == "O":
                out_required = True
            else:
                out_required = False
        else:
            in_out = False
    return in_out, in_required, out_required


if __name__ == "__main__":
    for module in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        logger.info(
            "\nBuilding the CSV file with the {}'s registers list".format(
                module.upper()
            )
        )
        build_registers_csv(module)

        logger.info(
            "Building the CSV files with the fields for each {}'s registers".format(
                module.upper()
            )
        )
        build_accurate_fields_csv(module)

        # OPTIONAL : log the different headers found in the module in order to define
        # hard-coded unified module's header at the beginning of this script
        # headers = get_all_headers(module)
        # logger.info("{}'s headers :".format(module.upper()))
        # for header in headers:
        #     logger.info(header)

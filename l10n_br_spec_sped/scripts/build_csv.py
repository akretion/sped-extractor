#!/usr/bin/env python3
"""
This module define 2 methods in order to build clean CSV files from the CSV
extracted by extract_csv.py :

1. `build_registers_spec_csv` create CSV files listing module's registers (one CSV
    for each module)
2. `build_fields_spec_csv` create CSV files listing register's fields (one CSV for
    each register)

"""

import csv
import logging
import re
from os import walk

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


# used to sort csv files
def atoi(text):
    return int(text) if text.isdigit() else text


# used to sort csv files
def natural_keys(text):
    """
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    """
    return [atoi(c) for c in re.split(r"(\d+)", text)]


# 1. build_registers_spec_csv
# ===========================


def is_register_code(code):
    return code and len(code) == 4 and code[1:3].isdigit()


def map_register_row(mod, row):
    """extracts row information for each kind of file, deal with CSV errors"""
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

    if v.get("code") and is_register_code(v["code"]):
        if str(v["level"]).isdigit():
            v["level"] = int(v["level"])
            # Clean description
            v["desc"] = (
                v["desc"]
                .replace("\n", "")
                .replace("\r", "")
                .replace("  ", " ")
                .replace("  ", " ")
            )
            v["card"] = v["card"].replace("\n", "").replace("\r", "")
            return v
        else:
            return False
    else:
        return False


def extract_registers_spec(mod):
    """scans the csv tables to read the registers (registros),
    specially their description and hierarchy."""
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
                    v = map_register_row(mod, row)
                    if v:
                        rows.append(v)
                        if v["code"] == "9999":
                            return rows

    return rows


def build_registers_spec_csv(mod):
    """Generate a csv with the Registers specifications. One line for each register.
    """
    filename = mod + "_reg_spec.csv"
    path = "../specs/{}/{}".format(mod, filename)
    rows = extract_registers_spec(mod)
    header = list(rows[0].keys())

    with open(path, "w") as reg_spec_file:
        # Delete actual reg_spec_file's datas before writing
        reg_spec_file.seek(0)
        reg_spec_file.truncate()

        # Write rows
        reg_spec_csv = csv.writer(
            reg_spec_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )
        # First line is columns titles
        reg_spec_csv.writerow(header)
        for row in rows:
            reg_spec_csv.writerow(list(row.values()))


# 2. build_fields_spec_csv
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


def row_patches():
    """for rows that were not extracted properly in the csv with camelot,
    we manually maintain e dictionary of proper rows. The key is formed with
    the module-the register-the field index.
    The field description is not required if the csv has it properly.
    """
    return {
        "ecf-Y671-8": ["8", "VL_INC_FIN", None, "N", "19", "2", "-", "Não"],
        "ecf-0020-33": [
            "33",
            "IND_DEREX",
            """Declaração sobre utilização dos recursos"""
            """em moeda estrangeira decorrentes do recebimento
de exportações (DEREX)
S – Sim
N – Não""",
            "C",
            "1",
            "-",
            "[S;N]",
            "Sim",
        ],
        "efd_icms_ipi-1391-11": ["11", "SAÍDAS", None, "N", "-", "02", "OC"],
        "efd_pis_cofins-0120-02": [
            "02",
            "MES_REFER",
            "Mês de referência do ano-calendário da"
            "escrituração  sem dados, dispensada da entrega. "
            "Campo a ser preenchido no formato “mmaaaa”",
            "C",
            "006*",
            "-",
            "S",
        ],
    }


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


def is_register_first_row(row):
    if len(row) > 5 and (
        row[1].replace(" ", "") == "REG"
        or row[2].replace(" ", "") == "REG"
        or " REG" in row[0]
    ):
        return True
    return False


def is_register_first_row_match(register_name, row):
    if register_name in "".join(row) and "Texto" in "".join(row):
        return True
    return False


def is_field_row_start(row, last_field_index, register):
    if (
        len(row) > 4
        and row[1].upper() == row[1]
        and row[1] != ""
        and len(row[1]) < 32
        and len(row[1]) > 1
        and not row[1][0].isdigit()
        and (
            row[0].isdigit()
            and row[1].replace(" ", "") != "REG"
            and int(row[0]) == last_field_index + 1
            or row[0] == "*"
        )
    ):
        return True
    #    if row[0].isdigit() and int(row[0]) == last_field_index + 2:
    #        print("WARNING FIELD LIKELY MISSED FROM %s, %s to %s" % (register,
    #                                                                 last_field_index,
    #                                                                 row[0]))
    return False


def is_field_row(mod, register, row, last_field_index):
    if "RZ_CONT" in row[1]:  # ECD, doesn't look like a real data field
        return False, row
    patch = row_patches().get("{}-{}-{}".format(mod, register, row[0]))
    if not patch:  # in case 1st is a blank before position
        patch = row_patches().get("{}-{}-{}".format(mod, register, row[1][0:2]))
    if patch:
        logger.info("PATCHING ROW: {} {}".format(register, patch))
        if patch[2] is None:  # assuming descr was correct
            patch[2] = row[2]
        row = patch
        return True, row
    else:
        if len(row) > 5 and row[0] == "":  # sometimes 1st is a blank
            row.pop(0)
        if (
            mod == "efd_pis_cofins"
            and len(row) > 4
            and row[0][0:2].isdigit()
            and len(row[0]) > 6
        ):
            split = row[0].split(" ")
            row = [row[0][0:2], split[len(split) - 1]] + row[2 : len(row) - 1]
        test = is_field_row_start(row, last_field_index, register)
        return test, row


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


def extract_fields_spec(mod, register_name):
    """scans the csv files to find the rows describing the fields
    of a given register."""
    # TODO map back into register: required, in_required, out_required
    path = "../specs/{}/raw/".format(mod)
    files = []
    in_register = False
    header = False
    header_candidate = False
    cols = 0
    values_col = None
    rule_col = None
    last_field_index = 1
    rows = []

    for (_dirpath, _dirnames, filenames) in walk(path):
        files = sorted(filenames, key=natural_keys)
    for csv_file in files:
        page = int(csv_file.split("-")[2])
        if register_name == "I510" and csv_file == "ecd-page-20-table-1.csv":
            continue  # seems like a false positive, real table is later
        with open(path + csv_file, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in reader:
                if (
                    not in_register
                    and is_register_first_row(row)
                    and is_register_first_row_match(register_name, row)
                ):
                    in_register = True
                    # The register header is the previous row of this current row
                    # (which is matching to be the table's first row)
                    header = header_candidate

                    c = 0
                    for index, col_name in enumerate(header):
                        if "Regras" in col_name:
                            rule_col = c
                        c += 1
                        # Clean header columns names
                        clean_name = col_name
                        if "\n" in col_name:
                            clean_name = col_name.replace("\n", "").replace("  ", " ")
                        if re.match(r"^[a-zA-Z]+\.$", col_name):
                            clean_name = col_name[:-1]
                        if clean_name != col_name:
                            header[index] = clean_name

                        (
                            in_out,
                            in_required,
                            out_required,
                        ) = _define_register_in_out_required(
                            row, header, register_name, rule_col
                        )

                    if in_out is True and (in_required is None or out_required is None):
                        logger.warning(
                            "WARNING the register '{}' has not a 'REG' row valid :\
                            \n{}\n{}".format(
                                register_name, header, row
                            )
                        )
                    continue
                if in_register:
                    if "".join(row) == "" or len(row) < 4:
                        continue  # empty line
                    elif is_register_first_row(row) and not is_register_first_row_match(
                        register_name, row
                    ):
                        # next register table found -> stopping
                        return header, rows
                    test, row = is_field_row(mod, register_name, row, last_field_index)
                    if test:
                        v = map_field_row(mod, page, register_name, row, header, in_out)
                        last_field_index = v["index"]
                        rows.append(v)
                elif "".join(row) != "":
                    header_candidate = row
    return header, rows


def build_fields_spec_csv(mod):
    reg_spec_path = "../specs/{}/{}_reg_spec.csv".format(mod, mod)
    fields_spec_path = "../specs/{}/{}_fields_spec.csv".format(mod, mod)

    # Open the CSV created by 'build_registers_spec_csv' with the module's
    # registers list
    with open(reg_spec_path, "r") as reg_spec_file, open(
        fields_spec_path, "w"
    ) as fields_file:
        # Delete actual fields_file's datas before writing
        fields_file.seek(0)
        fields_file.truncate()

        reg_spec = csv.reader(reg_spec_file, delimiter=",", quotechar='"')
        fields = csv.writer(
            fields_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )

        # First collect all the module's fields headers and all the rows
        headers = []
        rows = []
        for reg_spec_line in reg_spec:
            reg_name = reg_spec_line[1]
            reg_header, reg_rows = extract_fields_spec(mod, reg_name)
            rows.extend(reg_rows)

        # First line is columns titles
        fields.writerow(rows[0].keys())
        for row in rows:
            fields.writerow(list(row.values()))


if __name__ == "__main__":
    for module in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        logger.info(
            "\nBuilding the CSV file with the {}'s registers list".format(
                module.upper()
            )
        )
        build_registers_spec_csv(module)

        logger.info(
            "Building the CSV files with the fields for each {}'s registers".format(
                module.upper()
            )
        )
        build_fields_spec_csv(module)

#!/usr/bin/env python3

import csv
import re
from os import walk


def is_register_code(code):
    return code and len(code) == 4 and code[1:3].isdigit()


def map_register_row(mod, row):
    # extracts row information for each kind of file, deal with CSV errors
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
            if len(row[2]) == 4:
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


# used to sort csv files
def atoi(text):
    return int(text) if text.isdigit() else text


# used to sort csv files
def natural_keys(text):
    """
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    """
    return [atoi(c) for c in re.split(r"(\d+)", text)]


# used to sort register name according to their bloc
def register_keys(text):
    if text[0] == "9":  # bloc 9 registers come at last
        return ["Z", text[1:3]]
    else:
        return [atoi(c) for c in re.split(r"(\d+)", text)]


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
                    else:
                        break

    return rows


def build_registers_spec_csv(mod):
    """Generate a csv with the Registers specifications. One line for each register.
    """
    filename = mod + "_reg_spec.csv"
    path = "../specs/{}/{}".format(mod, filename)
    rows = extract_registers_spec(mod)
    title = list(rows[0].keys())

    with open(path, "w") as reg_spec_file:
        # Delete actual reg_spec_file's datas before writing
        reg_spec_file.seek(0)
        reg_spec_file.truncate()

        # Write rows
        reg_spec_csv = csv.writer(
            reg_spec_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )
        # First line is columns titles
        reg_spec_csv.writerow(title)
        for row in rows:
            reg_spec_csv.writerow(list(row.values()))


if __name__ == "__main__":
    build_registers_spec_csv("ecd")
    build_registers_spec_csv("ecf")
    build_registers_spec_csv("efd_icms_ipi")
    build_registers_spec_csv("efd_pis_cofins")

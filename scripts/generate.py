#!/usr/bin/env python3

# Copyright 2017-2018 Akretion LTDA (http://www.akretion.com)
# @author Raphael Valyi (rvalyi@akretion.com.br)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

# ==================================
#
# WORK IN PROGRESS...
#
# ===================================

"""
Synopsis:
    Generate Odoo SPED model definitions.
Usage:
    python generate.py [options]
Options:
    -f, --force
            Overwrite models.py and forms.py without asking.
    --no-class-suffixes
            Do not add suffix "_model" and _form" to generated class names.
    -h, --help
            Show this help message.
"""


import csv
import getopt
import os
import re
import sys
from os import walk

from unidecode import unidecode

# from sped.escrituracao import Escrituracao


PRINT_HIERARCHY = False


class ProgramOptions(object):
    def get_force_(self):
        return self.force_

    def set_force_(self, force):
        self.force_ = force

    force = property(get_force_, set_force_)


class Writer(object):
    def __init__(self, outfilename, stdout_also=False, mode="w"):
        self.outfilename = outfilename
        self.outfile = open(outfilename, mode)
        self.stdout_also = stdout_also
        self.line_count = 0

    def get_count(self):
        return self.line_count

    def write(self, content):
        self.outfile.write(content)
        if self.stdout_also:
            sys.stdout.write(content)
        count = content.count("\n")
        self.line_count += count

    def close(self):
        self.outfile.close()


# used to sort register name according to their block
def register_keys(text):
    if text[0] == "9":  # block 9 registers come at last
        return ["Z", text[1:3]]
    else:
        return [atoi(c) for c in re.split(r"(\d+)", text)]


def compare_register_fields(module_name, registers):
    "compares register_fields found scanning the PDF with python-sped when possible"
    registers_lib = Escrituracao(module_name, 2017)._registros
    error_count = 0
    field_count = 0
    for register_info in registers:
        register_name = register_info["code"]
        register_lib = getattr(registers_lib, "Registro{}".format(register_name))
        lib_fields = [f.nome for f in register_lib.campos if f.nome != "REG"]
        # TODO move field extraction outside from method?
        headers, rows = extract_fields_spec(module_name, register_name)
        register_info["spec_fields"] = rows
        spec_fields = [f["code"] for f in rows]
        extra_spec = list(set(spec_fields) - set(lib_fields))
        extra_lib = list(set(lib_fields) - set(spec_fields))
        if len(extra_spec) > 0 or len(extra_lib) > 0:
            print("\n{}".format(register_name))
            if len(extra_lib) > 0:
                print("     missing in pdf: %s" % (extra_lib))
            if len(extra_spec) > 0:
                print("     missing in python-sped: %s" % (extra_spec))
            error_count += len(extra_spec) + len(extra_lib)
        field_count += len(lib_fields)
        # TODO also report field types error (very likely inside python-sped)
    print(
        "\n %s field errors out of %s\
          fields (%s percent)"
        % (error_count, field_count, 100.0 / (field_count / float(error_count)))
    )


def collect_register_children(registers):
    "reads the registers hierarchy"
    for register_info in registers:
        if register_info.get("spec") and register_info["spec"]["level"] > 1:
            collect_children = False
            children_o2m = []
            children_m2o = []
            level = register_info["spec"]["level"]
            for r in registers:
                if r == register_info:
                    collect_children = True
                    continue
                if collect_children:
                    if r.get("spec") and r["spec"]["level"] == level + 1:
                        if "1:1" in r["spec"]["card"] or "1;1" in r["spec"]["card"]:
                            children_m2o.append(r)
                        else:
                            children_o2m.append(r)
                            child_specs = list(
                                filter(
                                    lambda x: x["code"] == r["spec"]["code"], registers
                                )
                            )
                            if child_specs:
                                child_specs[0]["parent"] = register_info
                    elif r.get("spec") and r["spec"]["level"] <= level:
                        break
            register_info["children_o2m"] = children_o2m
            register_info["children_m2o"] = children_m2o
            if PRINT_HIERARCHY:
                if children_o2m:
                    print("  " * level + "children o2m:")
                    for c in children_o2m:
                        print("  " * level + "  " + c["code"])
                if children_m2o:
                    print("  " * level + "children m2o:")
                    for c in children_m2o:
                        print("  " * level + "  " + c["code"])


def generate_model(options, module_name):
    "entry point to generate all models and views"
    print("\n\n***** GENERATING CODE FOR ", module_name)
    models_file_name = "../models/{}.py".format(module_name)
    views_file_name = "../views/{}.xml".format(module_name)

    if (os.path.exists(models_file_name)) and not options.force:
        sys.stderr.write("\nfiles exist already.  " "use -f/--force to overwrite.\n\n")
        sys.exit(1)
    models_writer = Writer(models_file_name)
    views_writer = Writer(views_file_name)
    security_writer = Writer("../security/{}".format("ir.model.access.csv"), mode="a")

    wrtmodels = models_writer.write
    wrtviews = views_writer.write
    wrtsecurity = security_writer.write

    wrtmodels("# -*- coding: utf-8 -*-\n\n")
    wrtmodels("from odoo import models, fields\n\n")
    wrtmodels("from . import spec_models\n\n")

    wrtviews('<?xml version="1.0" encoding="UTF-8"?>\n<odoo>')
    wrtviews('\n    <menuitem name="SPED" id="menu_root" sequence="115"/>')
    wrtviews(
        ('\n    <menuitem name="%s"' ' parent="menu_root" id="%s" sequence="2" />')
        % (module_name.upper(), module_name.lower())
    )

    last_bloco = None
    registers = []
    # collect registers
    registers_spec = extract_registers_spec(module_name)

    r_spec_l = {r["code"] for r in registers_spec}
    actual_registers = r_spec_l

    registers_lib = None
    try:
        registers_lib = Escrituracao(module_name, 2017)._registros
        sorted_registers_lib = sorted(dir(registers_lib), key=natural_keys)
        r_lib_l = {
            name[8:12]
            for name in sorted_registers_lib
            if "Registro" in name and name != "Registro"
        }
        actual_registers = r_lib_l
        print("registers not found in pdf: %s" % (list(r_lib_l - r_spec_l,)))
        print("registers not found in python-sped: %s" % (list(r_spec_l - r_lib_l,)))

    except:
        print("\nWARNING python-sped lib for {} cannot be loaded!".format(module_name))
        print("so there will be no checking against the python-sped layout!\n")

    for register_name in sorted(actual_registers, key=register_keys):
        # skip opening and ending registers:
        if register_name[1:4] == "001" or register_name[1:4] == "990":
            continue
        register_specs = list(
            filter(lambda r: r["code"] == register_name, registers_spec)
        )
        register_spec = register_specs and register_specs[0] or None
        headers, rows = extract_fields_spec(module_name, register_name)

        registers.append(
            {
                "code": register_name,
                "spec": register_spec,
                "spec_fields": rows,
                "children_o2m": [],
                "children_m2o": [],
            }
        )

    if registers_lib != None:
        compare_register_fields(module_name, registers)
    collect_register_children(registers)

    # generate models
    for register_info in registers:
        spec_fields = register_info["spec_fields"]
        if len(spec_fields) < 1:
            # TODO check errors. Then skip if no field?
            print(
                "NO FIELD FOUND IN REGISTER {}, SKIPPING IT".format(
                    register_info["code"]
                )
            )
        register_name = register_info["code"]
        register_specs = list(
            filter(lambda r: r["code"] == register_name, registers_spec)
        )
        if len(register_specs) == 0:
            print("SKIPPING REG {} AS NO (PDF) SPEC FOUND".format(register_name))
            continue
        register_spec = register_specs and register_specs[0] or None
        wrtmodels("\nclass Registro{}(models.Model):\n".format(register_name))
        wrtmodels(
            "    _name = 'l10n.br.sped.%s.%s'\n"
            % (module_name.lower(), register_name.lower(),)
        )
        wrtmodels(
            '    _description = u"""{}"""\n'.format(
                register_spec["desc"] or register_name
            )
        )
        wrtmodels("    _inherit = 'l10n.br.sped.mixin'\n")

        wrtsecurity(
            "access_%s_%s,%s.%s,model_%s_%s_%s,base.group_user,1,1,1,1\n"
            % (
                module_name.lower(),
                register_name.lower(),
                module_name.lower(),
                register_name.lower(),
                "l10n_br_sped",
                module_name.lower(),
                register_name.lower().replace(".", "_"),
            )
        )

        bloco_char = register_name[0]
        if bloco_char != last_bloco:
            # TODO put back bloco desc in menuitem name after extracting it
            wrtviews(
                ('\n\n    <menuitem name="Bloco %s"' ' parent="%s" id="%s_%s"/>')
                % (bloco_char, module_name.lower(), module_name, bloco_char.lower())
            )
        last_bloco = bloco_char

        #        for field in obj.campos:
        for spec in spec_fields:
            name, label, help_msg = get_name_label_help(spec)

            if spec["type"] == "D":
                if spec.get("required", False):
                    wrtmodels(
                        '    {} = fields.Date("{}", required=True)\n'.format(
                            name, label
                        )
                    )
                else:
                    wrtmodels('    {} = fields.Date("{}")\n'.format(name, label))
            elif spec.get("type") == "N" or name.startswith(
                "vl_"
            ):  # TODO use spec_type info too
                if spec.get("required", False):
                    if spec.get("digits"):
                        wrtmodels(
                            '    %s = fields.Monetary("%s", required=True, digits=%s)\n'
                            % (name, label, spec.get("digits"))
                        )
                    else:  # if spec.get('int_size'):
                        wrtmodels(
                            '    %s = fields.Integer("%s", required=True)\n'
                            % (name, label)
                        )  # TODO or Char with Select sometimes?
                else:
                    if spec.get("digits"):
                        wrtmodels(
                            '    %s = fields.Monetary("%s", digits=%s)\n'
                            % (name, label, spec.get("digits"))
                        )
                    else:  # spec.get('int_size'):
                        wrtmodels(
                            '    {} = fields.Integer("{}")\n'.format(name, label)
                        )  # TODO or Char with Select sometimes?
            else:
                if name == "":
                    name = "reg_av"
                    label = "REG_AV"  # FIXME ECF Registro9100 undefined field; brittle
                if spec.get("required", False):
                    wrtmodels(
                        '    %s = fields.Char("%s", '
                        "required=True,"
                        '\n        help="""%s""")\n' % (name, label, help_msg)
                    )
                else:
                    wrtmodels(
                        '    %s = fields.Char("%s",'
                        '\n        help="""%s""")\n' % (name, label, help_msg)
                    )
            # TODO Bolean fields, if values are [S;N], see python-sped
        if register_info.get("parent"):
            name = register_info["parent"]["spec"]["code"].lower()
            label = register_info["parent"]["spec"]["desc"]
            label = label.strip().splitlines()[0]
            wrtmodels(
                "    parent_%s_id = fields.Many2one('l10n.br.sped.%s.%s',\n\
                                     string=\"%s\")\n"
                % (name, module_name.lower(), name, label)
            )

        for child in register_info["children_m2o"]:
            name = child["spec"]["code"].lower()
            # TODO if label is not short move to help
            label = child["spec"]["desc"].strip()
            label = label.strip().splitlines()[0]
            help = "Bloco {}".format(child["spec"]["code"][0])
            wrtmodels(
                "    reg_%s_id = fields.Many2one('l10n.br.sped.%s.%s',\n\
                              string=\"%s\",\n\
                              help='%s') # m2o\n"
                % (name, module_name.lower(), name, label, help)
            )
        for child in register_info["children_o2m"]:
            name = child["spec"]["code"].lower()
            # TODO if label is not short move to help
            label = (child["spec"]["desc"]).strip()
            label = label.strip().splitlines()[0]
            help = "Bloco {}".format(child["spec"]["code"][0])
            wrtmodels(
                "    reg_%s_ids = fields.One2many('l10n.br.sped.%s.%s',"
                "'parent_%s_id',\n\
                               string=\"%s\",\n\
                               help='%s')\n"
                % (name, module_name.lower(), name, register_name.lower(), label, help)
            )

        if register_info["spec"].get("level") in [0, 1, 2]:  # , "3"]:
            action_name = strip_desc(register_info["spec"]["desc"])
            action = """\n
    <record id='%s_%s_action' model='ir.actions.act_window'>
        <field name="name">%s</field>
        <field name="res_model">l10n.br.sped.%s.%s</field>
        <field name="view_type">form</field>
        <field name="view_mode">tree,form</field>
    </record>""" % (
                module_name,
                register_name.lower(),
                action_name,
                module_name.lower(),
                register_name.lower(),
            )
            wrtviews(action)
            wrtviews(
                ('\n    <menuitem action="%s_%s_action"' ' parent="%s_%s" id="%s_%s"/>')
                % (
                    module_name,
                    register_name.lower(),
                    module_name,
                    bloco_char.lower(),
                    module_name,
                    register_name.lower(),
                )
            )

    wrtviews("\n</odoo>")
    models_writer.close()
    views_writer.close()


def get_name_label_help(field):
    name = unidecode(field["code"]).encode("ascii").decode("utf8")

    name = name.replace(" ", "_").replace("-", "_").replace(";", "").replace("*", "")
    if len(field["desc"]) < 40:
        label = field["desc"]
    else:
        label = field["desc"].split(".")[0]
        if len(label.split(":")[0]) > 15:
            label = label.split(":")[0]
        if len(label) > 64:
            label = name
    label = label.replace('"', "'")
    if field.get("conditional_required"):
        label += "*"
    # TODO help. Also put the pdf page in the help
    help_msg = "{}\nVer pagina {}".format(field["desc"], field["page"])
    #    help_msg = help_msg.replace('"', "'")
    return name.lower(), label, help_msg


def strip_desc(desc):
    desc = desc.strip().splitlines()[0]
    if len(desc) > 64:
        s = desc.split("(")
        if len(s) > 1 and len(s[0]) < 64:
            return s[0]
        s = desc.split("-")
        if len(s) > 30 and len(s[0]) < 64:
            return s[0]
        s = desc.split(",")
        if len(s) > 30 and len(s[0]) < 64:
            return "{},...".format(s[0])
        s = desc.split(" ")
        desc2 = ""
        for w in s:
            if len(desc2) + len(w) < 61:
                desc2 = "{} {}".format(desc2, w)
            else:
                break
        return "{}...".format(desc2)
    else:
        return desc


USAGE_TEXT = __doc__


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(
            args, "hfs:", ["help", "force", "no-class-suffixes",]
        )
    except:
        usage()
    options = ProgramOptions()
    options.force = False
    options.class_suffixes = False
    for opt, val in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-f", "--force"):
            options.force = True
        elif opt == "--no-class-suffixes":
            options.class_suffixes = False
    generate_model(options, "ecd")
    generate_model(options, "ecf")
    generate_model(options, "efd_icms_ipi")
    generate_model(options, "efd_pis_cofins")
    # generate_model(options, 'fci')


if __name__ == "__main__":
    main()

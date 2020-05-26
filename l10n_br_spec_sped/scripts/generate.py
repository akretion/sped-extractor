#!/usr/bin/env python3

# Copyright 2017-2018 Akretion LTDA (http://www.akretion.com)
# @author Raphael Valyi (rvalyi@akretion.com.br)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


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


import sys
import os
from os import walk
import getopt
import csv
import re
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
    def __init__(self, outfilename, stdout_also=False, mode='w'):
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
        count = content.count('\n')
        self.line_count += count

    def close(self):
        self.outfile.close()


def normalize_field_code(code):
    # TODO lookup table for manual name patches
    # TODO return original_name attr if need to remove accents
    return (code.replace('  ', ' ').replace('__', '_').replace(' _', '_')
            ).replace('_ ', '_').replace(' ', '_').replace('\r', '')
    # .replace('ÇÃO', 'CAO')


def row_patches():
    """for rows that were not extracted properly in the csv with camelot,
    we manually maintain e dictionary of proper rows. The key is formed with
    the module-the register-the field index.
    The field description is not required if the csv has it properly.
    """
    return {
        'ecf-Y671-8': [
            '8', 'VL_INC_FIN', None,
            "N", "19", "2", "-", "Não"],
        'ecf-0020-33': [
            '33', 'IND_DEREX', """Declaração sobre utilização dos recursos"""
            """em moeda estrangeira decorrentes do recebimento
de exportações (DEREX)
S – Sim
N – Não""", "C","1","-","[S;N]","Sim"],
        'efd_icms_ipi-1391-11': [
            '11', 'SAÍDAS', None, "N", "-", "02", "OC"],
        'efd_pis_cofins-0120-02': [
            "02",  "MES_REFER",  "Mês de referência do ano-calendário da"
            "escrituração  sem dados, dispensada da entrega. "
            "Campo a ser preenchido no formato “mmaaaa”",
            "C", "006*", "-", "S"],
    }


def infer_field_type(name, spec_type, row):
    # TODO use more and refine with values (Boolean) + Monetary/Dec
    if name.startswith('DT_') or name.startswith('DATA_'):
        return 'D'
    elif spec_type == 'D':  # Date
        return 'D'
    elif spec_type and 'N' in spec_type:  # Numeric
        return 'N'
    elif spec_type == 'C':  # Char
        return 'C'
    else:
        for i in row[1:len(row) - 1]:
            if i.isdigit() and int(i) > 16: # char size assumed
                return 'C'
        return None


def map_field_row(mod, page, register, row, headers, in_out):
    "extracts field information from its row in the csv file"
    # TODO extract possible values (valores)
    # TODO extract rules to mention them (to suggest overrides)
    v = {'index': int(row[0].replace('*', '0')),  # TODO check * cases
         'code': normalize_field_code(row[1]),
         'page': page,
         'desc': row[2]
         }

    # past this point, iteration is required to find the field type
    # while dealing with pissible blank columns.
    items = iter(row[3:50])
    index = 2
    for item in items:
        if item in ('C', 'N', 'NS', 'N’', 'D'):  # all known types
            v['spec_type'] = item  # keep original value for reference
            if item == 'D':  # Date
                v['type'] = 'D'
            elif 'N' in item:  # Numeric
                v['type'] = 'N'
            else:  # Char
                v['type'] = 'C'
            try:
                while True:  # hunt for size, digits, values and required
                    i = next(items)
                    index += 1
                    if i.replace("*", "").isdigit():
                        if v['type'] == 'N':
                            if v.get('int_size'):
                                # TODO can it be Decimal with no int_size?
                                # -> yes it can!! TODO
                                v['digits'] = int(i.replace("*", ""))
                            else:
                                v['int_size'] = int(i.replace("*", ""))
                        else:
                            v['length'] = i
                    if i in ['O', 'S', 'Sim', 'OC']:
                        if not in_out:
                            # O "OC" significa que o campo deve ser preenchido
                            # sempre que houver a informação.
                            if i == 'OC':
                                v['conditional_required'] = True
                            else:
                                v['required'] = True
                            break
                        else:  # in and out case:
                            j = next(items)
                            if j in ['O', 'S', 'Sim', 'OC']:
                                if i == 'OC':
                                    v['conditional_required_in'] = True
                                if j == 'OC':
                                    v['conditional_required_out'] = True
                                else:
                                    v['required'] = True
                                break
                            # TODO deal with in not required and out required
            except StopIteration:
                break
            break
        elif item != '':
            pass
            # TODO print and ensure all cases are dealt with (some
            # are properly dealt when type is discovered later, but check)
#            row[2] = 'desc (skipped here)'
#            print("BBBBBBBBBBBBBB", row)
    if not v.get('type'):
        f_type = infer_field_type(v['code'], None, row)
        if f_type is not None:
            v['type'] = f_type
    show_problematic_field_rows(row, page, v)
    return v


def show_problematic_field_rows(row, page, v):
    if not v.get('type') or v['type'] is None:
        row[2] = 'desc (skipped here)'
        print("page %s, field type cannot be resolved:" % (page,), row)


def is_register_row(row):
    if len(row) > 5 and (row[1].replace(' ', '') == "REG" or
                         row[2].replace(' ', '') == "REG" or
                         " REG" in row[0]):
        return True
    return False


def is_register_header_match(register_name, row):
    if register_name in "".join(row) and "Texto" in "".join(row):
        return True
    return False


def is_field_row_start(row, last_field_index, register):
    if len(row) > 4 and row[1].upper() == row[1] and row[1] != ''\
            and len(row[1]) < 32\
            and len(row[1]) > 1\
            and not row[1][0].isdigit()\
            and (row[0].isdigit() and row[1].replace(' ','') != "REG"\
                 and int(row[0]) == last_field_index + 1\
                 or row[0] == '*'):
        return True
#    if row[0].isdigit() and int(row[0]) == last_field_index + 2:
#        print("WARNING FIELD LIKELY MISSED FROM %s, %s to %s" % (register,
#                                                                 last_field_index,
#                                                                 row[0]))
    return False


def is_field_row(mod, register, row, last_field_index):
    if 'RZ_CONT' in row[1]:  # ECD, doesn't look like a real data field
        return False, row
    patch = row_patches().get("%s-%s-%s" % (mod, register, row[0]))
    if not patch:  # in case 1st is a blank before position
        patch = row_patches().get("%s-%s-%s" % (mod, register, row[1][0:2]))
    if patch:
        print("PATCHING ROW:", register, patch)
        if patch[2] is None:  # assuming descr was correct
            patch[2] = row[2]
        row = patch
        return True, row
    else:
        if len(row) > 5 and row[0] == '':  # sometimes 1st is a blank
            row.pop(0)
        if mod == 'efd_pis_cofins' and len(row) > 4 and\
                row[0][0:2].isdigit() and len(row[0]) > 6:
            split = row[0].split(' ')
            row = [row[0][0:2], split[len(split) - 1]] + row[2:len(row) - 1]
        test = is_field_row_start(row, last_field_index, register)
        return test, row


def extract_fields_spec(mod, register_name):
    """scans the csv files to find the rows describing the fields
    of a given register."""
    # TODO map back into register: required, in_required, out_required
    path = "../specs/%s" % (mod,)
    files = []
    in_register = False
    header = False
    header_candidate = False
    reg_line = None
    cols = 0
    values_col = None
    rule_col = None
    last_row = None
    last_field_index = 1
    rows = []
    in_out = None
    in_required = False
    out_required = False

    for (dirpath, dirnames, filenames) in walk(path):
        files = sorted(filenames, key=natural_keys)
    for csv_file in files:
        page = int(csv_file.split('-')[2])
        if register_name == "I510" and csv_file == "ecd-page-20-table-1.csv":
            continue # seems like a false positive, real table is later
        with open("../specs/%s/%s" % (mod, csv_file), 'rU') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                if not in_register and is_register_row(row)\
                        and is_register_header_match(register_name, row):
                    in_register = True
                    header = header_candidate

                    c = 0
                    for x in header:
                        if 'Regras' in x:
                            rule_col = c
                        c += 1

                    reg_line = row  # the line with the 'REG' field
                    cols = len(header)
                    if register_name in row[cols - 2]\
                            or register_name in ['Y681']:  # ECF error
                        in_out = False  # because only 1 col left
                        values_col = cols - 2
                    elif register_name in row[cols - 3]:
                        values_col = cols - 3
                        if row[cols - 1] == row[cols - 2] == 'O':
                            in_out = True
                            in_required = True
                            out_required = True
                        elif rule_col is None or rule_col < values_col:
                            in_out = True # but it never happens
                        else:
                            in_out = False
                    else:
                        if row[cols - 1] == row[cols - 2] == 'O':
                            in_out = True
                            in_required = True
                            out_required = True
                        if len(header) == 8 and 'Entr' in header[6]:
                            in_out = True
                            if row[cols - 2] == 'O':
                                in_required = True
                            else:
                                in_required = False
                            if row[cols - 1] == 'O':
                                out_required = True
                            else:
                                out_required = False
                        else:
                            in_out = False
                    if in_out is True and\
                            in_required is None or out_required is None:
                        print("ERROR", header, row)
                    continue
                if in_register:
                    if ''.join(row) == '' or len(row) < 4:
                        continue # empty line
                    elif is_register_row(row)\
                             and not is_register_header_match(register_name, row):
                        # next register table found -> stopping
                        return header, rows
                    test, row = is_field_row(mod, register_name, row,
                                             last_field_index)
                    if test:
                        v = map_field_row(mod, page, register_name,
                                          row, header, in_out)
                        last_field_index = v['index']
                        rows.append(v)
                        last_row = row
                elif "".join(row) != '':
                    header_candidate = row
    return header, rows


def compare_register_fields(module_name, registers):
    "compares register_fields found scanning the PDF with python-sped when possible"
    registers_lib = Escrituracao(module_name, 2017)._registros
    error_count = 0
    field_count = 0
    for register_info in registers:
        register_name = register_info['code']
        register_lib = getattr(registers_lib, 'Registro%s' % (register_name,))
        lib_fields = [f.nome for f in register_lib.campos
                      if f.nome != 'REG']
        # TODO move field extraction outside from method?
        headers, rows = extract_fields_spec(module_name, register_name)
        register_info['spec_fields'] = rows
        spec_fields = [f['code'] for f in rows]
        extra_spec = list(set(spec_fields) - set(lib_fields))
        extra_lib = list(set(lib_fields) - set(spec_fields))
        if len(extra_spec) > 0 or len(extra_lib) > 0:
            print("\n%s" % (register_name,))
            if len(extra_lib) > 0:
                print("     missing in pdf: %s" % (extra_lib))
            if len(extra_spec) > 0:
                print("     missing in python-sped: %s" % (extra_spec))
            error_count += len(extra_spec) + len(extra_lib)
        field_count += len(lib_fields)
        # TODO also report field types error (very likely inside python-sped)
    print("\n %s field errors out of %s\
          fields (%s percent)" % (error_count, field_count,
                                  100.0/( field_count / float(error_count))))

def collect_register_children(registers):
    "reads the registers hierarchy"
    for register_info in registers:
        if register_info.get('spec') and register_info['spec']['level'] > 1:
            collect_children = False
            children_o2m = []
            children_m2o = []
            level = register_info['spec']['level']
            for r in registers:
                if r == register_info:
                    collect_children = True
                    continue
                if collect_children:
                    if r.get('spec') and r['spec']['level'] == level + 1:
                        if '1:1' in r['spec']['card']\
                                or '1;1' in r['spec']['card']:
                            children_m2o.append(r)
                        else:
                            children_o2m.append(r)
                            child_specs = list(filter(lambda x: x['code'] == r['spec']['code'], registers))
                            if child_specs:
                                child_specs[0]['parent'] = register_info
                    elif r.get('spec') and r['spec']['level'] <= level:
                        break
            register_info['children_o2m'] = children_o2m
            register_info['children_m2o'] = children_m2o
            if PRINT_HIERARCHY:
                if children_o2m:
                    print("  "*level + 'children o2m:')
                    for c in children_o2m:
                        print("  "*level + "  " + c['code'])
                if children_m2o:
                    print("  "*level + 'children m2o:')
                    for c in children_m2o:
                        print("  "*level + "  " + c['code'])


def generate_model(options, module_name):
    "entry point to generate all models and views"
    print("\n\n***** GENERATING CODE FOR ", module_name)
    models_file_name = "../models/%s.py" % (module_name,)
    views_file_name = "../views/%s.xml" % (module_name,)

    if (
            (os.path.exists(models_file_name)
            ) and
            not options.force):
        sys.stderr.write(
            '\nfiles exist already.  '
            'use -f/--force to overwrite.\n\n')
        sys.exit(1)
    models_writer = Writer(models_file_name)
    views_writer = Writer(views_file_name)
    security_writer = Writer("../security/%s" % (
                             'ir.model.access.csv',), mode='a')

    wrtmodels = models_writer.write
    wrtviews = views_writer.write
    wrtsecurity = security_writer.write

    wrtmodels("# -*- coding: utf-8 -*-\n\n")
    wrtmodels("from odoo import models, fields\n\n")
    wrtmodels("from . import spec_models\n\n")

    wrtviews('<?xml version="1.0" encoding="UTF-8"?>\n<odoo>')
    wrtviews('\n    <menuitem name="SPED" id="menu_root" sequence="115"/>')
    wrtviews(('\n    <menuitem name="%s"'
              ' parent="menu_root" id="%s" sequence="2" />'
             ) % (module_name.upper(), module_name.lower()))

    last_bloco = None
    registers = []
    #collect registers
    registers_spec = extract_registers_spec(module_name)

    r_spec_l = set(r['code'] for r in registers_spec)
    actual_registers = r_spec_l

    registers_lib = None
    try:
        registers_lib = Escrituracao(module_name, 2017)._registros
        sorted_registers_lib = sorted(dir(registers_lib), key=natural_keys)
        r_lib_l = set([name[8:12] for name in sorted_registers_lib
                      if 'Registro' in name and name != 'Registro'])
        actual_registers = r_lib_l
        print("registers not found in pdf: %s" % (list(r_lib_l - r_spec_l,)))
        print("registers not found in python-sped: %s" % (list(r_spec_l - r_lib_l,)))

    except:
        print("\nWARNING python-sped lib for %s cannot be loaded!" % (module_name,))
        print("so there will be no checking against the python-sped layout!\n")

    for register_name in sorted(actual_registers, key=register_keys):
        # skip opening and ending registers:
        if register_name[1:4] == '001' or register_name[1:4] == '990':
            continue
        register_specs = list(filter(lambda r: r['code'] == register_name,
                              registers_spec))
        register_spec = register_specs and register_specs[0] or None
        headers, rows = extract_fields_spec(module_name, register_name)

        registers.append({
                          'code': register_name,
                          'spec': register_spec,
                          'spec_fields': rows,
                          'children_o2m': [],
                          'children_m2o': [],
                         })

    if registers_lib != None:
        compare_register_fields(module_name, registers)
    collect_register_children(registers)

    # generate models
    for register_info in registers:
        spec_fields = register_info['spec_fields']
        if len(spec_fields) < 1:
            # TODO check errors. Then skip if no field?
            print("NO FIELD FOUND IN REGISTER %s, SKIPPING IT" % (
                register_info['code'],))
        register_name = register_info['code']
        register_specs = list(filter(lambda r: r['code'] == register_name,
                                registers_spec))
        if len(register_specs) == 0:
            print("SKIPPING REG %s AS NO (PDF) SPEC FOUND" % (register_name,))
            continue
        register_spec = register_specs and register_specs[0] or None
        wrtmodels('\nclass Registro%s(models.Model):\n' % (register_name,))
        wrtmodels("    _name = 'l10n.br.sped.%s.%s'\n" % (
            module_name.lower(), register_name.lower(),))
        wrtmodels('    _description = u"""%s"""\n' % (
            register_spec['desc'] or register_name,))
        wrtmodels("    _inherit = 'l10n.br.sped.mixin'\n")

        wrtsecurity("access_%s_%s,%s.%s,model_%s_%s_%s,base.group_user,1,1,1,1\n" % (
            module_name.lower(), register_name.lower(),
            module_name.lower(), register_name.lower(),
            'l10n_br_sped', module_name.lower(),
            register_name.lower().replace('.', '_')))



        bloco_char = register_name[0]
        if bloco_char != last_bloco:
            # TODO put back bloco desc in menuitem name after extracting it
            wrtviews(('\n\n    <menuitem name="Bloco %s"'
                        ' parent="%s" id="%s_%s"/>'
                        ) % (bloco_char,
                            module_name.lower(),
                            module_name,
                            bloco_char.lower()))
        last_bloco = bloco_char

#        for field in obj.campos:
        for spec in spec_fields:
            name, label, help_msg = get_name_label_help(spec)

            if spec['type'] == 'D':
                if spec.get('required', False):
                    wrtmodels("    %s = fields.Date(\"%s\", required=True)\n" % (name, label))
                else:
                    wrtmodels("    %s = fields.Date(\"%s\")\n" % (name, label))
            elif spec.get('type') == 'N'\
                    or name.startswith('vl_'):  # TODO use spec_type info too
                if spec.get('required', False):
                    if spec.get('digits'):
                        wrtmodels("    %s = fields.Monetary(\"%s\", required=True, digits=%s)\n" % (name, label, spec.get('digits')))
                    else: # if spec.get('int_size'):
                        wrtmodels("    %s = fields.Integer(\"%s\", required=True)\n" % (name, label)) # TODO or Char with Select sometimes?
                else:
                    if spec.get('digits'):
                        wrtmodels("    %s = fields.Monetary(\"%s\", digits=%s)\n" % (name, label, spec.get('digits')))
                    else: # spec.get('int_size'):
                        wrtmodels("    %s = fields.Integer(\"%s\")\n" % (
                            name, label)) # TODO or Char with Select sometimes?
            else:
                if name == '':
                    name = "reg_av"
                    label = 'REG_AV' # FIXME ECF Registro9100 undefined field; brittle
                if spec.get('required', False):
                    wrtmodels("    %s = fields.Char(\"%s\", "
                              "required=True,"
                              "\n        help=\"\"\"%s\"\"\")\n" % (
                                  name, label, help_msg))
                else:
                    wrtmodels("    %s = fields.Char(\"%s\","
                              "\n        help=\"\"\"%s\"\"\")\n" % (
                                  name, label, help_msg))
            # TODO Bolean fields, if values are [S;N], see python-sped
        if register_info.get('parent'):
            name = register_info['parent']['spec']['code'].lower()
            label = register_info['parent']['spec']['desc']
            label = label.strip().splitlines()[0]
            wrtmodels("    parent_%s_id = fields.Many2one('l10n.br.sped.%s.%s',\n\
                                     string=\"%s\")\n" % (name,
                                                        module_name.lower(),
                                                        name, label))

        for child in register_info['children_m2o']:
            name = child['spec']['code'].lower()
            # TODO if label is not short move to help
            label = child['spec']['desc'].strip()
            label = label.strip().splitlines()[0]
            help = "Bloco %s" % (child['spec']['code'][0],)
            wrtmodels("    reg_%s_id = fields.Many2one('l10n.br.sped.%s.%s',\n\
                              string=\"%s\",\n\
                              help='%s') # m2o\n" % (name, module_name.lower(),
                                                     name, label, help))
        for child in register_info['children_o2m']:
            name = child['spec']['code'].lower()
            # TODO if label is not short move to help
            label = (child['spec']['desc']).strip()
            label = label.strip().splitlines()[0]
            help = "Bloco %s" % (child['spec']['code'][0],)
            wrtmodels("    reg_%s_ids = fields.One2many('l10n.br.sped.%s.%s',"
                      "'parent_%s_id',\n\
                               string=\"%s\",\n\
                               help='%s')\n" % (name,
                                                module_name.lower(),
                                                name,
                                                register_name.lower(),
                                                label, help))

        if register_info['spec'].get('level') in [0, 1, 2]:#, "3"]:
            action_name = strip_desc(register_info['spec']['desc'])
            action = """\n
    <record id='%s_%s_action' model='ir.actions.act_window'>
        <field name="name">%s</field>
        <field name="res_model">l10n.br.sped.%s.%s</field>
        <field name="view_type">form</field>
        <field name="view_mode">tree,form</field>
    </record>""" % (module_name,
                    register_name.lower(),
                    action_name,
                    module_name.lower(),
                    register_name.lower())
            wrtviews(action)
            wrtviews(('\n    <menuitem action="%s_%s_action"'
                        ' parent="%s_%s" id="%s_%s"/>') % (
                            module_name,
                            register_name.lower(),
                            module_name,
                            bloco_char.lower(),
                            module_name,
                            register_name.lower(),
                        ))

    wrtviews("\n</odoo>")
    models_writer.close()
    views_writer.close()


def get_name_label_help(field):
    name = unidecode(field['code']).encode('ascii').decode('utf8')

    name = name.replace(' ', '_').replace('-', '_').replace(';', '').replace("*", "")
    if len(field['desc']) < 40:
        label = field['desc']
    else:
        label = field['desc'].split(".")[0]
        if len(label.split(":")[0]) > 15:
            label = label.split(":")[0]
        if len(label) > 64:
            label = name
    label = label.replace('"', "'")
    if field.get('conditional_required'):
        label += "*"
    # TODO help. Also put the pdf page in the help
    help_msg = "%s\nVer pagina %s" % (field['desc'], field['page'])
#    help_msg = help_msg.replace('"', "'")
    return name.lower(), label, help_msg


def strip_desc(desc):
    desc = desc.strip().splitlines()[0]
    if len(desc) > 64:
        s = desc.split('(')
        if len(s) > 1 and len(s[0]) < 64:
            return s[0]
        s = desc.split('-')
        if len(s) > 30 and len(s[0]) < 64:
            return s[0]
        s = desc.split(',')
        if len(s) > 30 and len(s[0]) < 64:
            return "%s,..." % (s[0],)
        s = desc.split(" ")
        desc2 = ""
        for w in s:
            if len(desc2) + len(w) < 61:
                desc2 = "%s %s" % (desc2, w)
            else:
                break
        return "%s..." % (desc2,)
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
            args, 'hfs:', [
                'help', 'force',
                'no-class-suffixes', ])
    except:
        usage()
    options = ProgramOptions()
    options.force = False
    options.class_suffixes = False
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-f', '--force'):
            options.force = True
        elif opt == '--no-class-suffixes':
            options.class_suffixes = False
    generate_model(options, 'ecd')
    generate_model(options, 'ecf')
    generate_model(options, 'efd_icms_ipi')
    generate_model(options, 'efd_pis_cofins')
    # generate_model(options, 'fci')


if __name__ == '__main__':
    main()

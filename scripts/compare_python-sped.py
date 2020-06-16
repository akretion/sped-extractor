#!/usr/bin/env python3

import logging

import click
from build_csv import get_fields, get_registers
from sped.efd.icms_ipi import registros as efd_icms_ipi_registers
from sped.efd.pis_cofins import registros as efd_pis_cofins_registers
from sped.escrituracao import Escrituracao

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _get_python_sped_reg_and_fields(mod):
    """ Return 2 objects :
    `reg_classes`, a dictionary with python-sped module's registers looking like :
        {
            'F990': <class 'sped.efd.pis_cofins.registros.RegistroF990'>,
            'I001': <class 'sped.efd.pis_cofins.registros.RegistroI001'>,
            'I010': <class 'sped.efd.pis_cofins.registros.RegistroI010'>,
            ...
        }
    and `fields` a list of dictionaries with python-sped module's fields looking like :
        [
            {"register": "F990", "index": 2, "code": "FORMA_APUR_I"},
            {"register": "F990", "index": 3, "code": "IND_ALIQ_CSLL"},
            ...
        ]
    """
    reg_module = {}
    reg_classes = {}
    fields = []

    try:
        # Catch registers defined from 2017 python-sped leiaute
        # (only available for ECD and ECF modules)
        reg_module = Escrituracao(mod, 2017)._registros
    except FileNotFoundError:
        # Catch registers for EFD_ICMS_IPI and EFD_PIS_COFINS modules
        if mod == "efd_icms_ipi":
            reg_module = efd_icms_ipi_registers
        elif mod == "efd_pis_cofins":
            reg_module = efd_pis_cofins_registers

    for name, object in reg_module.__dict__.items():
        if (
            isinstance(object, type)
            and getattr(object, "campos", False)
            and name != "Registro"  # Avoid "Registro" abstract class
        ):
            # Build a reg_classes dict with keys like "M630"
            # taken from registers class names like "RegistroM630"
            reg_classes[name[8:12]] = object

    for reg_name, reg_class in reg_classes.items():
        for field in reg_class.campos:
            if field.nome != "REG":
                fields.append(
                    {"register": reg_name, "index": field.indice, "code": field.nome}
                )

    return reg_classes, fields


def _compare_registers(mod, pysped_registers):
    ext_registers = get_registers(mod)
    ext_reg_codes = [reg["code"] for reg in ext_registers]

    not_in_pysped = [c for c in ext_reg_codes if c not in pysped_registers]
    logger.info("    Not in python-sped : {}".format(not_in_pysped))

    not_in_extractor = [c for c in pysped_registers if c not in ext_reg_codes]
    logger.info("    Not in sped_extractor : {}".format(not_in_extractor))

    common_reg = [c for c in ext_reg_codes if c in pysped_registers]
    return common_reg


def _compare_fields(mod, common_reg, pysped_fields):
    ext_fields = get_fields(mod)
    not_in_pysped = {}
    not_in_extractor = {}

    for reg in common_reg:
        ext_fields_reg = [f["code"] for f in ext_fields if f["register"] == reg]
        psped_fields_reg = [f["code"] for f in pysped_fields if f["register"] == reg]

        not_in_pysped[reg] = [c for c in ext_fields_reg if c not in psped_fields_reg]
        not_in_extractor[reg] = [c for c in psped_fields_reg if c not in ext_fields_reg]

    logger.info("  Not in python-sped :")
    fields_nb = 0
    reg_nb = 0
    for reg, fields in not_in_pysped.items():
        if fields:
            logger.info("    {} : {}".format(reg, fields))
            fields_nb += len(fields)
            reg_nb += 1
    logger.info("  >> {} missing fields in {} registers\n".format(fields_nb, reg_nb))

    logger.info("  Not in sped_extractor :")
    fields_nb = 0
    reg_nb = 0
    for reg, fields in not_in_extractor.items():
        if fields:
            logger.info("    {} : {}".format(reg, fields))
            fields_nb += len(fields)
            reg_nb += 1
    logger.info("  >> {} missing fields in {} registers\n".format(fields_nb, reg_nb))


@click.command()
def main():
    """Compare extracted registerts and fields with python-sped library."""
    for mod in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        logger.info("\nComparing {} module...".format(mod.upper()))
        logger.info("\nRegisters :")
        pysped_registers, pysped_fields = _get_python_sped_reg_and_fields(mod)
        common_reg = _compare_registers(mod, pysped_registers)
        logger.info("\nFields :")
        _compare_fields(mod, common_reg, pysped_fields)


if __name__ == "__main__":
    main()

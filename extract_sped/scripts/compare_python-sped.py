#!/usr/bin/env python3

import logging

import click
from build_csv import extract_fields, extract_registers
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
    ext_registers = extract_registers(mod)
    ext_reg_codes = [reg["code"] for reg in ext_registers]

    not_in_pysped = [c for c in ext_reg_codes if c not in pysped_registers]
    logger.info("    Not in python-sped : {}".format(not_in_pysped))

    not_in_extractor = [c for c in pysped_registers if c not in ext_reg_codes]
    logger.info("    Not in sped_extractor : {}".format(not_in_extractor))

    common_reg = [c for c in ext_reg_codes if c in pysped_registers]
    return common_reg


def _compare_fields(mod, common_reg, pysped_fields):
    ext_fields = extract_fields(mod)

    for reg in common_reg:
        ext_fields_reg = [f["code"] for f in ext_fields if f["register"] == reg]
        pysped_fields_reg = [f["code"] for f in pysped_fields if f["register"] == reg]

        not_in_pysped = [c for c in ext_fields_reg if c not in pysped_fields_reg]
        not_in_extractor = [c for c in pysped_fields_reg if c not in ext_fields_reg]

        if not_in_pysped or not_in_extractor:
            logger.info("{} :".format(reg))
        if not_in_pysped:
            logger.info("    Not in python-sped : {}".format(not_in_pysped))
        if not_in_extractor:
            logger.info("    Not in sped_extractor : {}".format(not_in_extractor))


@click.command()
def main():
    """Compare extracted registerts and fields with python-sped library."""
    for mod in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        logger.info("\n\nComparing {} module...".format(mod.upper()))
        logger.info("\nRegisters :")
        pysped_registers, pysped_fields = _get_python_sped_reg_and_fields(mod)
        common_reg = _compare_registers(mod, pysped_registers)
        logger.info("\nFields :")
        _compare_fields(mod, common_reg, pysped_fields)


if __name__ == "__main__":
    main()

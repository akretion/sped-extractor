import logging

import click
from itertools import groupby
from xsdata.models.config import GeneratorConfig
from xsdata_odoo.generator import OdooGenerator
from xsdata_odoo.generator import GeneratorResult
from xsdata.codegen.models import Attr, AttrType, Class, Restrictions
from xsdata.codegen.resolver import DependenciesResolver

from .build_csv import _is_reg_row, clean_row, get_raw_rows
from .build_csv import get_fields, get_registers, get_blocks
from .constants import MODULES, MOST_RECENT_YEAR, OLDEST_YEAR

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


@click.option(
    "--year",
    default=MOST_RECENT_YEAR,
    show_default=True,
    type=click.IntRange(OLDEST_YEAR, MOST_RECENT_YEAR),
    help="Operate on a specific year's folder, "
    f"can be between {OLDEST_YEAR} and {MOST_RECENT_YEAR}",
)
@click.command()
def main(year):
    """
    Generate Odoo models
    """
    config = GeneratorConfig()
    print("CCC", config)
    generator = OdooGenerator(config)
    print(generator)
    resolver = DependenciesResolver(packages={})
    for mod in MODULES:
        if mod != "ecd":  # FIXME
            continue
        print("********************* MOD", mod)
        classes = []
        registers = get_registers(mod, year)
        print(type(registers))
        fields = get_fields(mod, year)
        field_iterator = groupby(fields, lambda x: x["register"])
        for reg_code, group in field_iterator:
            name = "Registro%s" % (reg_code,)
            register = list(filter(lambda x: x["code"] == reg_code, registers))[0]
            attrs = []
            for field in list(group):
                types = [
                    AttrType(
                        qname="{http://www.w3.org/2001/XMLSchema}string", native=True
                    )
                ]  # TODO
                restrictions = Restrictions(
                    min_occurs=field.get("required") and 1 or 0
                )  # TODO make it work. It uses metadata in generate.py and fail
                attr = Attr(
                    tag=field["code"],
                    name=field["code"],
                    types=types,
                    restrictions=restrictions,
                    help=field["desc"],
                )
                attrs.append(attr)

            # TODO add relational fields. See parents and children in https://github.com/akretion/sped-extractor/blob/12.0/l10n_br_spec_sped/scripts/generate.py#L492

            k = Class(
                qname=name,
                tag=name,
                location="TODO",
                attrs=attrs,
                help=register["desc"],
                module=mod,
            )
            classes.append(k)
            logger.info(k)

        source = generator.render_module(resolver, classes)
        print(source)


if __name__ == "__main__":
    main()

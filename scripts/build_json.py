#!/usr/bin/env python3

import json
import logging

import click
from build_csv import get_fields

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _build_json(mod):
    # TODO : Build module's JSON with a real nested structure : Block > Register > Field
    # (with nested Registers following their own level)
    path = "../specs/{}/".format(mod)
    fields = get_fields(mod)
    with open(path + "{}_fields.json".format(mod), "w") as json_file:
        # Delete actual json_file's datas before writing
        json_file.seek(0)
        json_file.truncate()

        json.dump(fields, json_file, indent=4)


@click.command()
def main():
    """Build a JSON file with the module's fields for each module."""
    logger.info("Building JSON files for each modules...")
    for module in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        _build_json(module)
        logger.info("> {}_fields.json".format(module))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import csv
import logging
from os import walk

import click
from build_csv import _is_reg_row, clean_row, natural_keys

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _get_mod_headers(mod):
    path = "../specs/{}/raw_camelot_csv/".format(mod)
    files = []
    previous_row = False
    headers = []

    for (_dirpath, _dirnames, filenames) in walk(path):
        files = sorted(filenames, key=natural_keys)
    for csv_file in files:
        with open(path + csv_file, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in reader:
                row = clean_row(row)
                if len(row) > 2 and _is_reg_row(row) and previous_row not in headers:
                    headers.append(previous_row)
                previous_row = row
    return headers


@click.command()
def main():
    """Display a list of all the different fields headers found in the four modules.

    Used to define the modules headers hard-coded at the beginning of ./build_csv.py .
    """
    for module in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        headers = _get_mod_headers(module)
        logger.info("\n{}'s headers :".format(module.upper()))
        for header in headers:
            logger.info(header)


if __name__ == "__main__":
    main()

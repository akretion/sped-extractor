#!/usr/bin/env python3

import logging

import click
from build_csv import _get_raw_rows, _is_reg_row, clean_row
from years import MOST_RECENT_YEAR, OLDEST_YEAR

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _get_mod_headers(mod, year):
    previous_row = False
    headers = []
    raw_rows = _get_raw_rows(mod, year)

    for page in raw_rows:
        for row in raw_rows[page]:
            row = clean_row(row)
            if len(row) > 2 and _is_reg_row(row) and previous_row not in headers:
                headers.append(previous_row)
            previous_row = row
    return headers


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
    """Display a list of all the different fields headers found in the four modules.

    Used to define the modules headers hard-coded at the beginning of ./build_csv.py .
    """
    for mod in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        headers = _get_mod_headers(mod, year)
        logger.info(f"\n{mod.upper()}'s headers :")
        for header in headers:
            logger.info(header)


if __name__ == "__main__":
    main()

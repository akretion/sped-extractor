#!/usr/bin/env python3

import logging
import os
import csv

import click
import requests
from PyPDF2 import PdfFileReader
from pathlib import Path

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _get_max_min_year():
    """Return a tuplet with most recent and oldest year folder available in '../specs/'
    """
    years = [f.name for f in os.scandir("../specs/") if f.is_dir()]
    return (int(max(years, key=int)), int(min(years, key=int)))


MOST_RECENT_YEAR = _get_max_min_year()[0]
OLDEST_YEAR = _get_max_min_year()[1]


def _get_url(mod, year):
    """Return the first URL found for a module's year version"""
    with open("../specs/{}/download_info.csv".format(year), "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        header = next(reader)
        col_url = header.index("url")
        col_mod = header.index("module")
        for row in reader:
            if row[col_mod] == mod:
                return row[col_url]


def _download(mod, year):
    Path("../specs/{}/pdf".format(year)).mkdir(parents=True, exist_ok=True)
    pdf = "../specs/{}/pdf/{}.pdf".format(year, mod)
    url = _get_url(mod, year)
    try:
        r = requests.get(url)
    except requests.exceptions.MissingSchema:
        logger.warning(
            "  Cannot download {}'s pdf because '{}' is not a valid URL.".format(
                mod.upper(), url
            )
        )
        pass
    else:
        if not r or r.headers.get("content-type") != "application/pdf":
            logger.warning("  No pdf found at '{}' for {}.".format(url, mod.upper()))
        else:
            # Remove existing pdf if any
            try:
                os.remove(pdf)
            except OSError:
                pass
            # Create a new one
            with open(pdf, "wb") as f:
                f.write(r.content)


@click.command()
@click.option(
    "--year",
    default=MOST_RECENT_YEAR,
    show_default=True,
    type=int,
    help="Specify a SPED specification year between {} and {}".format(
        OLDEST_YEAR, MOST_RECENT_YEAR
    ),
)
def main(year):
    """Download SPED specifications pdf from http://sped.rfb.gov.br/"""
    assert year >= OLDEST_YEAR and year <= MOST_RECENT_YEAR, (
        f"An integer between {OLDEST_YEAR} and {MOST_RECENT_YEAR} is required "
        f"for year's option, not '{year}'"
    )

    for module in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        logger.info(f"Downloading pdf {module.upper()} {year}...")
        _download(module, year)


if __name__ == "__main__":
    main()

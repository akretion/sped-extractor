#!/usr/bin/env python3

import logging
import os
import csv

import click
import requests
from PyPDF2 import PdfFileReader

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _get_max_min_year():
    """Return a tuplet with most recent and oldest year version available in
    '../specs/download_url.csv' """
    max_year = 2020
    min_year = 2016
    with open("../specs/download_url.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        header = next(reader)
        col_year = header.index("year_version")
        for row in reader:
            year = int(row[col_year])
            if year > max_year:
                max_year = year
            if year < min_year:
                min_year = year
    return (max_year, min_year)


MOST_RECENT_YEAR = _get_max_min_year()[0]
OLDEST_YEAR = _get_max_min_year()[1]


def _get_url(mod, year_version):
    """Return the first URL found for a module's year version"""
    with open("../specs/download_url.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        header = next(reader)
        col_url = header.index("url")
        col_mod = header.index("module")
        col_year = header.index("year_version")
        for row in reader:
            if row[col_mod] == mod and row[col_year] == str(year_version):
                return row[col_url]

def _download(mod, year_version):
    pdf = "../specs/{}.pdf".format(mod)
    url = _get_url(mod, year_version)
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
    for module in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        if year < OLDEST_YEAR or year > MOST_RECENT_YEAR :
            logger.warning(
                "An integer between {} and {} is required for year's option, not '{}'.\
                ".format(
                    OLDEST_YEAR, MOST_RECENT_YEAR, year
                )
            )
            break
        else:
            logger.info("Downloading {} pdf from {}...".format(module.upper(), year))
            _download(module, year)


if __name__ == "__main__":
    main()

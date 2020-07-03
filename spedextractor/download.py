#!/usr/bin/env python3

import logging
import os
import csv

import click
import requests
from PyPDF2 import PdfFileReader
from pathlib import Path

from years import MOST_RECENT_YEAR, OLDEST_YEAR

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _get_url(mod, year):
    """Return the first URL found for a module's year version"""
    dl_info_path = f"../specs/{year}/download_info.csv"
    try:
        with open(dl_info_path, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            header = next(reader)
            col_url = header.index("url")
            col_mod = header.index("module")
            for row in reader:
                if row[col_mod] == mod:
                    return row[col_url]
    except FileNotFoundError:
        logger.exception(
            f"The file '{dl_info_path}' containing the pdf URL "
            "is required to download them."
        )


def _download(mod, year):
    Path(f"../specs/{year}/pdf").mkdir(parents=True, exist_ok=True)
    pdf = f"../specs/{year}/pdf/{mod}.pdf"
    url = _get_url(mod, year)
    try:
        r = requests.get(url)
    except requests.exceptions.MissingSchema:
        logger.exception(
            f"  Cannot download {mod.upper()}'s pdf because '{url}' is not a valid URL."
        )
        pass
    else:
        if not r or r.headers.get("content-type") != "application/pdf":
            logger.warning(f"  No pdf found at '{url}' for {mod.upper()}.")
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
    type=click.IntRange(OLDEST_YEAR, MOST_RECENT_YEAR),
    help="Operate on a specific year's folder, "
    f"can be between {OLDEST_YEAR} and {MOST_RECENT_YEAR}",
)
def main(year):
    """Download SPED specifications pdf from http://sped.rfb.gov.br/"""

    for module in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        logger.info(f"Downloading pdf {module.upper()} {year}...")
        _download(module, year)


if __name__ == "__main__":
    main()

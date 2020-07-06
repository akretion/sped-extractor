#!/usr/bin/env python3

import logging

import camelot
import click
from PyPDF2 import PdfFileReader

from . import download
from .constants import MODULES, MOST_RECENT_YEAR, OLDEST_YEAR, SPECS_PATH

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

START = 0
STEP = 10


def _limit_pages(pdf, limit=False):
    """Return the pages number to be extracted"""
    pdf_file = PdfFileReader(str(pdf.resolve()))
    return limit if limit else pdf_file.getNumPages()


def extract_mod_tables(mod, year, pdf=None, limit=False):
    if not pdf:
        download.download_mod_pdf(mod, year)
        pdf = SPECS_PATH / f"{year}" / "pdf" / f"{mod}.pdf"

    pdf_path = str(pdf.resolve())
    limit_pages = _limit_pages(pdf, limit)
    export_csv = SPECS_PATH / f"{year}" / f"{mod}" / "raw_camelot_csv"
    export_csv_path = str((export_csv / f"{mod}.csv").resolve())

    logger.info(
        f"> Extracting pdf {mod.upper()} {year} - {limit_pages} pages. "
        "It can take easily 5 minutes..."
    )
    # Creating directory if not existing
    export_csv.mkdir(parents=True, exist_ok=True)
    # Deleting previous extracted files if existing
    for file in export_csv.iterdir():
        file.unlink()

    # Extracting with camelot : we process the pages 10 by 10 to avoid malloc errors
    i = START
    while i < limit_pages:
        limit = min(i + STEP, limit_pages)
        logger.info(f"    pages {i} to {limit}...")
        tables = camelot.read_pdf(pdf_path, pages=f"{i}-{limit}", line_scale=40)
        tables.export(export_csv_path, f="csv", compress=False)
        i += STEP


@click.command()
@click.option(
    "--year",
    default=MOST_RECENT_YEAR,
    show_default=True,
    type=click.IntRange(OLDEST_YEAR, MOST_RECENT_YEAR),
    help="Operate on a specific year's folder, "
    f"can be between {OLDEST_YEAR} and {MOST_RECENT_YEAR}",
)
@click.option(
    "-l",
    "--limit",
    default=False,
    show_default=True,
    type=int,
    help="Extract a limited number of pdf pages",
)
def main(year, limit):
    """Extract tables from SPED modules pdf (from a given year) using camelot.

    The pdf must be present at './specs/YEAR/' and the extracted CSV files will be
    placed at './specs/YEAR/MODULE/raw_camelot_csv/'.

    If an option --limit is given, only the first pages will be parsed until the limit
    number."""
    logger.info(
        f"Extracting tables from the {year} SPED pdf. It can take a while "
        "(easily 20 minutes)"
    )
    for mod in MODULES:
        extract_mod_tables(mod, year, limit)


if __name__ == "__main__":
    main()

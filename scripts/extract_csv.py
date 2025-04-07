#!/usr/bin/env python3

import logging
import os
from pathlib import Path

import camelot
import click
from download import MOST_RECENT_YEAR, OLDEST_YEAR
from PyPDF2 import PdfFileReader

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

START = 0
STEP = 10


def _limit_pages(pdf_path, limit=False):
    """Return the pages number to be extracted"""
    pdf = PdfFileReader(pdf_path)
    return limit if limit else pdf.getNumPages()


def _extract_csv(mod, pdf_path, year, limit=False):
    limit_pages = _limit_pages(pdf_path, limit)

    export_csv_path = "../specs/{}/{}/raw_camelot_csv/".format(year, mod)
    # Creating directory if not existing
    Path(export_csv_path).mkdir(parents=True, exist_ok=True)
    # Deleting previous extracted files if existing
    for filename in os.listdir(export_csv_path):
        os.unlink(os.path.join(export_csv_path, filename))

    # Extracting with camelot : we process the pages 10 by 10 to avoid malloc errors
    i = START
    while i < limit_pages:
        limit = min(i + STEP, limit_pages)
        logger.info("    extracting pages {} to {}...".format(i, limit))
        tables = camelot.read_pdf(
            pdf_path, pages="{}-{}".format(i, limit), line_scale=40
        )
        tables.export(export_csv_path + "{}.csv".format(mod), f="csv", compress=False)
        i += STEP


@click.command()
@click.option(
    "--year",
    default=MOST_RECENT_YEAR,
    show_default=True,
    type=int,
    help="Extract tables from a specific year between {} and {}".format(
        OLDEST_YEAR, MOST_RECENT_YEAR
    ),
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

    The pdf must be present at '../specs/YEAR/' and the extracted CSV files will be
    placed at '../specs/YEAR/MODULE/raw_camelot_csv/'.

    If an option --limit is given, only the first pages will be parsed until the limit
    number."""
    logger.info(
        "Extracting tables from the {} SPED pdf. It can take a while "
        "(easily 20 minutes)".format(year)
    )
    for mod in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        pdf_path = "../specs/{}/pdf/{}.pdf".format(year, mod)
        limit_pages = _limit_pages(pdf_path, limit)

        logger.info("""> {} - {} pages""".format(mod.upper(), limit_pages))
        _extract_csv(mod, pdf_path, year, limit)


if __name__ == "__main__":
    main()

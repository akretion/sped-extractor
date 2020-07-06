#!/usr/bin/env python3

import csv
import logging

import click
import requests

from .constants import MODULES, MOST_RECENT_YEAR, OLDEST_YEAR, SPECS_PATH

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _get_url(mod, year):
    """Return the first URL found for a module's year version"""
    dl_info_file = SPECS_PATH / f"{year}" / "download_info.csv"
    try:
        with open(dl_info_file, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            header = next(reader)
            col_url = header.index("url")
            col_mod = header.index("module")
            for row in reader:
                if row[col_mod] == mod:
                    return row[col_url]
    except FileNotFoundError:
        logger.exception(
            f"The file '{dl_info_file}' containing the SPED {year} pdfs URLs is "
            "required to download them."
        )


def download_mod_pdf(mod, year):
    logger.info(f"> Downloading pdf {mod.upper()} {year}...")
    pdf_folder = SPECS_PATH / f"{year}" / "pdf"
    # Create pdf folder if necessary
    pdf_folder.mkdir(parents=True, exist_ok=True)

    pdf = pdf_folder / f"{mod}.pdf"
    url = _get_url(mod, year)
    if url:
        try:
            r = requests.get(url)
        except requests.exceptions.MissingSchema:
            logger.exception(
                f"  Cannot download {mod.upper()}'s pdf. '{url}' is not a valid URL."
            )
            pass
        else:
            if not r or r.headers.get("content-type") != "application/pdf":
                logger.warning(f"  No pdf found at '{url}' for {mod.upper()}.")
            else:
                # Remove existing pdf if any
                try:
                    pdf.unlink()
                except FileNotFoundError:
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

    for module in MODULES:
        download_mod_pdf(module, year)


if __name__ == "__main__":
    main()

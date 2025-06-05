import csv
import logging
import pathlib
from typing import Optional, Iterator, Dict, List

import click
import requests

from .constants import (
    MODULES,
    MOST_RECENT_YEAR,
    OLDEST_YEAR,
    SPECS_PATH,
)

logger = logging.getLogger(__name__)


def _read_download_info(year: int) -> Iterator[Dict[str, str]]:
    """Reads the download_info.csv for a given year and yields rows as dicts."""
    dl_info_file: pathlib.Path = SPECS_PATH / str(year) / "download_info.csv"
    if not dl_info_file.is_file():
        logger.error(
            f"The file '{dl_info_file}' (for SPED {year} PDF URLs) is required but not found."
        )
        return

    try:
        with open(dl_info_file, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            required_headers = ["module", "url", "version"]
            if not reader.fieldnames or not all(
                h in reader.fieldnames for h in required_headers
            ):
                logger.error(
                    f"CSV file {dl_info_file} is missing one or more required headers: {', '.join(required_headers)}."
                )
                return
            for row in reader:
                yield row
    except FileNotFoundError:  # Should be caught by is_file()
        logger.error(f"File not found: {dl_info_file}")
    except Exception as e:
        logger.exception(f"Error reading {dl_info_file}: {e}")


def _get_info_for_module(mod_name: str, year: int, key_to_get: str) -> Optional[str]:
    """Helper to get a specific piece of info (url or version) for a module and year."""
    for row in _read_download_info(year):
        if row and row.get("module") == mod_name:
            return row.get(key_to_get)
    return None


def _get_url(mod_name: str, year: int) -> Optional[str]:
    """Return the first URL found for a module's year version"""
    return _get_info_for_module(mod_name, year, "url")


def get_version(mod_name: str, year: int) -> Optional[str]:
    """Return the first layout version for a given mod and year"""
    return _get_info_for_module(mod_name, year, "version")


def download_mod_pdf(mod_name: str, year: int) -> bool:
    """
    Downloads the PDF for a given SPED module and year.
    Returns True on success, False on failure.
    """
    # --- Enhanced Logging Start ---
    pdf_folder: pathlib.Path = SPECS_PATH / str(year) / "pdf"
    # Ensure pdf_folder exists before determining the full pdf_file_path for logging
    # This mkdir is idempotent and safe to call early.
    pdf_folder.mkdir(parents=True, exist_ok=True)
    pdf_file_path: pathlib.Path = pdf_folder / f"{mod_name}.pdf"

    logger.info(
        f"Attempting to download PDF for module '{mod_name.upper()}' for year {year}."
    )
    logger.info(f"  Target file location: {pdf_file_path}")
    # --- Enhanced Logging End ---

    # Original logging for the actual download process can be kept or refined
    # logger.info(f"> Downloading PDF {mod_name.upper()} {year}...") # This is a bit redundant now

    url = _get_url(mod_name, year)

    if not url:
        logger.warning(
            f"  No URL found for {mod_name.upper()} {year} in download_info.csv. Download skipped."
        )
        return False

    logger.info(f"  Downloading from URL: {url}")  # Log the URL being used

    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
    except requests.exceptions.MissingSchema:
        logger.error(
            f"  Cannot download {mod_name.upper()}'s PDF. '{url}' is not a valid URL."
        )
        return False
    except requests.exceptions.RequestException as e:
        logger.error(f"  Error downloading {mod_name.upper()} from {url}: {e}")
        return False

    if "application/pdf" not in response.headers.get("content-type", "").lower():
        logger.warning(
            f"  Content at '{url}' for {mod_name.upper()} is not PDF "
            f"(Content-Type: {response.headers.get('content-type')}). Download aborted."
        )
        return False

    try:
        pdf_file_path.unlink(missing_ok=True)
        with open(pdf_file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        logger.info(
            f"  Successfully downloaded and saved: {pdf_file_path}"
        )  # Kept this for clarity
        return True
    except IOError as e:
        logger.error(f"  Could not write PDF file {pdf_file_path}: {e}")
        return False


@click.command()
@click.option(
    "--year",
    default=MOST_RECENT_YEAR,
    show_default=True,
    type=click.IntRange(OLDEST_YEAR, MOST_RECENT_YEAR),
    help=f"Year of the SPED specifications (between {OLDEST_YEAR} and {MOST_RECENT_YEAR}).",
)
@click.option(
    "--module",
    "target_module_str",
    type=click.Choice(MODULES, case_sensitive=False),
    required=False,
    help="Specific SPED module to download. If not provided, all modules will be downloaded.",
)
def main(year: int, target_module_str: Optional[str]):
    """Download SPED specification PDFs from official sources."""
    # Configure basic logging if not already configured by test runner or other setup
    # This is a simple fallback for direct script execution.
    # In tests, pytest's logging config usually takes precedence.
    if not logging.getLogger().hasHandlers():  # Check if root logger has handlers
        logging.basicConfig(
            level=logging.INFO, format="%(levelname)s: %(name)s: %(message)s"
        )

    logger.info(f"--- Starting PDF download process for SPED {year} ---")

    modules_to_download: List[str] = []
    if target_module_str:
        modules_to_download.append(target_module_str.lower())
    else:
        modules_to_download = MODULES

    # Ensure the base 'specs/YEAR' directory and 'download_info.csv' exists
    year_spec_dir = SPECS_PATH / str(year)
    download_info_file = year_spec_dir / "download_info.csv"

    if not download_info_file.is_file():
        logger.error(
            f"Required file 'download_info.csv' not found in '{year_spec_dir}'. "
            "Cannot proceed with downloads for this year."
        )
        # Create the year directory if it doesn't exist, even if download_info is missing,
        # so that pdf subfolder can be potentially created by download_mod_pdf
        year_spec_dir.mkdir(parents=True, exist_ok=True)
        (year_spec_dir / "pdf").mkdir(
            parents=True, exist_ok=True
        )  # Also ensure pdf dir
        return

    success_count = 0
    failure_count = 0
    for mod_name in modules_to_download:
        if download_mod_pdf(mod_name, year):  # This will now use the enhanced logging
            success_count += 1
        else:
            failure_count += 1

    logger.info(f"--- PDF download process finished for SPED {year} ---")
    logger.info(f"Summary: {success_count} downloaded, {failure_count} failed/skipped.")


if __name__ == "__main__":
    main()

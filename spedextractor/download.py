import csv
import logging
import pathlib
from typing import Optional, List

import click
import requests

from .constants import (
    MODULES,
    MODULES2,
    SPECS_PATH,
)

logger = logging.getLogger(__name__)


def download_mod_pdf(mod_name: str) -> bool:
    """
    Downloads the PDF for a given SPED module.
    Returns True on success, False on failure.
    """
    pdf_folder: pathlib.Path = (
        SPECS_PATH / mod_name / str(MODULES2[mod_name][0]) / "pdf"
    )
    pdf_folder.mkdir(parents=True, exist_ok=True)
    pdf_file_path: pathlib.Path = pdf_folder / f"{mod_name}.pdf"

    logger.info(f"Attempting to download PDF for module '{mod_name.upper()}'.")
    logger.info(f"  Target file location: {pdf_file_path}")

    url = MODULES2[mod_name][2]
    logger.info(f"  Downloading from URL: {url}")

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
    "--module",
    "target_module_str",
    type=click.Choice(MODULES, case_sensitive=False),
    required=False,
    help="Specific SPED module to download. If not provided, all modules will be downloaded.",
)
def main(target_module_str: Optional[str]):
    """Download SPED specification PDFs from official sources."""
    # Configure basic logging if not already configured by test runner or other setup
    # This is a simple fallback for direct script execution.
    # In tests, pytest's logging config usually takes precedence.
    if not logging.getLogger().hasHandlers():  # Check if root logger has handlers
        logging.basicConfig(
            level=logging.INFO, format="%(levelname)s: %(name)s: %(message)s"
        )

    logger.info("--- Starting PDF download process for SPED ---")

    modules_to_download: List[str] = []
    if target_module_str:
        modules_to_download.append(target_module_str.lower())
    else:
        modules_to_download = MODULES

    for module in modules_to_download:
        layout = MODULES2[module][0]
        spec_dir = SPECS_PATH / module / str(layout)

        spec_dir.mkdir(parents=True, exist_ok=True)
        (spec_dir / "pdf").mkdir(parents=True, exist_ok=True)

        if download_mod_pdf(module):
            logger.info(f"--- PDF download process finished for SPED {module} ---")


if __name__ == "__main__":
    main()

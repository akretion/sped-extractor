import sys
import logging
import pathlib
import warnings
from typing import Optional, List

import camelot

from PyPDF2.errors import PdfReadWarning

import click

try:
    from PyPDF2 import PdfReader
except ImportError:
    from PyPDF2 import PdfFileReader as PdfReader  # type: ignore

from . import download
from .constants import (
    MODULES,
    SPECS_PATH,
)

warnings.filterwarnings("ignore", category=PdfReadWarning)

logger = logging.getLogger(__name__)

CAMELOT_LINE_SCALE: int = 40
DEFAULT_CHUNK_SIZE: int = 10


def _get_pdf_page_count(pdf_path: pathlib.Path) -> int:
    """Return the number of pages in the PDF, or 0 if error."""
    if not pdf_path.is_file():
        logger.error(f"PDF file not found at {pdf_path} for counting pages.")
        return 0
    try:
        with open(pdf_path, "rb") as f:
            pdf_reader = PdfReader(f)
            return len(pdf_reader.pages)
    except Exception as e:
        logger.error(f"Error reading PDF {pdf_path} for page count: {e}")
        return 0


def extract_mod_tables(
    mod_name: str,
    pdf_path_override: Optional[pathlib.Path] = None,
    limit_pages_to_extract: int = 0,
    page_chunk_size: int = DEFAULT_CHUNK_SIZE,
) -> bool:
    """
    Extracts tables from a single SPED module's PDF.
    Returns True if extraction process completed, False if critical error.
    """
    pdf_to_process: pathlib.Path
    if pdf_path_override:
        pdf_to_process = pdf_path_override
    else:
        pdf_to_process = (
            SPECS_PATH / mod_name / str(MODULES[mod_name][0]) / f"{mod_name}.pdf"
        )

    if not pdf_to_process.is_file():
        logger.info(f"PDF {pdf_to_process.name} not found. Attempting download...")
        if not download.download_mod_pdf(mod_name):
            logger.error(
                f"Failed to download PDF for {mod_name.upper()}. Cannot extract tables."
            )
            return False
        if not pdf_path_override and not pdf_to_process.is_file():
            logger.error(
                f"PDF still not found at {pdf_to_process} after download attempt. Cannot extract tables."
            )
            return False

    actual_page_count = _get_pdf_page_count(pdf_to_process)
    if actual_page_count == 0:
        logger.warning(
            f"Cannot process PDF {pdf_to_process.name} as it has 0 pages or is unreadable."
        )
        return False

    pages_to_process = actual_page_count
    if limit_pages_to_extract > 0:
        pages_to_process = min(limit_pages_to_extract, actual_page_count)

    if pages_to_process == 0:
        logger.info(f"No pages to process for {pdf_to_process.name}.")
        return True

    export_csv_dir: pathlib.Path = (
        SPECS_PATH / mod_name / str(MODULES[mod_name][0]) / "raw_camelot_csv"
    )

    logger.info(
        f"> Extracting PDF {pdf_to_process.name} - "
        f"{pages_to_process} of {actual_page_count} page(s) to {export_csv_dir}"
    )
    export_csv_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"  Cleaning up previous CSV files in {export_csv_dir}...")
    for file in export_csv_dir.glob("*.csv"):
        try:
            file.unlink()
        except OSError as e:
            logger.warning(f"Could not delete old CSV {file}: {e}")

    current_page_start = 1
    extraction_successful_for_all_chunks = True
    while current_page_start <= pages_to_process:
        end_page_in_chunk = min(
            current_page_start + page_chunk_size - 1, pages_to_process
        )
        page_range_str = f"{current_page_start}-{end_page_in_chunk}"

        logger.info(f"    Processing pages {page_range_str}...")
        try:
            tables = camelot.read_pdf(
                str(pdf_to_process),
                pages=page_range_str,
                line_scale=CAMELOT_LINE_SCALE,
            )
            if tables.n == 0:
                logger.info(
                    f"      No tables found by Camelot on pages {page_range_str}."
                )
            else:
                export_filename_prefix = export_csv_dir / mod_name
                tables.export(str(export_filename_prefix), f="csv", compress=False)
                logger.info(
                    f"      Exported {tables.n} table(s) from pages {page_range_str}. "
                    f"Files saved in {export_csv_dir} with prefix '{mod_name}-page-*'."
                )
        except Exception as e:
            logger.error(
                f"    Error processing pages {page_range_str} with Camelot for {pdf_to_process.name}: {e}"
            )
            extraction_successful_for_all_chunks = False
        current_page_start = end_page_in_chunk + 1

    logger.info(f"Finished extracting tables for {mod_name.upper()}.")
    return extraction_successful_for_all_chunks


@click.command()
@click.option(
    "--module",
    "target_module_str",
    type=click.Choice(MODULES.keys(), case_sensitive=False),
    required=False,
    help="Specific SPED module to process. If not provided, all configured modules will be processed.",
)
@click.option(
    "-l",
    "--limit-pages",
    "limit_pages_to_extract",
    default=0,
    show_default=True,
    type=click.IntRange(min=0),
    help="Limit extraction to the first N pages of the PDF (0 for no limit).",
)
@click.option(
    "--chunk-size",
    default=DEFAULT_CHUNK_SIZE,
    show_default=True,
    type=click.IntRange(min=1),
    help="Number of PDF pages to process in each Camelot batch.",
)
def main(
    target_module_str: Optional[str],
    limit_pages_to_extract: int,
    chunk_size: int,
):
    """
    Extract tables from SPED module PDF using Camelot.
    PDFs are expected in './specs/MODULE/LAYOUT/pdf/' or will be downloaded if missing.
    Extracted CSV files are placed in './specs/MODULE/LAYOUT/raw_camelot_csv/'.
    """
    if "pytest" not in sys.modules:
        # If no handlers are configured for the root logger OR for our specific logger,
        # set up basic console logging.
        # Check both to be more robust.
        sped_logger = logging.getLogger(
            "spedextractor"
        )  # Get your package's base logger
        if not logging.getLogger().hasHandlers() and not sped_logger.hasHandlers():
            logging.basicConfig(
                level=logging.INFO,
                format="%(levelname)-7s: %(name)s: %(message)s",  # Slightly more informative format
            )

    logger.info("--- Starting table extraction process for SPED ---")

    modules_to_process: List[str] = []
    if target_module_str:
        modules_to_process.append(target_module_str.lower())
    else:
        modules_to_process = MODULES.keys()

    overall_success = True
    for mod_name in modules_to_process:
        logger.info(f"Processing module: {mod_name.upper()}")
        if not extract_mod_tables(
            mod_name,
            limit_pages_to_extract=limit_pages_to_extract,
            page_chunk_size=chunk_size,
        ):
            overall_success = False

    logger.info("--- Table extraction process finished for SPED ---")
    if not overall_success:
        logger.warning(
            "One or more modules encountered critical errors during extraction."
        )


if __name__ == "__main__":
    if not logging.getLogger().hasHandlers() or not logging.getLogger().handlers:
        logging.basicConfig(
            level=logging.INFO, format="%(levelname)s %(name)s:%(lineno)d: %(message)s"
        )
    main()

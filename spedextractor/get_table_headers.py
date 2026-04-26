import logging

import click

from .build_csv import _is_reg_row, clean_row, get_raw_rows
from .constants import MODULES

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def get_mod_table_headers(mod: str, layout: int) -> list[list[str]]:
    """Extract table headers from a module's raw CSV data."""
    previous_row: list[str] | None = None
    headers: list[list[str]] = []
    raw_rows = get_raw_rows(mod, layout)

    for page in raw_rows:
        for row in raw_rows[page]:
            cleaned_row = clean_row(row)
            if (
                len(cleaned_row) > 2
                and _is_reg_row(cleaned_row)
                and previous_row is not None
                and previous_row not in headers
            ):
                headers.append(previous_row)
            previous_row = cleaned_row
    return headers


@click.option(
    "--layout",
    "target_layout",
    type=int,
    help="Specific layout version to process (if not provided, uses the default for each module)",
)
@click.command()
def main(target_layout: int | None) -> None:
    """Display a list of all the different fields headers found in the four modules.

    Used to define the modules headers hard-coded at the beginning of ./build_csv.py .
    """
    for mod in MODULES:
        layout = target_layout if target_layout is not None else MODULES[mod][0]
        headers = get_mod_table_headers(mod, layout)
        logger.info(f"\n{mod.upper()}'s headers :")
        for header in headers:
            logger.info(header)


if __name__ == "__main__":
    main()

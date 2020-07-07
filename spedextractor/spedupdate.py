import logging
import pathlib

import click

from .constants import MODULES, MOST_RECENT_YEAR, OLDEST_YEAR, SPECS_PATH

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _get_source_files(year):
    """Returns two lists of year's modules CSV files :
    - one with the MODULE_registers.csv
    - another with the MODULE_fields.csv
    """
    registers_files = []
    fields_files = []
    year_path = SPECS_PATH / f"{year}"
    mod_dirs = [d for d in year_path.iterdir() if d.is_dir() and d.name in MODULES]

    for mod_dir in mod_dirs:
        for file in mod_dir.iterdir():
            if file.name == f"{mod_dir.name}_registers.csv":
                registers_files.append(file)
            if file.name == f"{mod_dir.name}_fields.csv":
                fields_files.append(file)

    return registers_files, fields_files


@click.command()
@click.option(
    "--year",
    default=MOST_RECENT_YEAR,
    show_default=True,
    type=click.IntRange(OLDEST_YEAR, MOST_RECENT_YEAR),
    help="Operate on a specific year's folder, "
    f"can be between {OLDEST_YEAR} and {MOST_RECENT_YEAR}",
)
@click.argument("dest_dir_path", type=click.Path(file_okay=False, resolve_path=True))
def main(year, dest_dir_path):
    dest_dir = pathlib.Path(dest_dir_path)
    # Catch source MODULE_accurate_registers.csv and MODULE_accurate_fields.csv files
    registers_files, fields_files = _get_source_files(year)

    if not dest_dir.exists():
        click.confirm(
            f"The directory {dest_dir_path} doesn't exist yet.\n"
            "Would you like to create it and copy sped-extractor's CSV files in it ?",
            abort=True,
        )
        dest_dir.mkdir(parents=True)
        # Copy source files in the new user's directory
        for file in registers_files + fields_files:
            new_file = dest_dir / file.name
            with open(new_file, "w") as newfile:
                # TODO : Add new column for mapping
                newfile.write(file.read_text())

        return True

    pass


if __name__ == "__main__":
    main()

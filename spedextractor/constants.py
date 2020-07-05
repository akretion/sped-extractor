import pathlib

SPECS_PATH = pathlib.Path(__file__).parent.resolve() / "specs"
MODULES = ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]


def _get_max_min_year():
    """Return a tuplet with most recent and oldest year folder available in './specs/'
    """
    years = [entry.name for entry in SPECS_PATH.iterdir() if entry.is_dir()]
    return (int(max(years, key=int)), int(min(years, key=int)))


MOST_RECENT_YEAR = _get_max_min_year()[0]
OLDEST_YEAR = _get_max_min_year()[1]

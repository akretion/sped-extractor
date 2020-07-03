import os


def _get_max_min_year():
    """Return a tuplet with most recent and oldest year folder available in '../specs/'
    """
    years = [f.name for f in os.scandir("../specs/") if f.is_dir()]
    return (int(max(years, key=int)), int(min(years, key=int)))


MOST_RECENT_YEAR = _get_max_min_year()[0]
OLDEST_YEAR = _get_max_min_year()[1]

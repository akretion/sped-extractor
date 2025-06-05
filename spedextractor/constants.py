import pathlib
import logging
from typing import Tuple, Optional, List, Dict

logger = logging.getLogger(__name__)

SPECS_PATH: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "specs"

MODULES: List[str] = ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]


def _get_max_min_year() -> Tuple[Optional[int], Optional[int]]:
    """Return a tuple with most recent and oldest year folder available in './specs/'
    Returns (None, None) if no valid year directories are found.
    """
    valid_years: List[int] = []
    if SPECS_PATH.exists() and SPECS_PATH.is_dir():
        for entry in SPECS_PATH.iterdir():
            if entry.is_dir():
                try:
                    valid_years.append(int(entry.name))
                except ValueError:
                    logger.debug(f"Skipping non-integer directory name: {entry.name}")

    if not valid_years:
        logger.warning(
            f"No valid year directories found in {SPECS_PATH}. "
            "Cannot determine MOST_RECENT_YEAR or OLDEST_YEAR."
        )
        return None, None
    return max(valid_years), min(valid_years)


_max_year, _min_year = _get_max_min_year()

MOST_RECENT_YEAR: int = _max_year if _max_year is not None else 2024  # Example default
OLDEST_YEAR: int = _min_year if _min_year is not None else 2010  # Example default

MODULE_HEADER: Dict[str, List[Tuple[str, str]]] = {
    "ecd": [
        ("Nº", "index"),
        ("Campo", "code"),
        ("Descrição", "desc"),
        ("Tipo", "spec_type"),
        ("Tamanho", "length"),
        ("Decimal", "decimal"),
        ("Valores Válidos", "spec_values"),
        ("Obrigatório", "spec_required"),
        ("Regras de Validação do Campo", "rules"),
    ],
    "ecf": [
        ("Nº", "index"),
        ("Campo", "code"),
        ("Descrição", "desc"),
        ("Tipo", "spec_type"),
        ("Tamanho", "length"),
        ("Decimal", "decimal"),
        ("Valores Válidos", "spec_values"),
        ("Obrigatório", "spec_required"),
    ],
    "efd_icms_ipi": [
        ("Nº", "index"),
        ("Campo", "code"),
        ("Descrição", "desc"),
        ("Tipo", "spec_type"),
        ("Tam", "length"),
        ("Dec", "decimal"),
        ("Obrig", "spec_required"),
        ("Entr", "spec_in"),
        ("Saídas", "spec_out"),
    ],
    "efd_pis_cofins": [
        ("Nº", "index"),
        ("Campo", "code"),
        ("Descrição", "desc"),
        ("Tipo", "spec_type"),
        ("Tam", "length"),
        ("Dec", "decimal"),
        ("Obrig", "spec_required"),
    ],
}

import pathlib
import logging
from typing import Tuple, List, Dict

logger = logging.getLogger(__name__)

SPECS_PATH: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "specs"

MODULES: dict[str, tuple] = {
    "ecd": (9, "2024-11-01", "http://sped.rfb.gov.br/arquivo/download/7300"),
    "ecf": (9, "2025-05-02", "http://sped.rfb.gov.br/arquivo/download/7625"),  # TODO 10
    "efd_icms_ipi": (19, "25-09-2024", "http://sped.rfb.gov.br/arquivo/download/7545"),
    "efd_pis_cofins": (6, "2021-06-18", "http://sped.rfb.gov.br/arquivo/download/5836"),
}

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

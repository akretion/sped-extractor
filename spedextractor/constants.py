import pathlib
import logging
from typing import TypedDict, Tuple, List, Dict

try:
    from typing import NotRequired
except ImportError:
    from typing_extensions import NotRequired

logger = logging.getLogger(__name__)

SPECS_PATH: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "specs"

ModuleInfo = tuple[int, str, str]

MODULES: dict[str, ModuleInfo] = {
    "ecd": (9, "2024-11-01", "http://sped.rfb.gov.br/arquivo/download/7300"),
    "ecf": (10, "2025-05-02", "http://sped.rfb.gov.br/arquivo/download/7625"),
    "efd_icms_ipi": (
        20,
        "2025-07-07",
        "http://sped.rfb.gov.br/estatico/A7/5FB73968C31ABA91EA180EC5CFDB714293F604/NT-2025.001%20v1.0.pdf",
    ),
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


class RegisterDict(TypedDict):
    block: str
    code: str
    desc: str
    level: int
    card: str
    required: NotRequired[bool]
    conditional_required: NotRequired[bool]
    in_required: NotRequired[bool]
    out_required: NotRequired[bool]
    conditional_in_required: NotRequired[bool]
    conditional_out_required: NotRequired[bool]
    spec_required: NotRequired[str]
    spec_in: NotRequired[str]
    spec_out: NotRequired[str]
    parent: NotRequired["RegisterDict"]
    o2m_parent: NotRequired["RegisterDict"]
    children_o2m: NotRequired[list["RegisterDict"]]
    children_m2o: NotRequired[list["RegisterDict"]]
    short_desc: NotRequired[str]


class FieldDict(TypedDict):
    register: str
    index: int
    code: str
    desc: NotRequired[str]
    type: NotRequired[str]
    xsd_type: NotRequired[str]
    required: NotRequired[bool]
    conditional_required: NotRequired[bool]
    in_required: NotRequired[bool]
    out_required: NotRequired[bool]
    conditional_in_required: NotRequired[bool]
    conditional_out_required: NotRequired[bool]
    length: NotRequired[str]
    decimal: NotRequired[str]
    spec_type: NotRequired[str]
    spec_required: NotRequired[str]
    spec_in: NotRequired[str]
    spec_out: NotRequired[str]
    spec_values: NotRequired[str]
    values: NotRequired[list[str]]
    rules: NotRequired[list[str]]


class BlockDict(TypedDict):
    code: str
    desc: str
    info: NotRequired[str]


RawRows = dict[int, list[list[str]]]

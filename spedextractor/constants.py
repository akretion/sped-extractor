import pathlib

SPECS_PATH = pathlib.Path(__file__).parent.resolve() / "specs"


def _get_max_min_year():
    """Return a tuplet with most recent and oldest year folder available in './specs/'
    """
    years = [entry.name for entry in SPECS_PATH.iterdir() if entry.is_dir()]
    return (int(max(years, key=int)), int(min(years, key=int)))


MOST_RECENT_YEAR = _get_max_min_year()[0]
OLDEST_YEAR = _get_max_min_year()[1]

MODULES = ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]

# We chose to hard-code the modules fields headers because it is easier to actualize
# them manually when necessary than mantaining a good heuristic algorithm catching these
# headers from raw CSV files.
# To define these headers manually, please use the script :
# `python -m spedextractor.get_mod_headers`
# which displays all the possible headers for each module.
MODULE_HEADER = {
    "ecd": [
        ("Nº", "index"),
        ("Campo", "code"),
        ("Descrição", "desc"),
        # key "type" reserved for the interpreted field dictionary
        ("Tipo", "spec_type"),
        ("Tamanho", "length"),
        ("Decimal", "decimal"),
        ("Valores Válidos", "spec_values"),
        # key "required" reserved for the interpreted field dictionary
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

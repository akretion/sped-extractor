import pytest

from spedextractor import build_csv, pva

# A miniature of a real descriptor, with the dirt the real ones carry: an
# accented attribute NAME (EFD ICMS/IPI), a field position written "3'", a
# fixed size written [4], a conditionally required register (obrigatorio=2)
# and a register removed from the layout by commenting it out.
DESCRIPTOR = """<descritor-escrituracao>
  <blocos>
    <registro id="0000" descricao="Abertura do Arquivo Digital" nivel="0" ocorrencia="0" obrigatorio="1" rotulo="0000">
      <campo n="1" id="REG" tipo="C" tamanho="[4]" obrigatorio="1" rotulo="Registro" />
      <campo n="2" id="COD_MUN" tipo="N" tamanho="7" obrigatorio="0" rotulo="Municipio" />
    </registro>
    <registro id="E100" descricao="Periodo da Apuracao" nivel="2" ocorrencia="2" obrigatorio="2" rotulo="E100">
      <campo n="1" id="REG" tipo="C" tamanho="[4]" obrigatorio="1" rotulo="Registro" />
      <campo n="2" id="DT_INI" tipo="D" tamanho="[8]" obrigatorio="1" rotulo="Data inicial" descrição="Data inicial do periodo" />
      <registro id="E110" descricao="Apuracao do ICMS" nivel="3" ocorrencia="1" obrigatorio="1" rotulo="E110">
        <campo n="1" id="REG" tipo="C" tamanho="[4]" obrigatorio="1" rotulo="Registro" />
        <campo n="3'" id="VL_TOT_CREDITOS" tipo="N" casasdecimais="2" obrigatorio="1" rotulo="Total dos creditos" />
        <campo n="2" id="IND_MOV" tipo="N" tamanho="1" obrigatorio="1" rotulo="Movimento">
          <valores-validos valores="0=Sem movimento;1=Com movimento" />
        </campo>
      </registro>
    </registro>
    <!-- Registro 1600 excluido a partir de 2022 -->
    <!-- <registro id="1600" nivel="2" ocorrencia="2" obrigatorio="0" rotulo="1600"> </registro> -->
  </blocos>
</descritor-escrituracao>"""


@pytest.fixture
def specs_path(tmp_path, monkeypatch):
    monkeypatch.setattr(pva, "SPECS_PATH", tmp_path)
    monkeypatch.setattr(build_csv, "SPECS_PATH", tmp_path)
    return tmp_path


@pytest.fixture
def generated(specs_path):
    pva.build_from_descriptor("efd_icms_ipi", 99, DESCRIPTOR.encode())
    return specs_path / "efd_icms_ipi" / "99"


def test_accurate_fields_csv_has_the_pdf_shape(generated):
    lines = (generated / "accurate_fields.csv").read_text().splitlines()
    header = '"Register","Page","Nº","Campo","Descrição","Tipo","Tam","Dec","Obrig","Entr","Saídas"'
    assert lines[0] == header
    # fixed [4] becomes 004*, plain 7 becomes 007, and Page marks the source
    assert '"0000","pva","1","REG","Registro","C","004*","","O","",""' in lines
    assert '"0000","pva","2","COD_MUN","Municipio","N","007","","","",""' in lines


def test_reg_row_carries_the_register_mandatoriness(generated):
    lines = (generated / "accurate_fields.csv").read_text().splitlines()
    # E100 is obrigatorio=2 in the descriptor: its REG row must say OC
    assert '"E100","pva","1","REG","Registro","C","004*","","OC","",""' in lines


def test_fields_come_out_in_position_order(generated):
    """The file is positional: a position written "3'" must not break it."""
    rows = [
        line
        for line in (generated / "accurate_fields.csv").read_text().splitlines()
        if line.startswith('"E110"')
    ]
    codes = [row.split(",")[3] for row in rows]
    assert codes == ['"REG"', '"IND_MOV"', '"VL_TOT_CREDITOS"']


def test_commented_out_register_stays_out(generated):
    content = (generated / "registers_pva.csv").read_text()
    assert "1600" not in content


def test_registers_csv_roundtrip(generated):
    registers = pva.read_registers_csv(generated / "registers_pva.csv")
    by_code = {register["code"]: register for register in registers}
    assert list(by_code) == ["0000", "E100", "E110"]
    assert by_code["E100"]["level"] == 2
    assert by_code["E100"]["card"] == "1:N"
    assert by_code["E110"]["card"] == "1:1"
    assert by_code["E110"]["required"] is True
    assert "required" not in by_code["E100"]  # obrigatorio=2 is not plain required


def test_extract_registers_list_prefers_the_descriptor(generated):
    """With registers_pva.csv in place the pdf pipeline must not be touched."""
    registers = build_csv.extract_registers_list("efd_icms_ipi", 99)
    assert [register["code"] for register in registers] == ["0000", "E100", "E110"]


def test_get_fields_interprets_the_descriptor_rows(generated):
    fields = build_csv.get_fields("efd_icms_ipi", 99)
    by_code = {field["code"]: field for field in fields}
    assert by_code["VL_TOT_CREDITOS"]["type"] == "float"
    assert by_code["VL_TOT_CREDITOS"]["required"] is True
    assert by_code["DT_INI"]["type"] == "date"
    # numeric with no decimals is a code, not a number
    assert by_code["COD_MUN"]["type"] == "char"

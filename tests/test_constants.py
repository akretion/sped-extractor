import pytest
from spedextractor import constants as sped_constants

@pytest.fixture
def mock_specs_path_empty(tmp_path, monkeypatch):
    specs_dir = tmp_path / "specs"
    specs_dir.mkdir()
    monkeypatch.setattr(sped_constants, "SPECS_PATH", specs_dir)
    return specs_dir

@pytest.fixture
def mock_specs_path_with_years(tmp_path, monkeypatch):
    specs_dir = tmp_path / "specs"
    specs_dir.mkdir()
    (specs_dir / "2020").mkdir()
    (specs_dir / "2022").mkdir()
    (specs_dir / "2021").mkdir()
    (specs_dir / "not_a_year").mkdir()
    monkeypatch.setattr(sped_constants, "SPECS_PATH", specs_dir)
    return specs_dir

def test_get_max_min_year_no_year_dirs(mock_specs_path_empty, caplog):
    max_y, min_y = sped_constants._get_max_min_year()
    assert max_y is None
    assert min_y is None
    assert "No valid year directories found" in caplog.text

def test_get_max_min_year_with_dirs(mock_specs_path_with_years):
    max_y, min_y = sped_constants._get_max_min_year()
    assert max_y == 2022
    assert min_y == 2020

def test_modules_list():
    assert "ecd" in sped_constants.MODULES
    assert isinstance(sped_constants.MODULES, list)

def test_module_header_exists():
    assert "ecd" in sped_constants.MODULE_HEADER
    assert isinstance(sped_constants.MODULE_HEADER["ecd"], list)

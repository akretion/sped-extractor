# tests/test_download.py
import pytest
from click.testing import CliRunner
from pathlib import Path
from unittest import mock
import logging # Import logging for caplog.set_level

from spedextractor import download
from spedextractor import constants as download_constants

# This fixture provides a mocked SPECS_PATH and ensures it's cleaned up
@pytest.fixture
def mock_specs(tmp_path, monkeypatch):
    m_specs_path = tmp_path / "specs_test_download_cli" # Unique name
    m_specs_path.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(download, "SPECS_PATH", m_specs_path)
    monkeypatch.setattr(download_constants, "SPECS_PATH", m_specs_path)
    return m_specs_path

# This fixture creates the necessary download_info.csv in the mocked SPECS_PATH
@pytest.fixture
def dummy_download_info_csv(mock_specs): # Depends on mock_specs
    year = "2023" # Align with year used in tests
    year_dir = mock_specs / year
    year_dir.mkdir(parents=True, exist_ok=True)
    csv_file = year_dir / "download_info.csv"
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("module,url,version\n")
        f.write("ecd,http://example.com/ecd.pdf,1.0\n")
        f.write("ecf,http://example.com/ecf.pdf,2.0\n")
    return csv_file

@pytest.fixture(autouse=True) # This autouse is fine
def mock_requests_global(mocker): # Renamed for clarity, applies globally
    """
    Automatically mock requests.get for all tests in this file
    to prevent actual network calls.
    """
    mock_get_instance = mocker.patch("requests.get") # This is the mock object for the 'get' function
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.headers = {"content-type": "application/pdf"}
    mock_response.content = b"%PDF-dummy-content-global" # Generic content
    mock_response.iter_content.return_value = [b"%PDF-dummy-content-global"]
    mock_response.raise_for_status = mock.Mock()
    mock_get_instance.return_value = mock_response
    return mock_get_instance # Return the mock of requests.get itself

# --- Unit tests for download_mod_pdf (should be separate from CLI tests usually) ---
# These were the tests that were passing before, let's ensure they are still here and correct.

@pytest.fixture
def unit_test_mock_specs(tmp_path, monkeypatch): # Separate mock_specs for unit tests if needed
    m_specs_path = tmp_path / "specs_test_unit"
    m_specs_path.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(download, "SPECS_PATH", m_specs_path)
    monkeypatch.setattr(download_constants, "SPECS_PATH", m_specs_path)
    return m_specs_path

@pytest.fixture
def unit_test_dummy_download_info_csv(unit_test_mock_specs):
    year = "2023"
    year_dir = unit_test_mock_specs / year
    year_dir.mkdir(parents=True, exist_ok=True)
    csv_file = year_dir / "download_info.csv"
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("module,url,version\n")
        f.write("ecd,http://example.com/ecd-unit.pdf,1.0-unit\n") # Different URL for clarity
    return csv_file

def test_download_mod_pdf_success_unit(unit_test_mock_specs, unit_test_dummy_download_info_csv, mock_requests_global, caplog):
    # mock_requests_global is autouse, but we also accept it as an argument
    # to make it explicit that this test uses it for assertions.
    mod_name = "ecd"
    year = 2023

    assert download.download_mod_pdf(mod_name, year) is True

    # mock_requests_global is the mock of requests.get
    mock_requests_global.assert_any_call("http://example.com/ecd-unit.pdf", stream=True, timeout=30)

    expected_pdf_path = unit_test_mock_specs / str(year) / "pdf" / f"{mod_name}.pdf"
    assert expected_pdf_path.exists()
    assert expected_pdf_path.read_bytes() == b"%PDF-dummy-content-global"
    assert f"Successfully downloaded and saved: {expected_pdf_path}" in caplog.text

def test_get_url_found_unit(unit_test_mock_specs, unit_test_dummy_download_info_csv): # Needs its own mock_specs
    url = download._get_url("ecd", 2023)
    assert url == "http://example.com/ecd-unit.pdf"


# --- CLI Tests ---
def TODOtest_download_cli_specific_module(mocker, mock_specs, dummy_download_info_csv, caplog):
    # mock_requests_for_cli_tests is autouse, so it's active.
    # mock_specs and dummy_download_info_csv provide the file system setup.

    mocker.patch.object(download_constants, "MOST_RECENT_YEAR", 2023)
    mocker.patch.object(download_constants, "OLDEST_YEAR", 2020)
    mocker.patch.object(download_constants, "MODULES", ["ecd", "ecf"]) # Critical for click.Choice

    runner = CliRunner()
    result = runner.invoke(download.main, ["--year", "2023", "--module", "ecd"])

    assert result.exit_code == 0, f"CLI failed. Output: {result.output}\nLogs: {caplog.text}"

    # Check logs to infer behavior
    assert "Attempting to download PDF for module 'ECD' for year 2023." in caplog.text
    expected_pdf_path = mock_specs / "2023" / "pdf" / "ecd.pdf"
    assert f"Target file location: {expected_pdf_path}" in caplog.text
    assert f"Successfully downloaded and saved: {expected_pdf_path}" in caplog.text
    assert (mock_specs / "2023" / "pdf" / "ecd.pdf").exists()
    assert not (mock_specs / "2023" / "pdf" / "ecf.pdf").exists()


def TODOtest_download_cli_all_modules(mocker, mock_specs, dummy_download_info_csv, caplog):
    # mock_requests_for_cli_tests is autouse.
    # mock_specs and dummy_download_info_csv provide the file system setup.

    mocker.patch.object(download_constants, "MOST_RECENT_YEAR", 2023)
    mocker.patch.object(download_constants, "OLDEST_YEAR", 2020)
    test_modules = ["ecd", "ecf"]
    mocker.patch.object(download_constants, "MODULES", test_modules)

    runner = CliRunner()
    result = runner.invoke(download.main, ["--year", "2023"])

    assert result.exit_code == 0, f"CLI failed. Output: {result.output}\nLogs: {caplog.text}"

    # Check ECD logs and file
    assert "Attempting to download PDF for module 'ECD' for year 2023." in caplog.text
    expected_ecd_pdf_path = mock_specs / "2023" / "pdf" / "ecd.pdf"
    assert f"Target file location: {expected_ecd_pdf_path}" in caplog.text
    assert f"Successfully downloaded and saved: {expected_ecd_pdf_path}" in caplog.text
    assert (mock_specs / "2023" / "pdf" / "ecd.pdf").exists()

    # Check ECF logs and file
    assert "Attempting to download PDF for module 'ECF' for year 2023." in caplog.text
    expected_ecf_pdf_path = mock_specs / "2023" / "pdf" / "ecf.pdf"
    assert f"Target file location: {expected_ecf_pdf_path}" in caplog.text
    assert f"Successfully downloaded and saved: {expected_ecf_pdf_path}" in caplog.text
    assert (mock_specs / "2023" / "pdf" / "ecf.pdf").exists()

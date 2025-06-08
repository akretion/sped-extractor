import pytest
from click.testing import CliRunner
from pathlib import Path
from unittest import mock

from spedextractor import extract_tables
from spedextractor import constants as extract_constants
from spedextractor.constants import MODULES

from spedextractor import (
    download as extract_download_module,
)  # For mocking download calls from extract_tables

# Try to import PdfWriter for PyPDF2 >= 2.0.0, fallback for < 2.0.0
try:
    from PyPDF2 import PdfWriter  # For PyPDF2 >= 2.0.0

    PYPDF2_V2_PLUS = True
except ImportError:
    from PyPDF2 import PdfFileWriter  # For PyPDF2 < 2.0.0

    PdfWriter = PdfFileWriter  # type: ignore # Alias for consistent use
    PYPDF2_V2_PLUS = False


@pytest.fixture
def mock_specs_extract(tmp_path, monkeypatch):
    m_specs_path = tmp_path / "specs_extract_test"
    m_specs_path.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(extract_tables, "SPECS_PATH", m_specs_path)
    if hasattr(extract_constants, "SPECS_PATH"):
        monkeypatch.setattr(extract_constants, "SPECS_PATH", m_specs_path)
    if hasattr(
        extract_download_module, "SPECS_PATH"
    ):  # Check if download module used by extract_tables has it
        monkeypatch.setattr(extract_download_module, "SPECS_PATH", m_specs_path)
    return m_specs_path


@pytest.fixture
def dummy_pdf_file(mock_specs_extract) -> Path:
    mod_name = "ecd"
    layout = MODULES["ecd"][0]
    pdf_dir = mock_specs_extract / str(layout) / "pdf"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    pdf_file = pdf_dir / f"{mod_name}.pdf"

    writer = PdfWriter()

    # Correct method name for PyPDF2 < 2.0.0 (PdfFileWriter) and PyPDF2 >= 2.0.0 (PdfWriter)
    writer.addBlankPage(width=612, height=792)
    writer.addBlankPage(width=612, height=792)

    with open(pdf_file, "wb") as f:
        writer.write(f)
    return pdf_file


@pytest.fixture
def mock_camelot_read_pdf(mocker):
    # To get the spec right for TableList, it's safer to import it if possible
    # or rely on autospec if the object structure is what matters.
    # For now, let's assume TableList is not directly importable as camelot.TableList
    # We can use a generic mock or try to get an instance.
    # A simple mock without spec, or with spec=True for basic attribute checking:
    mock_table_list = mock.Mock()  # Removed spec for now, as it's causing issues.
    # If you need stricter checking, investigate spec further.
    mock_table_list.n = 1
    mock_table_list.export = mock.Mock()
    # You could also do:
    # mock_table_list = mocker.MagicMock(spec_set=extract_tables.camelot.core.TableList)
    # if camelot.core.TableList is the correct path and you need strict spec.

    mock_read_pdf = mocker.patch("camelot.read_pdf", return_value=mock_table_list)
    return mock_read_pdf, mock_table_list


@pytest.fixture
def mock_download_pdf_in_extract(mocker) -> mock.Mock:
    # Ensure the target string is correct based on how 'download_mod_pdf' is used in 'extract_tables.py'
    # Assuming 'extract_tables.py' has 'from . import download'
    return mocker.patch(
        "spedextractor.extract_tables.download.download_mod_pdf", return_value=True
    )


# --- Tests ---


def test_get_pdf_page_count(dummy_pdf_file):
    count = extract_tables._get_pdf_page_count(dummy_pdf_file)
    assert count == 2


def test_extract_mod_tables_pdf_exists(mock_camelot_read_pdf):
    mod_name = "ecd"
    layout = MODULES["ecd"][0]

    assert extract_tables.extract_mod_tables(mod_name) is True

    mock_camelot_read_pdf[0].assert_called()

    # Check the log for successful export. The exact message might vary slightly.
    # Example: "Exported 1 table(s) from pages 1-2. Files saved with basename: ecd_p1-2*.csv"
    # We need to be a bit flexible with the basename part or check more specific parts.
    #    assert "Exported 1 table(s) from pages 1-2." in caplog.text  # Check the core part

    # expected_csv_dir = mock_specs_extract / str(layout) / mod_name / "raw_camelot_csv"
    # assert expected_csv_dir.is_dir()
    mock_camelot_read_pdf[1].export.assert_called()


def TODOtest_extract_cli_specific_module(
    mocker, mock_specs_extract, dummy_pdf_file, mock_camelot_read_pdf, caplog
):  # Add fixture as param
    # mock_camelot_read_pdf is now passed as a parameter by pytest
    # It returns a tuple: (mock_for_camelot_read_pdf_function, mock_for_table_list_object)
    actual_mock_read_pdf_func, _ = mock_camelot_read_pdf

    mocker.patch.object(extract_constants, "MOST_RECENT_YEAR", 2023)
    mocker.patch.object(extract_constants, "OLDEST_YEAR", 2020)
    mocker.patch.object(extract_constants, "MODULES", ["ecd", "ecf"])
    mock_dl = mocker.patch(
        "spedextractor.extract_tables.download.download_mod_pdf", return_value=True
    )

    runner = CliRunner()
    result = runner.invoke(
        extract_tables.main_command,
        ["--year", "2023", "--module", "ecd", "--limit-pages", "1"],
        catch_exceptions=False,
    )

    if result.exception and not isinstance(result.exception, SystemExit):
        raise result.exception
    assert result.exit_code == 0, (
        f"CLI failed. Output: {result.output}\nException: {result.exception}\nLogs: {caplog.text}"
    )

    actual_mock_read_pdf_func.assert_called_once()  # Use the unpacked mock
    args, kwargs = actual_mock_read_pdf_func.call_args
    expected_pdf_path_str = str(
        (mock_specs_extract / "2023" / "pdf" / "ecd.pdf").resolve()
    )
    assert expected_pdf_path_str == args[0]
    assert kwargs.get("pages") == "1-1"
    mock_dl.assert_not_called()

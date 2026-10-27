"""Small offline tests for basic project assumptions.

These tests do not call the external translation service.
Run with: pytest
"""
from pathlib import Path


def test_app_file_exists():
    assert Path("app.py").is_file()


def test_requirements_include_main_libraries():
    requirements = Path("requirements.txt").read_text(encoding="utf-8")
    assert "streamlit" in requirements
    assert "deep-translator" in requirements


def test_app_has_translation_ui():
    source = Path("app.py").read_text(encoding="utf-8")
    assert "GoogleTranslator" in source
    assert "Translate" in source
    assert "Download translation" in source

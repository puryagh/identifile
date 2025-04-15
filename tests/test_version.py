"""Tests for the version module."""

import pytest
from src.api.version import version, APP_VERSION, APP_NAME, APP_DESCRIPTION


def test_version_returns_dict():
    """Test that version() returns a dictionary."""
    result = version()
    assert isinstance(result, dict)


def test_version_contains_required_keys():
    """Test that version() returns a dictionary with the required keys."""
    result = version()
    assert "name" in result
    assert "description" in result
    assert "version" in result


def test_version_values():
    """Test that version() returns the expected values."""
    result = version()
    assert result["name"] == APP_NAME
    assert result["description"] == APP_DESCRIPTION
    assert result["version"] == APP_VERSION

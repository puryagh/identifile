"""Tests for the response module."""

import pytest
from src.api.response import IdentificationResponse


def test_identification_response_creation():
    """Test that IdentificationResponse can be created."""
    response = IdentificationResponse(
        method="test",
        mime="text/plain",
        score=0.5,
        description="Test description",
        label="test",
        group="text",
        size=100,
        filename="test.txt",
    )
    assert response.method == "test"
    assert response.mime == "text/plain"
    assert response.score == 0.5
    assert response.description == "Test description"
    assert response.label == "test"
    assert response.group == "text"
    assert response.size == 100
    assert response.filename == "test.txt"


def test_identification_response_score_normalization():
    """Test that IdentificationResponse normalizes scores."""
    # Test score > 1.0
    response = IdentificationResponse(
        method="test",
        mime="text/plain",
        score=1.5,
        description="Test description",
        label="test",
        group="text",
        size=100,
        filename="test.txt",
    )
    assert response.score == 1.0

    # Test score < 0.0
    response = IdentificationResponse(
        method="test",
        mime="text/plain",
        score=-0.5,
        description="Test description",
        label="test",
        group="text",
        size=100,
        filename="test.txt",
    )
    assert response.score == 0.0


def test_identification_response_size_normalization():
    """Test that IdentificationResponse normalizes size."""
    # Test negative size
    response = IdentificationResponse(
        method="test",
        mime="text/plain",
        score=0.5,
        description="Test description",
        label="test",
        group="text",
        size=-100,
        filename="test.txt",
    )
    assert response.size == 0.0

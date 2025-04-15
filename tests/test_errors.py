"""Tests for the errors module."""

import pytest
from fastapi import status
from src.api.errors import (
    FileProcessingError,
    FileTypeError,
    FileSizeError,
    MissingFileError,
    create_error_response,
)


def test_file_processing_error():
    """Test that FileProcessingError is created correctly."""
    error = FileProcessingError()
    assert error.status_code == status.HTTP_400_BAD_REQUEST
    assert error.detail == "Error processing file"

    error = FileProcessingError("Custom error message", status.HTTP_500_INTERNAL_SERVER_ERROR)
    assert error.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert error.detail == "Custom error message"


def test_file_type_error():
    """Test that FileTypeError is created correctly."""
    error = FileTypeError()
    assert error.status_code == status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    assert error.detail == "Unsupported file type"

    error = FileTypeError("Custom error message")
    assert error.status_code == status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    assert error.detail == "Custom error message"


def test_file_size_error():
    """Test that FileSizeError is created correctly."""
    error = FileSizeError()
    assert error.status_code == status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
    assert error.detail == "File size exceeds the limit"

    error = FileSizeError("Custom error message")
    assert error.status_code == status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
    assert error.detail == "Custom error message"


def test_missing_file_error():
    """Test that MissingFileError is created correctly."""
    error = MissingFileError()
    assert error.status_code == status.HTTP_400_BAD_REQUEST
    assert error.detail == "No file provided"

    error = MissingFileError("Custom error message")
    assert error.status_code == status.HTTP_400_BAD_REQUEST
    assert error.detail == "Custom error message"


def test_create_error_response():
    """Test that create_error_response returns the expected dictionary."""
    response = create_error_response(
        status.HTTP_400_BAD_REQUEST, "Error message", "ErrorType"
    )
    assert response["error"]["status_code"] == status.HTTP_400_BAD_REQUEST
    assert response["error"]["message"] == "Error message"
    assert response["error"]["type"] == "ErrorType"

    # Test with default error type
    response = create_error_response(status.HTTP_400_BAD_REQUEST, "Error message")
    assert response["error"]["status_code"] == status.HTTP_400_BAD_REQUEST
    assert response["error"]["message"] == "Error message"
    assert response["error"]["type"] == "UnknownError"

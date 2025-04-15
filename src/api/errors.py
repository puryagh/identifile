"""
Error handling module for the IdentiFile API.

This module defines custom exceptions and error handlers for the API.
"""

from fastapi import HTTPException, status
from typing import Dict, Any, Optional


class FileProcessingError(HTTPException):
    """Exception raised when there's an error processing a file."""

    def __init__(
        self,
        detail: str = "Error processing file",
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ):
        super().__init__(status_code=status_code, detail=detail)


class FileTypeError(FileProcessingError):
    """Exception raised when the file type is not supported."""

    def __init__(
        self,
        detail: str = "Unsupported file type",
        status_code: int = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    ):
        super().__init__(detail=detail, status_code=status_code)


class FileSizeError(FileProcessingError):
    """Exception raised when the file size exceeds the limit."""

    def __init__(
        self,
        detail: str = "File size exceeds the limit",
        status_code: int = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
    ):
        super().__init__(detail=detail, status_code=status_code)


class MissingFileError(FileProcessingError):
    """Exception raised when no file is provided."""

    def __init__(
        self,
        detail: str = "No file provided",
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ):
        super().__init__(detail=detail, status_code=status_code)


def create_error_response(
    status_code: int, message: str, error_type: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a standardized error response.

    Args:
        status_code: HTTP status code
        message: Error message
        error_type: Type of error

    Returns:
        Dict containing error details
    """
    return {
        "error": {
            "status_code": status_code,
            "message": message,
            "type": error_type or "UnknownError",
        }
    }

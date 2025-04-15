"""File identification module for the IdentiFile API.

This module provides functions for identifying files using standard methods
and Google's Magika AI.

Copyright (C) 2023 IdentiFile Contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

import logging
import mimetypes
from typing import Optional

from magika import Magika
from magika.types import MagikaResult
from fastapi import UploadFile, File

from src.api.response import IdentificationResponse
from src.api.errors import FileProcessingError, FileTypeError, FileSizeError

# Configure logging
logger = logging.getLogger("identifile.identify")

# Constants
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB


def _check_file_size(file: UploadFile) -> None:
    """Check if the file size is within limits.

    Args:
        file: The uploaded file to check

    Raises:
        FileSizeError: If the file size exceeds the limit
    """
    if file.size and file.size > MAX_FILE_SIZE:
        logger.warning(f"File size {file.size} exceeds limit of {MAX_FILE_SIZE}")
        raise FileSizeError(f"File size exceeds the limit of {MAX_FILE_SIZE / (1024 * 1024):.1f} MB")


def _get_file_extension(filename: str) -> Optional[str]:
    """Extract file extension from filename.

    Args:
        filename: The name of the file

    Returns:
        The file extension without the dot, or None if no extension
    """
    if not filename or '.' not in filename:
        return None
    return filename.rsplit('.', 1)[1].lower()


def identify(file: UploadFile = File(...)) -> IdentificationResponse:
    """
    Identifies the given file using standard header detection.

    Parameters:
    - file (UploadFile): The file to be identified.

    Returns:
    - IdentificationResponse: An object containing the identification results.

    Raises:
    - FileProcessingError: If there's an error processing the file.
    - FileSizeError: If the file size exceeds the limit.
    """
    try:
        _check_file_size(file)

        # Get file extension and try to determine mime type
        extension = _get_file_extension(file.filename)
        mime_type = file.content_type or (mimetypes.guess_type(file.filename)[0] if extension else None) or "application/octet-stream"

        # Try to determine file type group from mime type
        group = mime_type.split('/')[0] if '/' in mime_type else ""

        # Create a description based on mime type
        description = f"{mime_type} file"

        logger.info(f"Standard identification: {file.filename} -> {mime_type}")

        return IdentificationResponse(
            method="identify",
            mime=mime_type,
            score=1.0 if file.content_type else 0.7,  # Higher confidence if content_type was provided
            description=description,
            label=extension or "",
            group=group,
            size=file.size,
            filename=file.filename
        )
    except FileSizeError:
        # Re-raise FileSizeError to be handled by the exception handler
        raise
    except Exception as e:
        logger.error(f"Error in standard identification: {str(e)}")
        raise FileProcessingError(f"Error identifying file: {str(e)}")


def ai_identify(file: UploadFile = File(...)) -> IdentificationResponse:
    """
    Identifies the given file using Google's Magika AI.

    Parameters:
    - file (UploadFile): The file to be identified.

    Returns:
    - IdentificationResponse: An object containing the identification results.

    Raises:
    - FileProcessingError: If there's an error processing the file.
    - FileSizeError: If the file size exceeds the limit.
    """
    try:
        _check_file_size(file)

        # Reset file position to beginning
        file.file.seek(0)

        # Initialize Magika and identify the file
        magika = Magika()
        file_content = file.file.read()

        if not file_content:
            logger.warning(f"Empty file content for {file.filename}")
            raise FileProcessingError("Empty file content")

        result: MagikaResult = magika.identify_bytes(file_content)

        logger.info(f"AI identification: {file.filename} -> {result.output.mime_type} (score: {result.output.score:.2f})")

        return IdentificationResponse(
            method="ai_identify",
            mime=result.output.mime_type,
            score=result.output.score,
            description=result.output.description,
            label=result.output.ct_label,
            group=result.output.group,
            size=file.size,
            filename=file.filename
        )
    except FileSizeError:
        # Re-raise FileSizeError to be handled by the exception handler
        raise
    except Exception as e:
        logger.error(f"Error in AI identification: {str(e)}")
        raise FileProcessingError(f"Error identifying file with AI: {str(e)}")

"""Response models for the IdentiFile API.

This module defines the response models used by the API.

Copyright (C) 2023 IdentiFile Contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class IdentificationResponse:
    """
    A class representing the response of a file identification process.

    Attributes:
        method (str): The method used for identification (e.g., "identify" or "ai_identify").
        mime (str): The MIME type of the identified file (e.g., "image/jpeg").
        score (float): The confidence score of the identification (0.0 to 1.0).
        description (str): A human-readable description of the file type.
        label (str): A short label for the file type (e.g., "jpeg", "pdf").
        group (str): The group to which the file type belongs (e.g., "image", "document").
        size (float): The size of the file in bytes.
        filename (str): The original filename of the uploaded file.
    """

    method: str
    mime: str
    score: float
    description: str
    label: str
    group: str
    size: float
    filename: str

    def __post_init__(self) -> None:
        """Validate and normalize the response data."""
        # Ensure score is between 0 and 1
        self.score = max(0.0, min(1.0, self.score))

        # Ensure size is not negative
        self.size = max(0.0, self.size)

"""Version information for the IdentiFile API.

This module provides version information for the API.

Copyright (C) 2023 IdentiFile Contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

from typing import Dict, Any

# Application version
APP_VERSION: str = "v1.0.0"

# Application name
APP_NAME: str = "IdentiFile"

# Application description
APP_DESCRIPTION: str = "REST API for identifying file types based on content using Google Magika AI or standard file header detection."


def version() -> Dict[str, Any]:
    """
    Returns a dictionary containing information about the application's version.

    Returns:
        Dict[str, Any]: A dictionary with keys "name", "description", and "version".
    """
    return {
        "name": APP_NAME,
        "description": APP_DESCRIPTION,
        "version": APP_VERSION,
    }

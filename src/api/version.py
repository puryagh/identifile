APP_VERSION: str = "v1.0.0"


def version() -> dict:
    """
    Returns a dictionary containing information about the application's version.

    Returns:
        dict: A dictionary with keys "name", "description", and "version".
              The values for "name" and "description" are hardcoded.
              The value for "version" is obtained from the global variable `APP_VERSION`.
    """
    return {
        "name": "identifile",
        "description": "Rest API for identifying submitted file type by it content.",
        "version": APP_VERSION,
    }

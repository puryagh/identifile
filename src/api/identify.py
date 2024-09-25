from magika import Magika
from fastapi import UploadFile, File

from src.api.response import IdentificationResponse


def identify(file: UploadFile = File(...)) -> IdentificationResponse:
    """
    Identifies the given file.

    Parameters:
    - file (UploadFile): The file to be identified.

    Returns:
    - IdentificationResponse: An object containing the identification results with the following attributes:
        - method (str): The method used for identification.
        - mime (str): The MIME type of the file.
        - score (float): The identification score.
        - description (str): The description of the file content type.
        - label (str): The label of the file content type.
        - group (str): The group of the file content type.
        - size_kb (float): The size of the file in kilobytes.
    """
    return IdentificationResponse(
        method="identify",
        mime=file.content_type,
        score=0.0,
        description="",
        label="",
        group="",
        size=file.size,
        filename=file.filename
    )


def ai_identify(file: UploadFile = File(...)) -> IdentificationResponse:
    """
    Identifies the given file using AI.

    Parameters:
    - file (UploadFile): The file to be identified.

    Returns:
    - IdentificationResponse: An object containing the identification results with the following attributes:
        - method (str): The method used for identification.
        - mime (str): The MIME type of the file.
        - score (float): The identification score.
        - description (str): The description of the file.
        - label (str): The label of the file content type.
        - group (str): The group of the file content type.
        - size_kb (float): The size of the file in kilobytes.
    """

    magika = Magika()
    result = magika.identify_bytes(file.file.read())

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

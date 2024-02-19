from dataclasses import dataclass


@dataclass
class IdentificationResponse:
    """
    A class representing the response of an identification process.

    Attributes:
        method (str): The method used for identification.
        mime (str): The MIME type of the identified object.
        score (float): The confidence score of the identification.
        description (str): A description of the identified object.
        label (str): The label assigned to the identified object.
        group (str): The group to which the identified object belongs.
        size_kb (float): The size of the identified object in kilobytes.
    """

    method: str
    mime: str
    score: float
    description: str
    label: str
    group: str
    size_kb: float

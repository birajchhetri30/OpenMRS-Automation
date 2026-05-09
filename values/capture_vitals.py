from dataclasses import dataclass


@dataclass
class CaptureVitals:
    """
    Data class for the CAPTURE_VITALS keyword.
    """
    patient_identifier: str

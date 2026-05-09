from typing import Any, Callable
from values.login_info import LoginInfo
from values.register_patient import RegisterPatient
from values.capture_vitals import CaptureVitals
from dataclasses import dataclass

@dataclass(frozen=True)
class KeywordData:
    data_type: Any | None
    log_when_executed: Callable[[Any], str]


class Keywords:
    LOGIN = KeywordData(
        data_type=LoginInfo,
        log_when_executed=lambda login_info: (
            f"Login with username: {login_info.username} and location: {login_info.location}"
        )
    )

    LOGOUT = KeywordData(
        data_type=None,
        log_when_executed=lambda _: "Logout from the application"
    )

    TO_REGISTER_PATIENT_PAGE = KeywordData(
        data_type=None,
        log_when_executed=lambda _: "Navigate to the Register Patient page"
    )

    REGISTER_PATIENT = KeywordData(
        data_type=RegisterPatient,
        log_when_executed=lambda register_patient: f"Register a new patient: {repr(register_patient)}"
    )

    FIND_PATIENT_RECORD = KeywordData(
        data_type=None,
        log_when_executed=lambda _: "Navigate to the Find Patient Record screen"
    )

    CAPTURE_VITALS = KeywordData(
        data_type=CaptureVitals,
        log_when_executed=lambda capture_vitals: f"Capture vitals for patient: {capture_vitals.patient_identifier}"
    )

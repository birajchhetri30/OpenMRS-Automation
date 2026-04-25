from typing import Any, Callable
from values.login_info import LoginInfo
from values.register_patient import RegisterPatient
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

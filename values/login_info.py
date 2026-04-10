from dataclasses import dataclass
from values.location import Location

@dataclass
class LoginInfo:
    """
    Data class for the LOGIN keyword.
    """
    username: str
    password: str
    location: Location

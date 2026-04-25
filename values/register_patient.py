from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class RelationshipType(Enum):
    DOCTOR = "Doctor"
    SIBLING = "Sibling"
    PARENT = "Parent"
    AUNT_UNCLE = "Aunt/Uncle"
    SUPERVISOR = "Supervisor"
    PATIENT = "Patient"
    CHILD = "Child"
    NIECE_NEPHEW = "Niece/Nephew"
    SUPERVISEE = "Supervisee"

@dataclass
class RegisterPatient:
    """
    Data class representing the information required to register a patient in the OpenMRS application.
    """
    given_name: str
    family_name: str
    gender: Gender
    birthday_day: int
    birthday_month: int
    birthday_year: int
    address1: str
    address2: str
    city: str
    state: str
    country: str
    postal_code: str
    phone_number: str
    relationship_type: RelationshipType
    
    middle_name: str = None


    def __repr__(self) -> str:
        return (
            f"RegisterPatient(given_name='{self.given_name}', "
            f"middle_name='{self.middle_name}', "
            f"family_name='{self.family_name}', "
            f"gender='{self.gender}', "
            f"birthday_day={self.birthday_day}, "
            f"birthday_month={self.birthday_month}, "
            f"birthday_year={self.birthday_year}, "
            f"address1='{self.address1}', "
            f"address2='{self.address2}', "
            f"city='{self.city}', "
            f"state='{self.state}', "
            f"country='{self.country}', "
            f"postal_code='{self.postal_code}', "
            f"phone_number='{self.phone_number}', "
            f"relationship_type='{self.relationship_type}')"
        )
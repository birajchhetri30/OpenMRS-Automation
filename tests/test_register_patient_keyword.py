import pytest
from keyword_core.keyword_execution import Execute
from keyword_core.keywords import Keywords
from keyword_core.page_provider import get_page
from values.location import Location
from values.login_info import LoginInfo
from values.register_patient import Gender, RegisterPatient, RelationshipType

def test_register_patient_keyword():
    # Arrange: Set up test data for registering a patient
    username = "admin"
    password = "Admin123"

    login_info = LoginInfo(
        username=username,
        password=password,
        location=Location.LABORATORY
    )

    patient_info = RegisterPatient(
        given_name="John",
        middle_name="A",
        family_name="Doe",
        gender=Gender.MALE,
        birthday_day=15,
        birthday_month=12,
        birthday_year=2001,
        address1="123 Main St",
        address2="Apartment 4B",
        city="Anytown",
        state="State",
        country="Country",
        postal_code="12345",
        phone_number="9841234567",
        relationship_type=RelationshipType.CHILD
    )

    Execute(Keywords.LOGIN, login_info)
    Execute(Keywords.TO_REGISTER_PATIENT_PAGE)

    # Act: Execute the register patient keyword
    Execute(Keywords.REGISTER_PATIENT, patient_info)
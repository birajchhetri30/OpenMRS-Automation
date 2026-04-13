import pytest
from keyword_core.keyword_execution import Execute
from keyword_core.keywords import Keywords
from values.location import Location
from values.login_info import LoginInfo
from keyword_core.page_provider import get_page

@pytest.mark.parametrize("location", [
    Location.LABORATORY,
    Location.ISOLATION_WARD,
    Location.INPATIENT_WARD,
    Location.OUTPATIENT_CLINIC,
    Location.PHARMACY,
    Location.REGISTRATION_DESK,
])
def test_login_keyword(location):
    # Arrange: Set up test data
    username = "admin"
    password = "Admin123"

    login_info = LoginInfo(
        username=username,
        password=password,
        location=location
    )

    # Act: Perform the login
    Execute(Keywords.LOGIN, login_info)

    # Assert: Verify login was successful (e.g., check if redirected to home page)
    page = get_page()
    assert "home.page" in page.url.lower(), f"Expected to be on OpenMRS page after login, but URL is {page.url}"
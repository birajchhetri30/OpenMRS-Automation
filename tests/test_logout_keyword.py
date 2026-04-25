import pytest
from keyword_core.keyword_execution import Execute
from keyword_core.keywords import Keywords
from values import login_info
from values.location import Location
from values.login_info import LoginInfo
from keyword_core.page_provider import get_page


def test_logout_keyword():
    # Arrange: Perform the login
    username = "admin"
    password = "Admin123"
    location = Location.LABORATORY

    login_info = LoginInfo(
        username=username,
        password=password,
        location=location
    )

    Execute(Keywords.LOGIN, login_info)

    # Act: Perform the logout
    Execute(Keywords.LOGOUT)

    # Assert: Verify logout was successful (e.g., check if redirected to login page)
    page = get_page()
    assert "login.htm" in page.url.lower(), f"Expected to be on login page after logout, but URL is {page.url}"
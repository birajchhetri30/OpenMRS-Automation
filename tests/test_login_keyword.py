from keyword_core.keyword_execution import Execute
from keyword_core.keywords import Keywords
from values.location import Location
from values.login_info import LoginInfo

def test_login_keyword():
    username = "admin"
    password = "Admin123"
    location = Location.LABORATORY

    login_info = LoginInfo(
        username=username,
        password=password,
        location=location
    )

    Execute(Keywords.LOGIN, login_info)

if __name__ == "__main__":
    test_login_keyword()
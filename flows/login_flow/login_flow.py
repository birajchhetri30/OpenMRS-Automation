from screens.login.login_screen import LoginScreen
from values.location import Location
from keyword_core.page_provider import get_page
from playwright.sync_api import Page


class LoginFlow:
    def __init__(self):
        self.page = get_page()
        self.login_screen = LoginScreen(self.page)
    
    def perform_login(self, username: str, password: str, location: Location) -> None:
        self.page.goto("https://o2.openmrs.org/openmrs/login.htm")
        self.login_screen.username_field.fill(username)
        self.login_screen.password_field.fill(password)
        
        if location == Location.INPATIENT_WARD:
            self.login_screen.inpatient_ward_button.click()
        elif location == Location.ISOLATION_WARD:
            self.login_screen.isolation_ward_button.click()
        elif location == Location.LABORATORY:
            self.login_screen.laboratory_button.click()
        elif location == Location.OUTPATIENT_CLINIC:
            self.login_screen.outpatient_clinic_button.click()
        elif location == Location.PHARMACY:
            self.login_screen.pharmacy_button.click()
        elif location == Location.REGISTRATION_DESK:
            self.login_screen.registration_desk_button.click()
        
        self.login_screen.login_button.click()


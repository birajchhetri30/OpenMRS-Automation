from playwright.sync_api import Locator, Page


class LoginScreen:
    _USERNAME_FIELD_ID = '#username'
    _PASSWORD_FIELD_ID = '#password'
    _INPATIENT_WARD_BUTTON_ID = '#Inpatient Ward'
    _ISOLATION_WARD_BUTTON_ID = '#Isolation Ward'
    _LABORATORY_BUTTON_ID = '#Laboratory'
    _OUTPATIENT_CLINIC_BUTTON_ID = '#Outpatient Clinic'
    _PHARMACY_BUTTON_ID = '#Pharmacy'
    _REGISTRATION_DESK_BUTTON_ID = '#Registration Desk'
    _LOGIN_BUTTON_ID = '#loginButton'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_field = self.page.locator(self._USERNAME_FIELD_ID)
        self.password_field = self.page.locator(self._PASSWORD_FIELD_ID)
        self.inpatient_ward_button = self.page.locator(self._INPATIENT_WARD_BUTTON_ID)
        self.isolation_ward_button = self.page.locator(self._ISOLATION_WARD_BUTTON_ID)
        self.laboratory_button = self.page.locator(self._LABORATORY_BUTTON_ID)
        self.outpatient_clinic_button = self.page.locator(self._OUTPATIENT_CLINIC_BUTTON_ID)
        self.pharmacy_button = self.page.locator(self._PHARMACY_BUTTON_ID)
        self.registration_deck_button = self.page.locator(self._REGISTRATION_DESK_BUTTON_ID)
        self.login_button = self.page.locator(self._LOGIN_BUTTON_ID)
 
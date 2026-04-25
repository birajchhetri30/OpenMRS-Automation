from playwright.sync_api import Page

class HomeScreen:
    # _FIND_PATIENT_RECORD_BUTTON_ID = ''
    # _ACTIVE_VISITS_BUTTON_ID = ''
    # _CAPTURE_VITALS_BUTTON_ID = ''
    _REGISTER_PATIENT_BUTTON_ID = 'referenceapplication-registrationapp-registerPatient-homepageLink-referenceapplication-registrationapp-registerPatient-homepageLink-extension'
    # _APPOINTMENT_SCHEDULING_BUTTON_ID = ''
    # _REPORTS_BUTTON_ID = ''
    # _DATA_MANAGEMENT_BUTTON_ID = ''
    # _CONFIGURE_METADATA_BUTTON_ID = ''
    # _SYSTEM_ADMINISTRATION_BUTTON_ID = ''

    _LOGOUT_BUTTON_ID = '.nav-item.logout'

    def __init__(self, page: Page):
        self.page = page
        # self.find_patient_record_button = self.page.locator(self._FIND_PATIENT_RECORD_BUTTON_ID)
        # self.active_visits_button = self.page.locator(self._ACTIVE_VISITS_BUTTON_ID)
        # self.capture_vitals_button = self.page.locator(self._CAPTURE_VITALS_BUTTON_ID)
        self.register_patient_button = self.page.locator(self._REGISTER_PATIENT_BUTTON_ID)
        # self.appointment_scheduling_button = self.page.locator(self._APPOINTMENT_SCHEDULING_BUTTON_ID)
        # self.reports_button = self.page.locator(self._REPORTS_BUTTON_ID)
        # self.data_management_button = self.page.locator(self._DATA_MANAGEMENT_BUTTON_ID)
        # self.configure_metadata_button = self.page.locator(self._CONFIGURE_METADATA_BUTTON_ID)
        # self.system_administration_button = self.page.locator(self._SYSTEM_ADMINISTRATION_BUTTON_ID)
        self.logout_button = self.page.locator(self._LOGOUT_BUTTON_ID)
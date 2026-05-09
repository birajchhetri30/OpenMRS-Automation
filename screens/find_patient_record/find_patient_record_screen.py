from playwright.sync_api import Page


class FindPatientRecordScreen:
    # TODO: Fill in selectors
    # _SEARCH_FIELD_ID = ''
    # _SEARCH_BUTTON_ID = ''
    # _PATIENT_RESULT_ID = ''

    def __init__(self, page: Page):
        self._page = page
        # self.search_field = self._page.locator(self._SEARCH_FIELD_ID)
        # self.search_button = self._page.locator(self._SEARCH_BUTTON_ID)
        # self.patient_result = self._page.locator(self._PATIENT_RESULT_ID)

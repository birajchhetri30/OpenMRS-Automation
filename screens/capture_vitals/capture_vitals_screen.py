from playwright.sync_api import Page


class CaptureVitalsScreen:
    # TODO: Fill in selectors
    # _PATIENT_SEARCH_FIELD_ID = ''
    # _PATIENT_LIST_RESULT_ID = ''
    # _VITALS_FIELD_ID = ''
    # _SUBMIT_BUTTON_ID = ''

    def __init__(self, page: Page):
        self._page = page
        # self.patient_search_field = self._page.locator(self._PATIENT_SEARCH_FIELD_ID)
        # self.patient_list_result = self._page.locator(self._PATIENT_LIST_RESULT_ID)
        # self.vitals_field = self._page.locator(self._VITALS_FIELD_ID)
        # self.submit_button = self._page.locator(self._SUBMIT_BUTTON_ID)

from playwright.sync_api import Page

class RegisterPatientScreen:
    _GIVEN_NAME_FIELD_ID = '[name="givenName"]'
    _MIDDLE_NAME_FIELD_ID = '[name="middleName"]'
    _FAMILY_NAME_FIELD_ID = '[name="familyName"]'

    _GENDER_SELECT_ID = "#gender-field"

    _BIRTHDAY_FIELD_ID = "#birthdateDay-field"
    _BIRTHMONTH_DROPDOWN_ID = "#birthdateMonth-field"
    _BIRTHYEAR_FIELD_ID = "#birthdateYear-field"

    _ADDRESS1_FIELD_ID = "#address1"
    _ADDRESS2_FIELD_ID = "#address2"
    _CITY_FIELD_ID = "#cityVillage"
    _STATE_FIELD_ID = "#stateProvince"
    _COUNTRY_FIELD_ID = "#country"
    _POSTAL_CODE_FIELD_ID = "#postalCode"

    _PHONE_NUMBER_FIELD_ID = '[name="phoneNumber"]'

    _RELATIONSHIP_TYPE_DROPDOWN_ID = "#relationship_type"
    # PERSON_NAME_FIELD_ID = ''
    
    _NEXT_BUTTON_ID = '#next-button'
    _PREV_BUTTON_ID = '#prev-button'
    _CONFIRM_BUTTON_ID = '#submit'
    _CANCEL_BUTTON_ID = '#cancelSubmission'

    def __init__(self, page: Page):
        self._page = page
        self.given_name_field = self._page.locator(self._GIVEN_NAME_FIELD_ID)
        self.middle_name_field = self._page.locator(self._MIDDLE_NAME_FIELD_ID)
        self.family_name_field = self._page.locator(self._FAMILY_NAME_FIELD_ID)
        self.gender_select = self._page.locator(self._GENDER_SELECT_ID)
        self.birthday_field = self._page.locator(self._BIRTHDAY_FIELD_ID)
        self.birthmonth_dropdown = self._page.locator(self._BIRTHMONTH_DROPDOWN_ID)
        self.birthyear_field = self._page.locator(self._BIRTHYEAR_FIELD_ID)
        self.address1_field = self._page.locator(self._ADDRESS1_FIELD_ID)
        self.address2_field = self._page.locator(self._ADDRESS2_FIELD_ID)
        self.city_field = self._page.locator(self._CITY_FIELD_ID)
        self.state_field = self._page.locator(self._STATE_FIELD_ID)
        self.country_field = self._page.locator(self._COUNTRY_FIELD_ID)
        self.postal_code_field = self._page.locator(self._POSTAL_CODE_FIELD_ID)
        self.phone_number_field = self._page.locator(self._PHONE_NUMBER_FIELD_ID)
        self.relationship_type_dropdown = self._page.locator(self._RELATIONSHIP_TYPE_DROPDOWN_ID)
        self.next_button = self._page.locator(self._NEXT_BUTTON_ID)
        self.prev_button = self._page.locator(self._PREV_BUTTON_ID)
        self.confirm_button = self._page.locator(self._CONFIRM_BUTTON_ID)
        self.cancel_button = self._page.locator(self._CANCEL_BUTTON_ID)
from screens.register_patient.register_patient_screen import RegisterPatientScreen
from keyword_core.page_provider import get_page
from values.register_patient import Gender, RegisterPatient

class RegisterPatientFlow:
    def __init__(self):
        self.page = get_page()
        self.register_patient_screen = RegisterPatientScreen(self.page)
    
    def register_patient(self, register_patient: RegisterPatient):
        self.register_patient_screen.given_name_field.fill(register_patient.given_name)
        self.register_patient_screen.family_name_field.fill(register_patient.family_name)
        self.register_patient_screen.middle_name_field.fill(register_patient.middle_name)
        self.register_patient_screen.next_button.click()

        self.register_patient_screen.gender_select.select_option(register_patient.gender.value)
        self.register_patient_screen.next_button.click()

        self.register_patient_screen.birthday_field.fill(str(register_patient.birthday_day))
        self.register_patient_screen.birthmonth_dropdown.select_option(index=register_patient.birthday_month - 1)
        self.register_patient_screen.birthyear_field.fill(str(register_patient.birthday_year))
        self.register_patient_screen.next_button.click()

        self.register_patient_screen.address1_field.fill(register_patient.address1)
        self.register_patient_screen.address2_field.fill(register_patient.address2)
        self.register_patient_screen.city_field.fill(register_patient.city)
        self.register_patient_screen.state_field.fill(register_patient.state)
        self.register_patient_screen.country_field.fill(register_patient.country)
        self.register_patient_screen.postal_code_field.fill(register_patient.postal_code)
        self.register_patient_screen.next_button.click()

        self.register_patient_screen.phone_number_field.fill(register_patient.phone_number)
        self.register_patient_screen.next_button.click()

        self.register_patient_screen.relationship_type_dropdown.select_option(register_patient.relationship_type.value)
        self.register_patient_screen.next_button.click()

        self.register_patient_screen.confirm_button.click()
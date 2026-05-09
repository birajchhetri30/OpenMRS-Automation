from screens.find_patient_record.find_patient_record_screen import FindPatientRecordScreen
from keyword_core.page_provider import get_page


class FindPatientRecordFlow:
    def __init__(self):
        self.page = get_page()
        self.find_patient_record_screen = FindPatientRecordScreen(self.page)

    def find_patient_record(self):
        pass  # TODO: Implement navigation to the Find Patient Record screen

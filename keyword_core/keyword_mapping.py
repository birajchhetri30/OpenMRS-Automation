from flows.register_patient.register_patient_flow import RegisterPatientFlow
from flows.find_patient_record.find_patient_record_flow import FindPatientRecordFlow
from flows.capture_vitals.capture_vitals_flow import CaptureVitalsFlow
from keyword_core.keywords import Keywords, KeywordData
from values.login_info import LoginInfo
from values.capture_vitals import CaptureVitals
from flows.login_flow.login_flow import LoginFlow
from flows.home_flow.home_flow import HomeFlow
from typing import Callable


class KeywordMapping:
    def __init__(self):
        self._mapping_dict: dict[KeywordData, Callable] = {}
        self._mapping()
    
    def _mapping(self):
        self._mapping_dict[Keywords.LOGIN] = self._login
        self._mapping_dict[Keywords.LOGOUT] = self._logout
        self._mapping_dict[Keywords.TO_REGISTER_PATIENT_PAGE] = self._to_register_patient_page
        self._mapping_dict[Keywords.REGISTER_PATIENT] = self._register_patient
        self._mapping_dict[Keywords.FIND_PATIENT_RECORD] = self._find_patient_record
        self._mapping_dict[Keywords.CAPTURE_VITALS] = self._capture_vitals

    
    def _login(self, login_info: LoginInfo):
        login_flow = LoginFlow()
        login_flow.perform_login(
            username=login_info.username,
            password=login_info.password,
            location=login_info.location
        )
    
    def _logout(self, _ignored_arg):
        home_flow = HomeFlow()
        home_flow.perform_logout()

    def _to_register_patient_page(self, _ignored_arg):
        home_flow = HomeFlow()
        home_flow.home_screen.register_patient_button.click()

    def _register_patient(self, register_patient):
        register_patient_flow = RegisterPatientFlow()
        register_patient_flow.register_patient(register_patient)

    def _find_patient_record(self, _ignored_arg):
        find_patient_record_flow = FindPatientRecordFlow()
        find_patient_record_flow.find_patient_record()

    def _capture_vitals(self, capture_vitals: CaptureVitals):
        capture_vitals_flow = CaptureVitalsFlow()
        capture_vitals_flow.capture_vitals(capture_vitals)

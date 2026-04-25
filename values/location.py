from enum import Enum


class Location(Enum):
    INPATIENT_WARD = 'Inpatient Ward'
    ISOLATION_WARD = 'Isolation Ward'
    LABORATORY = 'Laboratory'
    OUTPATIENT_CLINIC = 'Outpatient Clinic'
    PHARMACY = 'Pharmacy'
    REGISTRATION_DESK = 'Registration Desk'
from dataclasses import dataclass


@dataclass
class Location:
    """
    Enum data class representing the different locations in the OpenMRS application.
    """
    INPATIENT_WARD = 'Inpatient Ward'
    ISOLATION_WARD = 'Isolation Ward'
    LABORATORY = 'Laboratory'
    OUTPATIENT_CLINIC = 'Outpatient Clinic'
    PHARMACY = 'Pharmacy'
    REGISTRATION_DESK = 'Registration Desk'
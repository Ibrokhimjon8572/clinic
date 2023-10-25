from patient import Patient
from clinicexeptions import NoSuchPatient, NoSuchDoctor
from doctor import Doctor

class Clinic:
    def __init__(self) -> None:
        self._patient_list: list[Patient] = []
        self._doctor_list: list[Doctor] = []

    def addpatient(self, patient: Patient):
        self._patient_list.append(patient)
        print('tizimga bemor kiritildi')

    def getpatient(self, ssn):
        for patient in self._patient_list:
            if patient.ssn == ssn:
                return patient
        raise NoSuchPatient(ssn)
    
    def adddoctor(self, doctor: Doctor):
        self._doctor_list.append(doctor)
        print('doctor tizmga qo\'shildi')

    def getdoctor(self, doctor_id):
        for doctor in self._doctor_list:
            if doctor.id == doctor_id:
                return doctor
        raise NoSuchDoctor(doctor_id)
    
    def assignPatientToDoctor(self, patiend_ssn, doctor_id):
        try:
            doctor = self.getdoctor(doctor_id)
        except:
            raise NoSuchDoctor(doctor_id)
        try:
            patient = self.getpatient(patiend_ssn)
        except:
            raise NoSuchPatient(patiend_ssn)
        doctor.addpatient(patiend_ssn)
        patient.setdoctor(doctor_id)

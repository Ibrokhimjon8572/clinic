from patient import Patient
from clinicexeptions import NoSuchPatient, NoSuchDoctor
from doctor import Doctor
from collections import OrderedDict

class Clinic:
    def __init__(self) -> None:
        self._patient_list: list[Patient] = []
        self._doctor_list: list[Doctor] = []

    def addpatient(self, patient: Patient):
        for _patient in self._patient_list:
            if _patient.ssn == patient.ssn:
                print('bunday ssn bemor mavjud')
                return
        self._patient_list.append(patient)
        print('tizimga bemor kiritildi')

    def getpatient(self, ssn):
        for patient in self._patient_list:
            if patient.ssn == ssn:
                return patient
        raise NoSuchPatient(ssn)
    
    def adddoctor(self, doctor: Doctor):
        for _doctor in self._doctor_list:
            if _doctor.ssn == doctor.ssn and _doctor.id == doctor.id:
                print('bunday doctor mavjud')
                return
        self._doctor_list.append(doctor)
        print('doctor tizmga qo\'shildi')

    def getdoctor(self, doctor_id):
        for doctor in self._doctor_list:
            if doctor.id == doctor_id:
                return doctor
        raise NoSuchDoctor(doctor_id)
    
    def assignPatientToDoctor(self, patiend_ssn, doctor_id):
        if self.getdoctor(doctor_id) and self.getpatient(patiend_ssn):
            doctor = self.getdoctor(doctor_id)
            patient = self.getpatient(patiend_ssn)
        doctor.collectpatient(patiend_ssn)
        patient.colletdoctor(doctor_id)

    def idleDoctors(self):
        res = dict()
        for doctor in self._doctor_list:
            if len(doctor.getpatients()) == 0:
                res[doctor.familyasi] = doctor.ismi
        res = OrderedDict(sorted(res.items()))
        return dict(res)
    
    def busyDoctors(self):
        ortbemor = 0
        for doctor in self._doctor_list:
            ortbemor += len(doctor.getpatients())
        res = dict()
        for doctor in self._doctor_list:
            if len(doctor.getpatients()) >= ortbemor/len(self._doctor_list):
                res[doctor.familyasi] = doctor.ismi
        res = OrderedDict(sorted(res.items()))
        return dict(res)
    
    def doctorsByNumPatients(self):
        res = {}
        for doctor in self._doctor_list:
            res[doctor.ismi] = len(doctor.getpatients)
        res = sorted(res.items(), key=lambda x:x[1], reverse=True)
        return res

    def countPatientsPerSpecialization(self):
        res = {}
        for doctor in self._doctor_list:
            res[doctor.speciality] = len(doctor.getpatients)
        res = sorted(res.items(), key=lambda x:x[1], reverse=True)
        return res
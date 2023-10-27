from patient import Patient

class Doctor(Patient):
    def __init__(self, ismi, familyasi, ssn, id, speciality) -> None:
        self._id = id
        self._speciality = speciality
        self._patient_list = []
        super().__init__(ismi, familyasi, ssn)
    
    @property
    def speciality(self):
        return self.speciality

    @property
    def ismi(self):
        return self._ismi
    
    @property
    def familyasi(self):
        return self._familyasi

    @property
    def id(self):
        return self._id
    
    @property
    def speciality(self):
        return self._speciality
    
    def collectpatient(self, ssn):
        self._patient_list.append(ssn)
        print('doctorga bemor biriktirildi')

    def getpatients(self):
        return self._patient_list
    
    def __str__(self) -> str:
        return super().__str__()
    

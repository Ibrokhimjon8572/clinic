from patient import Patient

class Doctor(Patient):
    def __init__(self, ismi, familyasi, ssn, id, speciality) -> None:
        self._id = id
        self._speciality = speciality
        self._patient_list: list[Patient] = []
        super().__init__(ismi, familyasi, ssn)

    @property
    def id(self):
        return self._id
    
    @property
    def speciality(self):
        return self._speciality
    
    def addpatient(self, patient):
        self._patient_list.append(patient)
        print('doctorga patient biriktirildi')

    def getpatients(self):
        return self._patient_list
    
    def __str__(self) -> str:
        return super().__str__()
    

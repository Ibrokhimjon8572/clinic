from doctor import Doctor

class Patient:
    def __init__(self, ismi, familyasi, ssn) -> None:
        self._ismi = ismi
        self._familyasi = familyasi
        self._ssn = ssn
        self._doctor = None

    @property
    def ssn(self):
        return self._ssn
    
    def setdoctor(self, doctor):
        self._doctor = doctor

    def getdoctor(self):
        return self._doctor

    def __str__(self) -> str:
        return self._ismi
class Patient:
    def __init__(self, ismi, familyasi, ssn) -> None:
        self._ismi = ismi
        self._familyasi = familyasi
        self._ssn = ssn
        self._doctor = None

    @property
    def ssn(self):
        return self._ssn

    def getdoctor(self):
        return self._doctor
    
    def colletdoctor(self, doctor_id):
        self._doctor = doctor_id
        print('kasalga doctor biriktirildi')

    def __str__(self) -> str:
        return self._ismi
class NoSuchPatient(Exception):
    def __init__(self, ssn) -> None:
        self._ssn = str(ssn)
        self.message = self._ssn + " raqamlik bemor yo\'q ekan afsuski"
        super().__init__(self.message)

class NoSuchDoctor(Exception):
    def __init__(self, id) -> None:
        self._id = str(id)
        self.message = self._id + " id lik doctor yo\'q ekan afsuski"
        super().__init__(self.message)
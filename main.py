from clinic import Clinic
from patient import Patient
from doctor import Doctor

kasalxona = Clinic()

doctor1 = Doctor('ali', 'valiyev', 123432, 1, 'hirurg')
kasalxona.adddoctor(doctor1)
print(kasalxona.getdoctor(2))
# bemor1 = Patient('ali', 'valiyev', 123432)

# kasalxona.addpatient(bemor1)
# print(kasalxona.getpatient(123432))
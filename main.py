from clinic import Clinic
from patient import Patient
from doctor import Doctor

kasalxona = Clinic()

doctor1 = Doctor('ali', 'valiyev', 10, 11, 'hirurg')
doctor2 = Doctor('ali1', 'valiyev', 11, 12, 'hirurg')
doctor3 = Doctor('ali2', 'aliyev', 12, 13, 'hirurg')
doctor4 = Doctor('ali3', 'faliyev', 13, 14, 'hirurg')
patient1 = Patient('A', 'B', 1)
patient2 = Patient('C', 'D', 2)
kasalxona.adddoctor(doctor1)
kasalxona.adddoctor(doctor2)
kasalxona.adddoctor(doctor3)
kasalxona.adddoctor(doctor4)
# kasalxona.adddoctor(doctor1)
kasalxona.addpatient(patient1)
kasalxona.addpatient(patient2)
# kasalxona.addpatient(patient)

kasalxona.assignPatientToDoctor(2, 11)
print(kasalxona.idleDoctors())
# kasalxona.assignPatientToDoctor(2, 11)

# print(doctor1.getpatients())
# print(patient1.getdoctor())
# print(patient2.getdoctor())
# kasalxona.adddoctor(doctor1)
# print(kasalxona.getdoctor(2))
# bemor1 = Patient('ali', 'valiyev', 123432)

# kasalxona.addpatient(bemor1)
# print(kasalxona.getpatient(123432))
'''
print("This is the database.py file")

print("Python thinks this is called {}".format(__name__))


import bloodcalculator as bc
#from bloodcalculator import HDL_analysis


HDL = 55

HDL_analysis = bc.HDL_analysis(HDL)
print("The HDL analysis is {}".format(HDL_analysis))

bc.generic_input("Other Test")
'''

def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age]
    return new_patient

def main_driver():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 34))
    db.append(create_patient_entry("Bob Boyles", 2, 45))
    db.append(create_patient_entry("Chris Chou", 3, 52))
    print(db)
    print("Get patient Ann")
    mrn_to_find = 4
    found_patient = get_patient_entry(db, mrn_to_find)
    if found_patient is False:
        print("Patient mrn {} not found".format(mrn_to_find))
    else:
        print(found_patient)

def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False

if __name__ == "__main__":
    main_driver()

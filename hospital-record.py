import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Use a service account
cred = credentials.Certificate('patient-data-shar-acbada87cb20.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

#Adding or Updating
# aou = input("Add or Update? ")
# while (aou != "Add") or (aou != "Update"):
#   aou = input("Can only enter either \'Add\' or \'Update\' exactly: ")

# if aou == "Update":
#   update()
# if aou == "Add":
#   add()

# Update Patient Info
def update():
  patient_id = input("Input id of patient to be updated: ")
  collections = ['patient-record', 'patient_bill', 'patient_triage', 'patient_test','patient_visit']
  collection = ''
  isCollection = False
  while not isCollection:
    collection = input("Which collection? Valid choices are 'patient-record', 'patient_bill', 'patient_triage', 'patient_test', or 'patient_visit': ")
    if collection in collections:
      isCollection = True
    else:
      print("Input is NOT a valid collection; try again")

  col_ref = db.collection('patient-record').document(patient_id)
  if collection != 'patient-record':
    doc_id = input("Input id of document within collection '" + collection + "' to be update: ")
    col_ref = db.collection('patient-record').document(patient_id).collection(collection).document(doc_id)

  field = input("Which field in collection '" + collection + "' ? ")
  ui = input("Updated value: ")

  col_ref.update({field: ui})




# Add Patient 
def add():

#patient-record
  print("Input Patient Record Information")

  first_name = input("\tFirst Name: ")
  last_name = input("\tLast Name: ")
  gender = input("\tGender: ")
  marital_status = input("\tMarital Status: ")
  email = input("\tEmail: ")
  SSN = input("\tSSN: ")
  age = input("\tAge: ")
  phone_no = input("\tPhone No: ")
  race = input("\tRace: ")
  resident_address = input("\tResident Address: ")


  doc_ref = db.collection('patient-record').document()
  doc_id = doc_ref.id
  doc_ref.set({
      'patient_id': ''+doc_id,
      'patient_first_name': first_name,
      'patient_last_name': last_name,
      'gender': gender,
      'marital_status': marital_status,
      'email': email,
      'SSN': SSN,
      'age': age,
      'phone_no': phone_no,
      'race': race,
      'resident_address': resident_address,
  })

  #patient_triage

  print("Input Patient Triage Information")

  blood_pressure = input("\tBlood pressure: ")
  heart_beat = input("\tHeart Beat: ")
  sugar_level = input("\tSugar Level: ")
  height = input("\tHeight: ")
  weight = input("\tWeight: ")
  time_of_reg = input("\tTime of Regulation: ")
  comment = input("\tTime of Reg: ")
  other = input("\tOther: ")

  dt = str(datetime.datetime.now())
  triage_ref = doc_ref.collection('patient_triage').document(dt)
  triage_id = triage_ref.id
  triage_ref.set({
      'triage_id': ''+triage_id,
      'blood_pressure': blood_pressure,
      'heart_beat': heart_beat,
      'sugar_level': sugar_level,
      'height': height,
      'weight': weight,
      'time_of_reg': time_of_reg,
      'comment': comment,
      'other': other,
  })

  #patient_test

  print("Input Patient Test Information")

  test_name = input("\tTest Name: ")
  test_description = input("\tTest Description: ")
  return_date = input("\tReturn Date: ")
  comment = input("\tComment: ")
  fee = input("\tFee: ")
  comment = input("\tComment: ")
  other = input("\tOther: ")

  dt = str(datetime.datetime.now())
  test_ref = doc_ref.collection('patient_test').document(dt)
  test_id = test_ref.id
  test_ref.set({
      'test_id': ''+test_id,
      'test_name': test_name,
      'test_description': test_description,
      'return_date': return_date,
      'comment': comment,
      'datetime': dt,
      'fee': fee,
      'other': other,
  })

  # patient bill

  print("Input Patients' Bill Information (example):")

  insurance = input("\tInsurance: ")

  ambulance = input("\tAmbulance charge: ")
  surgery = input("\tSurgery: ")
  treatment = input("\tTreatment")
  advance = input("\tAdvance")

  dt = str(datetime.datetime.now())
  bill_ref = doc_ref.collection('patient_bill').document(dt)
  bill_id = bill_ref.id
  bill_ref.set({
    'bill_id': ''+bill_id,
    'insurace': insurance,
    'charges': {
      'ambulance': ambulance,
      'surgery': surgery,
      'treatment': treatment,
      'advance': advance,
    },
  })


  # patient visit 

  print("Input Patient Visit History Information")
  doctor_name = input("\tDoctor Name: ")
  organization = input("\tOrganization: ")
  visit_notes = input("\tVisit Notes: ")

  dt = str(datetime.datetime.now())
  visit_ref = doc_ref.collection('patient_visit').document(dt)
  visit_id = visit_ref.id
  visit_ref.set({
    'visit_id': ''+visit_id,
    'doctor_name': doctor_name,
    'organization': organization,
    'visit_notes': visit_notes,
  })


'''
python3 -u "/Users/ahnafkhan/Documents/Semester 8/CS Research Capstone/hospital-datasharing-interface/hospital-record.py"
'''

isValidInput = False
aou = ""
while not isValidInput:
  aou = input("Add, Update, Delete, or Retrieve? ")
  if (aou == "Add") or (aou == "Update"):
    isValidInput = True
  else:
    print("Invalid input (Input can only be either \'Add\' or \'Update\')")

if aou == "Add":
  add()
if aou == "Update":
  update()


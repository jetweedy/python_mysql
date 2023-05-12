import json
import pandas as pd

df = pd.read_excel("myfile.xlsx", header=0).fillna('')
#print(df.head())

## Let's create dictionaries for our unique patients and medications.
## We'll key them by the ssn and medication name, respectively
patients = {}
medications = {}
## Then let's just create an list of prescriptions that will hold 
## an array of dictionaries containing medication name and dosage info
## for each prescription:
prescriptions = []

for index, row in df.iterrows():
    if (row["ssn"]):
        if (row["ssn"] not in patients):
            ## Create an entry for the patient and give them an empty list of prescriptions
            patients[row["ssn"]] = {"firstname":row["firstname"], "lastname":row["lastname"]}
    if (row["medication"]):
        if (row["medication"] not in medications):
            ## Create a dictionary entry for the medication
            medications[row["medication"]] = {"medication":row["medication"]}
        prescriptions.append({
                "patient":row["ssn"],
                "medication":row["medication"],
                "dosage":row["dosage"],
            })


## Show that we have unique meds and patients now:
print(json.dumps(medications, indent=2))
print(json.dumps(patients, indent=2))
## And show the list of prescriptions we compiled:
print(json.dumps(prescriptions, indent=2))



## This imports the configuration parser library
import configparser
## This creates an instance of its 'ConfigParser' tool
cfg = configparser.ConfigParser()
## This reads data from 'config.ini' into that 'cfg' variable
cfg.read('config.ini')


## This imports the mysql.connector library:
import mysql.connector
## This creates an instance of a connection using those cfg values:
dbconn = mysql.connector.connect(user=cfg["db"]["user"], 
                                    password=cfg["db"]["password"],
                                    host=cfg["db"]["host"],
                                    database=cfg["db"]["database"])
## This creates a cursor that can run queries against your db connection:
cursor = dbconn.cursor()

## We're going to use the json and pandas libraries for some data and output stuff:
import json
import pandas as pd

## This reads in our excel file:
df = pd.read_excel("myfile.xlsx", header=0).fillna('')
## This would output the first few rows of what we just read in.
## We'll print all 6:
print(df.head(6))

## Let's create dictionaries for our unique patients and medications.
## We'll key them by the ssn and medication name, respectively
patients = {}
medications = {}

## Let's create our three tables (if they don't exist):
sql = "CREATE TABLE IF NOT EXISTS patients (patid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ssn VARCHAR(50), firstname VARCHAR(200), lastname VARCHAR(200));"
cursor.execute(sql)
sql = "CREATE TABLE IF NOT EXISTS medications (medid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, medication VARCHAR(200));"
cursor.execute(sql)
sql = "CREATE TABLE IF NOT EXISTS prescriptions (patid INT, medid INT, dosage VARCHAR(100));"
cursor.execute(sql)

for index, row in df.iterrows():
    if (row["ssn"]):
        if (row["ssn"] not in patients):
            ## Insert the patient into our database table and retrieve the generated ID:
            sql = "INSERT INTO patients (ssn, firstname, lastname) VALUES ('"+str(row["ssn"])+"', '"+row["firstname"]+"', '"+row["lastname"]+"');"
            cursor.execute(sql)
            patid = cursor.lastrowid
            ## Create an entry for the patient and give them an empty list of prescriptions
            ## Include the ID we just inserted for them
            patients[row["ssn"]] = {"patid":patid, "firstname":row["firstname"], "lastname":row["lastname"]}
    if (row["medication"]):
        if (row["medication"] not in medications):
            ## Insert the medication into our database table and retrieve the generated ID:
            sql = "INSERT INTO medications (medication) VALUES ('"+row["medication"]+"');"
            cursor.execute(sql)
            medid = cursor.lastrowid
            ## Create a dictionary entry for the medication
            medications[row["medication"]] = {"medid":medid}
        ## Insert the prescription row using our known patid and medid values for those pat/med indexes:
        patid = patients[row["ssn"]]["patid"]
        medid = medications[row["medication"]]["medid"]
        sql = "INSERT INTO prescriptions (patid, medid, dosage) VALUES ("+str(patid)+", "+str(medid)+", '"+row["dosage"]+"')"
        cursor.execute(sql)

## Commit our queries (so that it's saved for real, and not just in the context of our connection)
dbconn.commit()


## Our data is in the database! Let's prove it:
cursor.execute("SELECT * FROM patients") 
patients = []
for row in cursor.fetchall():
    rowdict = dict(zip([column[0] for column in cursor.description], row))
    patients.append(rowdict)

cursor.execute("SELECT * FROM medications") 
medications = []
for row in cursor.fetchall():
    rowdict = dict(zip([column[0] for column in cursor.description], row))
    medications.append(rowdict)

cursor.execute("SELECT * FROM prescriptions") 
prescriptions = []
for row in cursor.fetchall():
    rowdict = dict(zip([column[0] for column in cursor.description], row))
    prescriptions.append(rowdict)

## Now let's dump it all out in the console as pretty-printed JSON:
print("patients:")
print(json.dumps(patients, indent=2))
print("medications:")
print(json.dumps(medications, indent=2))
print("prescriptions:")
print(json.dumps(prescriptions, indent=2))

## And to clean up, let's drop all three tables
sql = "DROP TABLE prescriptions, medications, patients;"
cursor.execute(sql);
dbconn.commit()


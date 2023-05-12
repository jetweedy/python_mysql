## We'll import a json library so we can neatly display things and serve up json data:
import json

## This imports the configuration parser library
import configparser
## This creates an instance of its 'ConfigParser' tool
cfg = configparser.ConfigParser()
## This reads data from 'config.ini' into that 'cfg' variable
cfg.read('config.ini')
## You can now access variables like: cfg["db"]["user"], etc

## This imports the mysql.connector library:
import mysql.connector
## This creates an instance of a connection using those cfg values:
mydb = mysql.connector.connect(user=cfg["db"]["user"], 
                                    password=cfg["db"]["password"],
                                    host=cfg["db"]["host"],
                                    database=cfg["db"]["database"])
## This creates a cursor that can run queries against your db connection:
cursor = mydb.cursor()

## Now we can run queries using our cursor's 'execute' method:
cursor.execute("CREATE TABLE IF NOT EXISTS testable (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, label VARCHAR(200));")

## We can get certain information about our query, if relevant...

## Most importantly for our purposes...
## ... we can get the last auto ID that was generated.
cursor.execute("INSERT INTO testable(label) VALUES('Label 1')")
print("ID Generated:", cursor.lastrowid)
cursor.execute("INSERT INTO testable(label) VALUES('Label 2')")
print("ID Generated:", cursor.lastrowid)

## We can get rows affected by operations:
myUpdateQuery = "UPDATE testable SET label = 'Label Two' WHERE id = " + str(cursor.lastrowid)
print(myUpdateQuery)
cursor.execute(myUpdateQuery)
print(cursor.rowcount, " record(s) updated")

cursor.execute("SELECT * FROM testable;")
## We COULD use simple this...
#for row in cursor.fetchall():
#    print(row[0], row[1])
## (Notice I'm commenting it out. You can only use fetchall once on a cursor that you've run.)

## But it's a little awkward to have to remember the columns and their indexes
## Let's do something to wrap the results up in a nice array of dictionaries:
results = []
for row in cursor.fetchall():
    ## This line creates a dictionary of the row using column names with values:
    rowdict = dict(zip([column[0] for column in cursor.description], row))
    ## This one appends that dictionary to our array of results
    results.append(rowdict)

## Let's dump our results out as pretty-printed JSON
print("Current data in testable:")
print(json.dumps(results, indent=2))


## Finally we'll just drop our test table:
cursor.execute("DROP TABLE IF EXISTS testable;")
exit()

















"""

#### Let's import a json module so we can create JSON strings from our data later:
import json

#### Let's use the configparser tool to load a 'cfg' dictionary with credentials from our 'config.ini' file:
import configparser
cfg = configparser.ConfigParser()
cfg.read('config.ini')


#### Create a connection to the DB I made you using this code:
from mysql.connector import (connection)
cnx = connection.MySQLConnection(user=cfg["db"]["user"], 
                                    password=cfg["db"]["password"],
                                    host=cfg["db"]["host"],
                                    database=cfg["db"]["database"])

#### Create a 'cursor' to run query/ies through this connection:
cursor = cnx.cursor()

#### Samples:

## Create a table to mess with:
cursor.execute("CREATE TABLE IF NOT EXISTS testable (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, label VARCHAR(200));")

## Insert a label into it:
cursor.execute("INSERT INTO testable (label) VALUES ('A');")
## Commit our change so we get a lastrowid in the cursor
cnx.commit()
print("Inserted Row was given auto-ID", print(cursor.lastrowid))

## Insert a couple more values:
cursor.execute("INSERT INTO testable (label) VALUES ('B'), ('C');")
## Quickly output all those things we selected:
cursor.execute("SELECT * FROM testable;")
for row in cursor:
    print(row)

## Delete one of our labels ('A')
cursor.execute("DELETE FROM testable WHERE (label = 'A');")

## Select the labels again (A will be missing)
## This time we're explicitly asking for what we want, so we know what the items are...
## 0 is id, 1 is label, etc:
cursor.execute("SELECT id, label FROM testable;")
## Create an array of items to build:
items = []
## for each of the rows remaining in our database, add it:
for row in cursor:
    ## Convert our row data into a dictionary/object:
    ## We're using those 0, 1, etc positions that we mentioned above:
    item = {"id":row[0], "label":row[1]}
    ## Append that object/dictionary to our array of items:
    items.append(item)


## Drop the table to clean our test up:
cursor.execute("DROP TABLE testable;")

## Convert our list of items into a JSON string:
output = json.dumps(items)
## Print that JSON:
print(output)

#### Close the connection using this code:
cnx.close()

"""


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
## Insert a couple of labels into it:
cursor.execute("INSERT INTO testable (label) VALUES ('A'), ('B'), ('C');")

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

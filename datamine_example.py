import sys
#!conda install --yes -- prefix {sys.prefix} mysqlclient
#!conda install --yes --prefix {sys.prefix} mysql-connector-python
#!conda install --yes --prefix {sys.prefix} PyMySQL
#!{sys.executable} -m pip install mysql-connector-python
#!{sys.executable} -m pip install mysqlclient
!{sys.executable} -m pip install PyMySQL

import json
import configparser
cfg = configparser.ConfigParser()
cfg.read('config.ini')
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

## https://pypi.org/project/pymysql/

import pymysql.cursors
connection = pymysql.connect(host=cfg["db"]["host"],
                             user=cfg["db"]["user"],
                             password=cfg["db"]["password"],
                             database=cfg["db"]["database"],
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM patients;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

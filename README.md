# python_mysql
Some starter tools for connecting to MySQL using Python

## Fork/Clone this repository
You won't be able to push code up to it, so you'll probably want to fork your own copy and play with it there.

## Install the Python MySQL Connector Module
```
pip install mysql-connector-python
```

## Review this documentation:
https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

## Create a file called 'config.ini' in your copy of this folder
It is ignored in the .gitignore folder, so you can put your passwords and secrets there, and it won't get pushed to github.

## Run the test file
```
python test.py
```
It should create a table, insert some rows, delete a row, read the remaining rows, put the data into an array of dictionary items, and then convert that array to JSON and print it out to the screen.

## Side notes:
This is another tool you can use, but may require installing an additional MySQL ODBC driver:

https://docs.devart.com/odbc/mysql/python.htm


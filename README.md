# python_mysql
Some starter tools for connecting to MySQL using Python

## Get Access to a MySQL Database
If you don't have an existing option, then you can use something like Docker Desktop to run it in a container. There are some quick instructions for that at the bottom.

## Fork/Clone this repository
You won't be able to push code up to it, so you'll probably want to fork your own copy and play with it there.

## Install the Python MySQL Connector Module
```
pip install mysql-connector-python
or
pip install PyMySQL
```

## Review this documentation:
https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

## Create a file called 'config.ini' in your copy of this folder
It is ignored in the .gitignore folder, so you can put your passwords and secrets there, and it won't get pushed to github.

## Run the respective files
```
python _______.py
```
It should create a table, insert some rows, delete a row, read the remaining rows, put the data into an array of dictionary items, and then convert that array to JSON and print it out to the screen.

## Side notes:
This is another tool you can use, but may require installing an additional MySQL ODBC driver:

https://docs.devart.com/odbc/mysql/python.htm


--------------------------------------------------------

# Using MySQL on Docker:

1. Install <a href="https://www.docker.com/products/docker-desktop/" target="_blank">Docker Desktop</a>
2. After opening, look for the Magnifying Glass Search Button at the top.
3. Look for 'mysql'. A standard image should come up at the top.
4. Click the Run button (triangle pointing right)
5. Before running, click Optional Settings, and set a MYSQL_ROOT_PASSWORD of your choise (e.g. 'root') under Environment Variables
    



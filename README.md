Python MySQL Example
======================

Following the tutorial from 
http://zetcode.com/db/mysqlpython/

"This is a Python programming tutorial for the MySQL database. It covers the basics of MySQL programming with Python. It uses the MySQLdb module. The examples were created and tested on Ubuntu Linux."

```
$ sudo apt-get install mysql-server
$ apt-cache search MySQLdb
```


Needed to run this command, otherwise I would get an error when trying to write the "Writers" table.
```
$ pip install MySQL-python
```

Creates testdb, creates user testuser with password, add testdb, grant all privileges to testuser for all tables of testdb;

``` 
$ mysql -u root -p
mysql> SHOW DATABASES;
mysql> CREATE DATABASE testdb;
mysql> CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'test623';
mysql> USE testdb;
mysql> GRANT ALL ON testdb.* TO 'testuser'@'localhost';
mysql> quit;
```

_mysql module
=============
From the tutorial:
"The _mysql module implements the MySQL C API directly. It is not compatible with the Python DB API interface. Generally, the programmers prefer the object oriented MySQLdb module. We will concern ourself with the latter module. Here we present only one small example with the _mysql module."

This runs the script that connects to the db, gets the version, prints the version, then closes the connection.

``` 
$ python _MySQLModuleExample.py 
```

MySQLdb module
==============
This is similar to the above script, but uses the python db API, which is the preferred method of working with db using python as the code is more portable.
``` 
$ python first_example.py 
```


Creating and populating a table
===============================
Creates a table called 'Writers' and adds 5 entries.
``` 
$ python create_and_populate_table.py 
```

Retrieving Data
===============
The first example grabs the data using the fetchall() command, which could be time consuming if the data set is huge.
```
$ python retrieve_data_from_db.py
```

The second example grabs the data one row at a time using the fetchone() command.
```
$ python retrieve_rows_one_by_one.py
```

Using the dictionary cursor
===========================
The default cursor returns data as a tuple of tuples, but the DictCursor can be used and the data is sent in the form of python dictionaries.

```
$ python retrieve_rows_using_dictionary_cursor.py
```

Printing column headers
=======================

Prints the column headers using the .description operator.
```
$ python retrieve_column_headers.py
```

Prepared Statements
===================

Example of a prepared statement, using the ANSI print codes as that is what supported by the MySQLdb.

```
$ python prepared_statements.py
```

Inserting Images
================
Example of putting images into database.
```
$ python insert_images.py
```

Reading Images
==============
Example of reading an image from a database
```
$ python reading_image.py
```

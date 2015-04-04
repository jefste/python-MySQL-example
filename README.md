Python MySQL Example
======================

Following the tutorial from 
http://zetcode.com/db/mysqlpython/

"This is a Python programming tutorial for the MySQL database. It covers the basics of MySQL programming with Python. It uses the MySQLdb module. The examples were created and tested on Ubuntu Linux."

```
sudo apt-get install mysql-server
apt-cache search MySQLdb
```


Needed to run this command, otherwise I would get an error when trying to write the "Writers" table.
```
pip install MySQL-python
```

Creates testdb, creates user testuser with password, add testdb, grant all privileges to testuser for all tables of testdb;

``` 
mysql -u root -p
mysql> SHOW DATABASES;
mysql> CREATE DATABASE testdb;
mysql> CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'test623';
mysql> USE testdb;
mysql> GRANT ALL ON testdb.* TO 'testuser'@'localhost';
mysql> quit;
```

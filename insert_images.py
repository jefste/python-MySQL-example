#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb


def read_image():
    
    fin = open("Test_card.png")    
    img = fin.read()
    
    return img
    

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
 
with con:
    
    cur = con.cursor()
    data = read_image()
    cur.execute("INSERT INTO Images VALUES(1, %s)", (data, ))

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#!/usr/bin/python
import pymysql

db = pymysql.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="root",  # your password
                         db="ClimbingHoldsApe",
                         charset='utf8mb4',
                         autocommit=True)       # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

#cur.execute("CREATE TABLE Persons (PersonID varchar(20), LastName varchar(20), FirstName varchar(20), Address varchar(20), City varchar(20), PRIMARY KEY (FirstName, LastName));")
# Use all the SQL you like
#try:
	#cur.execute("INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) VALUES ('2', 'Jonesy', 'Cody', '788 Taylor Ln', 'Stoughton');")




# print all the first cell of all the rows
#except:

	
cur.execute("SELECT * FROM Moonboard")
for row in cur.fetchall():
	print(row)

db.close()
#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="ClimbingHoldsApe.db.8216949.hostedresource.com",    # your host, usually localhost
                     user="ClimbingHoldsApe",         # your username
                     passwd="Comply9879!",  # your password
                     db="ClimbingHoldsApe")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

#cur.execute("CREATE TABLE Persons (PersonID varchar(20), LastName varchar(20), FirstName varchar(20), Address varchar(20), City varchar(20), PRIMARY KEY (FirstName, LastName));")
# Use all the SQL you like
#try:
	#cur.execute("INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) VALUES ('2', 'Jonesy', 'Cody', '788 Taylor Ln', 'Stoughton');")
cur.execute("ALTER TABLE Moonboard ADD repeats VARINT(5) AFTER Moves") 



# print all the first cell of all the rows
#except:
print("DUPLICATE")
	
cur.execute("SELECT * FROM Moonboard")
for row in cur.fetchall():
	print(row)

db.close()
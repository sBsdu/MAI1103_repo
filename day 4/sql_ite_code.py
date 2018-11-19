import sqlite3

#create database
conn = sqlite3.connect('employees.db')

#create cursor
c = conn.cursor()

#create table
#c.execute("""create table employee(id INTEGER, first TEXT,last TEXT,pay INTEGER)""")

id = 01
first = "'BSDU'"
last = "'University'"
pay = 500000
#INSERT INTO employees values (01,'BSDU','Univarsity',500000)
c.execute("""INSERT INTO employee VALUES ({},{},{},{})""".format(id,first,last,pay))

c.execute('select* FROM employee')

print (c.fetchall())




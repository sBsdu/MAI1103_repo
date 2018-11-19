import sqlite3

import csv
#create database
conn = sqlite3.connect('zoo.db')

#create cursor
c = conn.cursor()

#create table
#c.execute("""create table zoo(animal text,uniq_id integer,water_need integer)""")


with open('zoo.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for i in csv_reader:
        c.execute("""INSERT INTO zoo VALUES('{}','{}','{}')""".format(i[0],i[1],i[2])) 
        
       



c.execute("""select* FROM zoo""")

print (c.fetchall())



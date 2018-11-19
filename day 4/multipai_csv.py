import sqlite3

import csv
#create database
conn = sqlite3.connect('zoo.db')
conn = sqlite3.connect('carmakers.db')
conn = sqlite3.connect('list.db')

#create cursor
c = conn.cursor()
#create table
#c.execute("""create table zoo(animal text,uniq_id integer,water_need integer)""")
choice_1 = input('>')
if(choice_1==1):
    with open('zoo.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for i in csv_reader:
            c.execute("""INSERT INTO zoo VALUES('{}','{}','{}')""".format(i[0],i[1],i[2]))
            c.execute("""select* FROM zoo""")
            print (c.fetchall())
choice_2 = input('>')
if(choice_2==2):
    c.execute("""create table carmakers(maker text ,FullName text,country integer)""")
    with open('carmakers.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for i in csv_reader:
            c.execute("""INSERT INTO carmakers VALUES('{}','{}','{}')""".format(i[0],i[1],i[2]))
            c.execute("""select* FROM carmakers""")
            print (c.fetchall())
choice_3 = input('>')
if(choice_3==3):
    c.execute("""create table list(LastName text,FirstName text,Grade integer,Classroom integer)""")
    with open('list.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for i in csv_reader:
            c.execute("""INSERT INTO list VALUES('{}','{}','{}','{}')""".format(i[0],i[1],i[2],[3]))
            c.execute("""select* FROM list""")
            print (c.fetchall())


        

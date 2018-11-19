
#from pandas impot dataframe
import mysql.connector
import csv
#connect to mysql server along with database name
conn = mysql.connector.connect(user ='root',passward = 'mydb',host = 'localhost')

#create cursor
mycursor = conn.cursor()

mycursor = executed(


with open('zoo.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for i in csv_reader:
        c.execute("""INSERT INTO zoo VALUES('{}','{}','{}')""".format(i[0],i[1],i[2])) 
        
       



c.execute("""select* FROM zoo""")

print (c.fetchall())

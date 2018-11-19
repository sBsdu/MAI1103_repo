import csv

with open('zoo.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        #print (row)
        print (row[2])

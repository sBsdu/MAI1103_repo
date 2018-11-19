with open('zoo.csv')as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    #to skip the header from csv file


    for row in csv_reader:
        #print(row)
        if row[0] not in animal_dict.keys():
            animal_dict[row[0]]= int(row[2])
        else:
            animal_dict[row[0]] = animal_dict[row[0]]+int(row[2])

print"all animals water needs are \n",animal_dict
or key,values in animal_dict.items():
    print (key,values)

import csv

water_1= 0
water_2= 0
water_3= 0
water_4= 0
water_5= 0
water_6= 0
with open('zoo.csv')as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    #to skip the header from csv file


    for row in csv_reader:
        if row[0]=='elephant':
          water_1 = water_1+ int(row[2])
        elif row[0]=='tiger':
          water_2 = water_2+ int(row[2])
        elif row[0]=='lion':
          water_3 = water_3+ int(row[2])
        elif row[0]=='zebra':
          water_4 = water_4+ int(row[2])
        elif row[0]=='kangaroo':
          water_5 = water_5+ int(row[2])
          water_6=water_1+water_2+water_3+water_4+water_5
    print 'total water need for animal is=',water_6
    print 'total water need for elephant is=',water_1
    print 'total water need for tiger is =',water_2
    print 'total water need for lion is =',water_3
    print 'total water need for zebra is =',water_4
    print 'total water need for kangaroo is=',water_5

# my file
water = 0
my_file = open("zoo2.CSV",'rt')
              
for i in my_file:
    y = i.split(',')
    if y[0]=='elephant':
          print y[2]
          water = water+ int(y[2])
print"total water need for elephant is =",water
my_file = open("zoo2.CSV",'rt')
              
for i in my_file:
    y = i.split(',')
    if y[0]=='tiger':
          print y[2]
          water = water+ int(y[2])
print"total water need for tiger is =",water
my_file = open("zoo2.CSV",'rt')
              
for i in my_file:
    y = i.split(',')
    if y[0]=='zebra':
          print y[2]
          water = water+ int(y[2])
print"total water need for zebra is =",water
my_file = open("zoo2.CSV",'rt')
              
for i in my_file:
    y = i.split(',')
    if y[0]=='kangaroo':
          print y[2]
          water = water+ int(y[2])
print"total water need for kangaroo is =",water
my_file.close()

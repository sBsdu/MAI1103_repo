# my file
water = 0
my_file = open("zoo2.CSV",'rt')
              
for i in my_file:
    y = i.split(',')
    if y[0]=='elephant':
          water = water+ int(y[2])
    if y[0]=='elephant':
          water = water+ int(y[2])
print"total water need for elephant is =",water

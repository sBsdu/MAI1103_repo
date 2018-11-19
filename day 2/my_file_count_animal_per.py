# cunt animal in zoo table
count_elephant = 0
count_lion = 0
count_tiger = 0
count_zebra = 0
count_kangaroo = 0

my_file = open("zoo2.CSV",'rt')

for i in my_file:
    y = i.split(',')
    if (y[0] == 'elephant'):
        count_elephant = count_elephant + 1

    if (y[0] == 'lion'):
        count_lion = count_lion + 1

    if (y[0] == 'tiger'):
        count_tiger = count_tiger + 1

    if (y[0] == 'zebra'):
        count_zebra = count_zebra + 1

    if (y[0] == 'kangaroo'):
        count_kangaroo = count_kangaroo + 1

        
print count_elephant
print count_lion
print count_tiger
print count_zebra
print count_kangaroo

my_file.close()

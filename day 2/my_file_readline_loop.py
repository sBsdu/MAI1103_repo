# my file

my_file =open('C:/a.txt','rt')
my_file_3 =open('c.txt','wt')

for i in my_file:

     my_file_3.write(i)

my_file.close()
my_file_3.close()

# my file

my_file =open("student.txt",'wt')

number = 0
while number <7:
       student_name = raw_input("enter name of student>")
       number = number + 1
       my_file.write(student_name+'\n')

my_file.close()


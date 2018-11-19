counter = 2

while counter < 100:
    i = 1
    while i < counter:
        i =i + 1
        if (counter % i == 0 ):
            break
        
    if i == counter:
            print  "prime number = ", counter
    counter = counter + 1
   

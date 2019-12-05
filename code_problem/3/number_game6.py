#Challenge 6
#    Print the number of tries left 

import random

count = 0
while count<6:
    a = random.randrange(1,10)

    
    count = count+1
    num = int(input("enter the Guess number:"))
    
    if a==num:
        print("number is {}, player wins and computer lose".format(num))
        
    else:
        print("number is {}, player lose and computer wins".format(a))
    
    count2 = 6-count
    print("Number of tries left",count2)

#Challenge 5
#Limit the number of guesses to maximum 6 tries 



import random


count = 0
while count<6:
    a = random.randrange(1,10)

    num = int(input("enter the Guess number:"))
    count = count+1
    if a==num:

        print("number is {}, player wins and computer lose".format(num))
        
    else:
    
        print("number is {}, player lose and computer wins".format(a))

#Challenge 8
#   Catch when someone submits a non integer

import random
while True:
    a = random.randrange(1,10)
    num = input("enter the Guess number:")
    if num.isdigit() == False:                  #exception handling
        print("please enter the correct input")
        continue
    num = int(num)
    if a==num:
        print("number is {}, player wins and computer lose".format(num))
        break
    else:
        print("number is {}, player lose and computer wins".format(a))
        
#Challenge 7
#    Lets give user the option to play again
def game():
    import random

    a = random.randrange(1,10)

    num = int(input("enter the Guess number:"))

    if a==num:
        print("player wins and computer lose")

    else:
        print("player lose and computer wins")
        
    return("")
print(game())

inp= input("play again press k, else press any key")

if inp =="k":
    print(game())    

else:
    print()
    

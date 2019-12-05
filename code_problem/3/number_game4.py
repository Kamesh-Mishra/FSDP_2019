# Interactive Guess the Number Game 

"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""

'''
Challenge 2
   Print the secret number and guess number when Player loses using format function 
'''

#Challenge 4
#    Let people play again and again until he guesses the right secret number




import random
while True:
    a = random.randrange(1,10)

    num = int(input("enter the Guess number:"))

    if a==num:
        print("number is {}, player wins and computer lose".format(num))
        break

    else:
        print("number is {}, player lose and computer wins".format(a))
        

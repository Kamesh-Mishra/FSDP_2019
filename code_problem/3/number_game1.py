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
import random

a = random.randrange(1,10)

num = int(input("enter the Guess number:"))

if a==num:
    print("player wins and computer lose")

else:
    print("player lose and computer wins")

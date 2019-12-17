
"""
Name: 
    Random Game 3         
Filename:
    randon_game3.py
Problem Statement:
    Write a program for a Higher / Lower guessing game
    The computer randomly generates a sequence of up to 10 numbers
    between 1 and 13. The player each after seeing each number
    in turn has to decide whether the next number is higher or lower.
    If you can remember Brucie’s ‘Play your cards right’ it’s basically
    that. If you get 10 guesses right you win the game.
    Starting number : 12
    Higher(H) or lower(L)? L
    Next number 8
    Higher(H) or lower(L)? L
    Next number 11
    You lose
Data:
    Not required
Extension:
    Give the players two lives
    Make sure only H or L can
    be entered  
Hint: 
    Use a condition controlled loop (do until, while etc) to control the
    game. Do not find yourself repeating the same code over and over!
    You don't need to remember all 10 numbers just the current number
    /next number. Don’t forget you’ll have to keep a count of the
    number of turns they’ve had. 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
""" 

import random
list1 = []
count = 0
    
while count< 10:
    count = count+1
    print("number of turn: ",count)
    
    num1 = random.randint(1,13)
    print("Starting number",num1)
    
    user = input("Higher(H) or lower(L)? ",)
    num2 = random.randint(1,13)
    print("next number: ",num2)
    
    if user == "L" and num2<=num1:
        
        list1.append(True)
        
    elif user == "H" and num2>num1:
        list1.append(True)
        
    else:
        print("you lose")
        list1.append(False)
        break
    
if all(list1):
    print("You won")
else:
    pass

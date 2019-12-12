
"""
Name: 
    CodeBreaker         
Filename:
    code_breaker.py
Problem Statement:
    The computer generates a 4 digit code
    The user types in a 4 digit code. Their guess.
    The computer tells them how many digits they guessed correctly
Data:
    Not required
Extension:
    the computer tells them how many digits are guessed correctly 
    in the correct place and how many digits have
    been guessed correctly but in the wrong place.
    The user gets 12 guesses to either 
    WIN – guess the right code. 
    Or
    LOSE – run out of guesses.  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
"""   

from random import randint
list1 = [randint(0,9),randint(0,9),randint(0,9),randint(0,9)]
n = [int(input("enter first digit: ")),int(input("enter second digit: ")),int(input("enter third digit: ")),int(input("enter forth digit: "))]

    
if n[0] == list1[0]:
    print("First digit is guessed correctly")
            
if n[1] == list1[1]:
    print("second digit is guessed correctly")
            
if n[2] == list1[2]:
    print("third digit is guessed correctly")
    
if n[3] == list1[3]:
    print("forth digit is guessed correctly")

if list1!=n:
    print("LOSE")
else:
    print("WON")
        

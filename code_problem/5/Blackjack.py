

"""
Name: 
    Blackjack         
Filename:
    Blackjack.py
Problem Statement:
    Play a game that draws two random cards.
    The player then decides to draw or stick.
    If the score goes over 21 the player loses (goes ‘bust’).
    Keep drawing until the player sticks.
    After the player sticks draw two computer cards. 
    If the player beats the score they win. 
Data:
    Not required
Extension:
    Aces can be 1 or 11! The number used is whichever gets the highest score.  
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

import random
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
k = random.choice(list1)
l =  random.choice(list1)
print("you get: ",k+l)
if (k+l)<21:
    a= random.choice(list1)
    b = random.choice(list1)
    print("computer gets: ",a+b)
    
    if (a+b)<(k+l):
        print("you won")
    else:
        print("computer won")
else:
    print("you bust")

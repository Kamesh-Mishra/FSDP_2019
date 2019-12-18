

"""
Name: 
    Bricks         
Filename:
    bricks.py
Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    2, 2, 11
Sample Output:
    True
""" 
inp1 = int(input("Enter number of small bricks: "))

inp2 = int(input("Enter number of big bricks: "))

inp3 = int(input("Enter target: "))

list1 = [inp1,inp2,inp3]

k = inp1*1+inp2*5
if k >= inp3:
    print(True)
else:
    print(False)
    

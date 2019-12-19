
"""
Name: 
    Character Frequency       
Filename:
    frequency.py 
Problem Statement:
    This program accepts a string from User and counts the number of characters 
    (character frequency) in the input string. 
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
    www.google.com
Sample Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
""" 
import collections
inp = input("enter string: ")

dict1 = {}

dict1 = collections.Counter(inp)
print(dict1)


"""
Name: 
    Digit Letter Counter      
Filename:
    digit_letter_counter.py
Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits 
    and letters. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Store the letters and Digits as keys in the dictionary  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Python 3.2
Sample Output:
    Letters 6 
    Digits 2
""" 

inp = input("enter input: ")
d = 0
k = 0
o = 0
for i in inp:
    if i in "0123456789":
        d = d+1
    elif i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        k = k+1
    else:
        o = o+1
        
print("Digits:",d, "Letters:",k)

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format4.py
  Problem Statement:
    This program accepts the user's first name and last name 
    Print them in reverse order with a space between them.
    Take Input from User 
    Your code should have only a single user input statement.  
  Hint:
    Try to serach for some function in the str using help() and dir()
  Input:
    Forsk Technologies
  Output:
    Technologies Forsk
"""

#String Handling

name = input("Enter first and last name:")
a = name.split()
b = a[::-1]
print(" ".join(b))


'''Hands On'''
# Print all the numbers from 1 to 10 using condition in while loop


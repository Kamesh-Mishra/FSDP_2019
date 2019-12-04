"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""


inp = input("enter input string statement:")

a= inp.split() #split string into list of each word as one individual object of list

print("*".join(a)) # convert list into string with * in it



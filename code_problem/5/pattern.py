"""
Code Challenge
Name: 
    Pattern Builder
Filename: 
    pattern.py
Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
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
    5
Sample Output:
    Below is the output of execution of this program.
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * 
    * * * 
    * * 
    * 
"""
n= int(input("number of rows:"))
for i in range(n-1):
        
        for j in range(n-i):
                print(" ", end=" ")
        print()
        for k in range(n-j):
                print("*",end =' ')
        
for i in range(n):
        
        for j in range(n-j):
                print(' ',end ='')
        print()
        for k in range(n-i):
                print("*", end=" ")
        

    

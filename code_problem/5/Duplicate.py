
"""
Name: 
    Duplicate       
Filename:
    Duplicate.py 
Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values with original 
    order reserved 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Distance = (Acceleration*Time*Time ) / 2 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 


l =[12,24,35,24,88,120,155,88,120,155]

k = list(set(l))
k.sort()
print(k)

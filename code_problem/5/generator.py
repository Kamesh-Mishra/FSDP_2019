
"""
Name: 
    generator       
Filename:
    3.py 
Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers. 
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
    2, 4, 7, 8, 9, 12
Sample Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
""" 

inp = input("enter input: ")

inp = inp.replace(",","")
print(tuple(inp))
print(list(inp))

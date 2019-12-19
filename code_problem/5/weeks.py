
"""
Name: 
    weeks       
Filename:
    weeks.py 
Problem Statement:
    Write a program that adds missing days to existing tuple of days 
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
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
Sample Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
""" 

inp =('Monday', 'Wednesday', 'Thursday', 'Saturday')



inp1 = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

inp = set(inp)
inp1 = set(inp1)


tuple(inp.union(inp1))

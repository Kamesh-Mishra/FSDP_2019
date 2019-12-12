

"""
Name: 
    Vowels Finder
Filename: 
    vowels.py
Problem Statement:
    Remove all the vowels from the list of states  
Hint: 
    Use nested for loops and while
Data:
    Not required
Extension:
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
Sample Output:
    ['lbm', 'clfrn', 'klhm', 'flrd'] 
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
list1 = []
for i in state_name:
    for s in i:
        if s in  ["a","e","i","o","u",'A',"O"]:
            i = i.replace(s,'')
    list1.append(i)
print(list1)        
    

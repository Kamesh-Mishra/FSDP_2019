
"""
Name: 
    Letter Distribution       
Filename:
    letter_dist.py 
Problem Statement:
    Ask the user to enter some text. 
    Display the distribution of letters from within the text. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Use dictionaries to solve 
    import string and use string.ascii_lowercase 
Algorithm:
    Convert all letters to lowercase
    Ignore characters that aren't lowercase letters
    Create a dictionary in which the keys are letters and the values are the counts. 
Boiler Plate Code:
    Not Available 
Sample Input:
    This is a test.  Show me the distribution, already!
Sample Output:
    t: 6 15%
    h: 3 7%
    i: 5 12%
    s: 5 12%
    a: 3 7%
    e: 4 10%
    o: 2 5%
    w: 1 2%
    m: 1 2%
    d: 2 5%
    r: 2 5%
    b: 1 2%
    u: 1 2%
    n: 1 2%
    l: 1 2%
    y: 1 2%
""" 



import collections
inp = input("Enter input: ")
t = 0
dict1 = {}
dict1 = collections.Counter(inp)
for i in dict1.values():
    t = t+i
for i,j in dict1.items():
    print(i,j,round((j/t)*100),"%")


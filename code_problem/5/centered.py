
"""
Name: 
    Centered Average         
Filename:
    centered.py
Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is the 
    mean average of the values, except ignoring the largest and smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. Use int division to produce the final average. 
    You may assume that the array is length 3 or more.
    Take input from user
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
    1, 2, 3, 4, 100 
Sample Output:
    3 
"""   
inp = input("enter values: ").split(",")
print(inp)


inp.sort()

print(inp)
sum = 0
for i in inp:
    sum = sum+int(i)
print(((sum-int(inp[0])-int(inp[-1]))/(len(inp)-2)))

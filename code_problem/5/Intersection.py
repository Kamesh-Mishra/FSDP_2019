"""
Name: 
    Intersection       
Filename:
    Intersection.py 
Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists. 
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
    Not Available
Sample Output:
    Not Available
""" 

list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]


set1 = set(list1)
set2 = set(list2)

set3 = set1.intersection(set2)
list3 = list(set3)
print(list3)

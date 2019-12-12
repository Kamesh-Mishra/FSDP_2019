"""
Name: 
    2 Dimensional Random List         
Filename:
    random_list.py
Problem Statement:
    Create a 2-Dimensional list of list of integers 10 by 10.
    Fill the 2-Dimensional list with random numbers in the range 0 to 255
    Display the array on the screen showing the numbers
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

import random
list1 = []
list2 = []

for item in range(10):
    for index in range(10):
        list1.append(random.randint(0,255))
   
   
    list2.append(list1.copy())
    list1.clear()
print(list2)

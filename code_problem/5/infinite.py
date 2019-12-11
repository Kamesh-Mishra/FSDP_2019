
"""
Name:
    Infinite input
Filename: 
    infinite.py    
Problem Statement:
    Write a program that asks the user, again and again, to enter a number.
    When the user enters an empty string, then stop asking for additional inputs.
    Along the way, as the user is entering numbers, 
    I want you to store those numbers in a list. 
    I also want you to keep track of the minimum and maximum values that you've seen so far.
    When the user has finished entering numbers, your program should print out:
         The sum of these numbers
         The average (mean) of these numbers
         The largest and smallest numbers you received from the user
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Use infinite while loop  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available  
    
"""

import statistics
list1 = []
while True:  
    inp = input("Enter a number: ")
    if not inp:
        print("sorted order of input: ",sorted(list1))
        print("maximum input is: ",max(list1))
        print("Minimum input is: ",min(list1))
        print("sum of all inputs is: ",sum(list1))
        print("mean of all inputs is: ",statistics.mean(list1))
        
        break
    inp1 = int(inp)
    
    list1.append(inp1)
    print("List of entered input is: ",list1)
    

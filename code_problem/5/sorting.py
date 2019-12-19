
"""
Name: 
    Sorting         
Filename:
    sorting.py
Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score 
Data:
    Not required
Extension:
    Aces can be 1 or 11! The number used is whichever gets the highest score.  
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
Sample Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
""" 
list1=[]
list2 =[]
list3=[]
list1 = input("Enter input: ").split(",")
a = 0
for i in range(0,len(list1),3):
    list3=[]
    for j in range(a,i):
    
        list3.append(list1[i])
        #print(j)
    a = i
    list2.append(tuple(list3))
    #print(i)
print(list3)
#print(inp)






















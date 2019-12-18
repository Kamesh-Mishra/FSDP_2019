
"""
Name: 
    Translate Function         
Filename:
    translate.py
Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User
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
    This is fun
Sample Output:
    ToThohisos isos fofunon
""" 
inp = input("Enter input string: ")


list1 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
list2= []
for i in inp:
    
    for j in i:
        if j.lower() in list1:
            list2.append(j+"o"+j)
        if j.lower() not in list1:
            list2.append(j)

print(''.join(list2))

                

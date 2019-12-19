
"""
Name: 
    Anagram 2        
Filename:
    anagram2.py
Problem Statement:
    Two words are anagrams if you can rearrange the letters of one to spell the second.  
   For example, the following words are anagrams:
   ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
  
   create a function which takes two arguments and return whether they are angram or no ( True or False)
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Use dictionary to solve it 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
"""

import collections    
inp1 = input("enter input: ").replace(" ","")
inp2 = input("enter input: ").replace(" ","")

dict1 = {}
dict2 = {}
dict1 = collections.Counter(inp1)
dict2 = collections.Counter(inp2)

def anagram(dict1,dict2):
        
    for i in dict1.keys():
        if dict1[i] != dict2[i]:
            return False
            break
    return True
anagram(dict1,dict2)


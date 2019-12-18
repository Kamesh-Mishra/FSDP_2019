
"""
Name: 
    Anagram         
Filename:
    anagram.py
Problem Statement:
    Two words are anagrams if you can rearrange the letters of one to spell the second.  
   For example, the following words are anagrams:
   ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
  
   create a function which takes two arguments and return whether they are
   angram or no ( True or False)
Data:
    Not required
Extension:
    Not Available  
Hint: 
    How can you tell quickly if two words are anagrams?  
    Try to use set 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 


inp1 = input("enter first word: ")
inp1 = list(inp1)
inp1 = set(inp1)

inp2 = input("enter second word: ")
inp2 = list(inp2)
inp2 = set(inp2)
def anagram(inp1,inp2):
    if inp1 == inp2:
        return True
    else:
        return False
    
anagram(inp1,inp2)
    

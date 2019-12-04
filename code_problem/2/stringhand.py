#String Handling

"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    stringhand.py
  Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""




name = input("Enter name:")
a = name.split()
b = a[::-1]
print(" ".join(b))


"""
Name: 
    Pangram         
Filename:
    pangram.py
Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    The five boxing wizards jumps. 
    Sphinx of black quartz, judge my vow.
    The jay, pig, fox, zebra and my wolves quack!
    Pack my box with five dozen liquor jugs.
Sample Output:
    NOT PANGRAM 
    PANGRAM
    PANGRAM
    PANGRAM
"""  

inp = input("Enter input string: ")
def pangram():
    str1 = "abcdefghijklmnopqrstuvwxyz"
    for i in str1:
        if i in inp:
            if i == str1[-1]:      #will check till last element and then print "pangram"
                print("PANGRAM")
        else:
            print("NOT PANGRAM")
            break
pangram()

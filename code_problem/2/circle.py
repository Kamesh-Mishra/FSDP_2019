
#Area and Perimeter of Circle

radius = float(input("Enter the value of radius:"))
import math
from math import pi
math.pi

area= (pi * radius * radius)

perimeter = (2 * pi * radius)

print("Area of circle is:",area,"Perimeter of circle is:",perimeter)



#***********************
#***********************
#***********************
'''Hands On'''
string = "Rajasthan"
#Print characters at the even index number

string = "Rajasthan"
print(string[0::2])




'''Hands On'''
string = "Rajasthan"
#Print the given string in reverse 

print(string[::-1])



'''Hands On'''
string = "Forsk Technologies"
#Print Forsk using slicing ( forward indexing Left to Right  )  

print(string[0:5])


'''Hands On'''
string = "Forsk Technologies"
#Print Technologies using slicing ( forward indexing Left to Right )  

print(string[6:])



'''Hands On'''
string = "Forsk Technologies"
#Print Forsk using slicing ( Reverse indexing Right to Left  )  

print(string[-13:-7])


'''Hands On'''
string = "Forsk Technologies"
#Print Technologies using slicing ( forward indexing Right to Left )  
print(string[-12:])



'''Hands On'''
string = "Forsk Technologies"
#Print ksroF using slicing ( forward indexing and Reverse  Indexing)  

print(string[4::-1])
print(string[:])


'''Hands On'''
string = "Forsk Technologies"
#Print siesgolonhceT using slicing ( forward indexing Left to Right )  

print(string[:5:-1])


'''Hands On'''
#Print Technologies Forsk using slicing ( forward indexing Left to Right  )  

string = "Forsk Technologies"
print(string[6::],string[0:5])


'''Hands On'''
#Print Technologies Forsk using slicing ( Reverse indexing Right to Left ) 

string = "Forsk Technologies"

string = "Forsk Technologies"
print(string[-12:],string[-18:-13])

'''Hands On'''
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


str1 = input("enter string first: ")
str2 = input("enter string second: ")
a = str1[0]
b = str1[1]
c = str2[0]
d = str2[1]
print(c,d,str1[2:] ," ", a,b,str2[2:], sep ="")


'''########################################################'''
'''########################################################'''
'''########################################################'''


'''Hands On''' 
# Write a program to count the number of words in a sentence.

string = input("enter the sentence:")

print(len(string.split()),"number of words is in the sentence")


'''Hands On'''
# Develop a program that will display a sentence backwards after entered.

inp = input("Enter sentence:")
print(inp[::-1])



'''Hands On'''
# Given a string s, print the string again
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: try using replace function


s = input("enter the string: ")
s2 = s[1:]
a = s[0]
print(a,s2.replace(s[0],"*"),sep="")



'''Hands On'''
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!


s = 'This dinner is not that bad!'
w = s.find("not")
p= s.find("bad")

print(w)
print(p)
k = s.replace(s[w:p+3],"good")
print(k)


'''Hands On'''
# Take donut count from the user and print a string of the 
# form 'Number of donuts: <count>'
# where <count> is the donut count entered by the user. 
# However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# Number of donuts: 5
# Number of donuts: many


inp = int(input("enter count of donuts: "))
if inp>=10:
    print("Number of Donuts: Many")
else:
    print("Number of Donuts: ",inp)



'''Hands On'''
# Take input string from the user, 
# print a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.

inp = input("enter string: ")

if len(inp)>=2:
    print(inp[0]+inp[1]+inp[-2]+inp[-1])

else:
    print("")




'''Hands On'''
# Take the age as input from the user and print whether he is a infant, Child , 
# Adult,  Senior Citizen
# 0 - 1 is Infant
# > 1 and < than 18 is Child 
# > 18 and < 60 is Adult
# > 60 is Senior Citizen



inp = int(input("Enter the age: "))

if inp >= 0 and inp<=1:
    print("Infant")
    
elif inp>1 and inp<18:
    print("Child")
    
elif inp>=18 and inp<60:
    print("Adult")
    
else:
    print("Senior Citizen")





'''Hands On'''
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Print the resulting string.



inp = input("Enter String: ")

if len(inp)>=3:
    if  inp.endswith("ing", -3,)==True:
        print(inp[:-3]+"ly")
    else:
        print(inp+"ing")
else:
    print(inp)    


    


'''Hands On'''
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

inp1 = input("Enter String 1: ")
inp2 = input("Enter String 2: ")

n = int(len(inp1))
m = int(len(inp2))

if n%2==0:
    print(inp1[0:n//2] , inp1[n//2:] , end = " ")
    
if n%2!=0:    
    print(inp1[0:n//2+1] , inp1[n//2+1:] , end = " ")
    
if m%2==0:    
    print(inp2[0:m//2] , inp2[m//2:] , end = " ")
    
if m%2!=0:
    print(inp2[0:m//2+1] , inp2[m//2+1:] , end = " ")




'''Hands On'''
# Print all the numbers from 1 to 10 using condition in while loop

a=1
while a<=10:
   print(a)
   a = a+1



'''Hands On'''
# Print all the numbers from 1 to 10 using while True loop
n  = 1
while True:
    if n<=10:
        print(n)
        n = n+1
    else:
        break





'''Hands On'''
# Print all the even numbers from 1 to 10 using condition in while loop

n = 0
while n<=10:
    
    if n%2==0:
        print(n)
    n =n+1





'''Hands On'''
# Print all the even numbers from 1 to 10 using while True loop
n = 0
while True:
    if n<=10 and n%2==0 :
        print(n)
    n = n+1
        


'''Hands On'''
# Print all the odd numbers from 1 to 10 using condition in while loop

n = 0
while n<=10:
    
    if n%2!=0:
        print(n)
    n =n+1


'''Hands On'''
# Print all the odd numbers from 1 to 10 using while True loop

n = 0
while True:
    if n<=10 and n%2!=0 :
        print(n)
    n = n+1













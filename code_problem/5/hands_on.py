'''Hands On'''
# Take the list of the parts of your street address
# Write a loop that goes through that list and prints out each item in that list
myaddress = [3225, 'West', 'Foster', 'Avenue', 'Chicago', 'IL', 60625]


for address in myaddress:
    print(address)



'''Hands On'''
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.

words = ['aba', 'xyz', 'aa', 'x', 'bbb']
words1 = ['', 'x', 'xy', 'xyx', 'xx']
words2 = ['aaa', 'be', 'abc', 'hello']
print("count of strings: ",len(words))
print("count of strings: ",len(words1))
print("count of strings: ",len(words2))



'''Hands On'''
# Take your street address and make it a list variable myaddress
# where each token is an element.

# What would be the code to set the sum of the numerical portions of
# your address list to a variable called address sum?

# What would be the code to change one of the string elements of the
# list to another string (e.g., if your address had "West" in it, how would
# you change that string to "North")?

# Change the street portion of myaddress to have the street first 
# and the building number at the end. 
          

inp = input("Enter address")
myaddress = inp.split()
l = 0
for i in myaddress:
    if i.isnumeric():
        address_sum = address_sum+i
print(address_sum)






'''Hands On'''
#Looping through a list of temperatures and applying a test
#Pretend you have the following list of temperatures T:
T = [273.4, 265.5, 277.7, 285.5]
#and a list of flags called Tflags that is initialized to all False
Tflags = [False, False, False, False]
#Write a loop that checks each temperature in T and sets the corresponding
#Tflags element to True if the temperature is above the freezing point of water.

T = [273.4, 265.5, 277.7, 285.5]

Tflags = [False, False, False, False]
n = 0
for i in T:
    if T[n] > 273:
        print("Temperature in T is:",T[n])
        print("temperature is above the freezing point of water:", not Tflags[n])
    else:
        print("Temperature in T is:",T[n])
        print("temperature is above the freezing point of water:", Tflags[n])
        
    n = n+1



'''Hands On'''
# Take the list of the parts of your street address
# Write a loop that goes through that list and prints out each item in that list
myaddress = [3225, 'West', 'Foster', 'Avenue', 'Chicago', 'IL', 60625]

for i in myaddress:
    print(i)


'''Hands On'''
# Create a list of Fibonnaci numbers up to the 50th term.
# The program will then ask the user for which position in the sequence
# they want to know the Fibonacci value for
# The Fibonacci sequence was originally used as a basic model for rabbit population growth:

a = 0
b = 1

n = int(input("number of term: "))

list1 = [0,1]
for i in range(n-2):
    
    c = a+b

    a= b
    b = c
    
    
    list1.append(c)
print(list1)
  
inp = int(input("Enter position in the sequence: "))
print(list1[inp-1])
   




'''Hands On'''
# Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

list1 = ['aa', 'xx', 'zz'] #['aa', 'xx']         ['aa', 'aa']
list2 = ['bb', 'cc']       #['bb', 'cc', 'zz']   ['aa', 'bb', 'bb']



list2.extend(list1)
list2.sort()
print(list2)







'''Hands On'''
# Make a function days_in_month to return the number of days in a specific month of a year


inp = input("Enter month: ")
def days_in_month():
    
    
    list1 =["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"] 
    list2 =[31,29,31,30,31,30,31,31,30,31,30,31]
    if inp in list1:
        print(list2[list1.index(inp)])
days_in_month()






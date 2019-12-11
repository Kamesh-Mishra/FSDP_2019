
"""
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

"""

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


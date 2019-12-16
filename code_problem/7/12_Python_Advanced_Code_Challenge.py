


"""
Find all of the numbers from 1-1000 that are divisible by 7
"""
####### Method 1 #######
list1 = []
def divisible(number):
    if number%7==0:
        return number
for i in range(1,1001):
    num1 = divisible(i)
    if num1:
        list1.append(num1)
print(list1)
####### Method 2 #######
    
divisible_7 = [x for x in range(1,1001) if x%7==0]
print(divisible_7)

####### Method 3 #######

divisible_7a = list(filter(lambda x: x%7==0,list(range(1,1001))))
print(divisible_7a)



"""
Find all of the numbers from 1-1000 that have a 3 in them
"""
####### Method 1 #######
list1 = []
def item(number):
    if '3' in str(number):
        return number
for i in range(1,1001):
    num1 = item(i)
    if num1:
        list1.append(num1)
print(list1)
####### Method 2 #######

item_3 = [x for x in range(1,1001) if '3' in str(x)]
####### Method 3 #######
item_3a = list(filter(lambda x: '3' in str(x),list(range(1,1001))))
print(item_3a)
 


"""
Count the number of spaces in a string
"""

# 1
n=0
string = input("Enter string")
for i in string:
    if i==' ':
        n+=1
print(n)


# 2
a = len([i for i in string if i==' '])
print(a)


# 3
b = len(list(map(lambda x: x==' ',string)))
print(b)



"""
Remove all of the vowels in a string
"""
# 1
string = input("Enter string")
vowels = "aeiou"
remain = []
for i in string:
    if i not in vowels:
        remain.append(i)
a = "".join(remain)
print(a)


# 2
remain = [i for i in string if i not in vowels]
print("".join(remain))


# 3

a = list(filter(lambda x:x not in vowels,string))
print("".join(a))


"""
Find all of the words in a string that are less than 4 letters
"""
# 1
string = input("Enter a string").split()
output = []
for i in string:
    if len(i) <4:
        output.append(i)
# 2 
output =[i for i in string if len(i)<4]
print(output)

# 3

a = list(filter(lambda x:len(x)<4),string)
print(a)   



"""
A list of all consonants in the sentence 'The quick brown fox jumped over the lazy dog'
"""
# 1
string = 'The quick brown fox jumped over the lazy dog'
vowels = "aeiou "
consonants=[]
for i in string:
    if i not in vowels:
        consonants.append(i)

# 2
a = [i for i in string if i not in vowels]
print(a)

# 3

b = list(filter(lambda x:x not in vowels,string))
print(b)


        
"""
A list of all the capital letters (and not white space) in 'The Quick Brown Fox Jumped Over The Lazy Dog'
"""
# 1
string = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital = []
for i in string:
    if i==i.upper() and i!=' ':
        capital.append(i)
        
# 2
capital = [i for i in string if i==i.upper() if i!=' ']  

# 3
b = list(filter(lambda x:x==x.upper() and x!=' ',string))
print(b)



"""
A list of all square numbers formed by squaring the numbers from 1 to 1000.
"""
# 1
square = []
for i in range(1,1000):
    a = i**2
    if a<1000:
        square.append(a)
    else:
        break
# 2
square = [i**2  for i in range(1,1000) if i**2<1000]
# 3
square = list(map(lambda y:y**2,filter(lambda z :z**2<1000,list(range(0,1000)))))


"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print (names)

As you can see, this algorithm can potentially assign 
the same secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.


"""



"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)



(Hopefully, the secret agents will have good memories and won’t forget 
each other’s secret code names during the secret mission.)


Rewrite the above code using map.
    

"""



"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""


"""
Code Challenge

# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

1 Get the corresponding `celsius` values in list

2 Create the `celsius` dictionary

3 convert a dictionary of Fahrenheit temperatures into celsius




Solution:
#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)


# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
print(celsius_dict)


"""




"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint:
    Write a Python program using lambda and map.
    
# Assume the data in form of list of list
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]

"""

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
"""


"""
Code Challenge
  Name: 
    Population Counting
  Filename: 
    Population.py
  Problem Statement:
      
      The given input has a number of rows, each with four 
      fields from a table, containing:
          

          Rank,City,Population,State or union territory
          1,Mumbai,"124.42",Maharashtra


    You are required to output:

        Country, State, Population of the state (obtained by summing up 
        the population of each city in that state)  


    Sample Input

    1,Mumbai,"124.42",Maharashtra
    9,Pune,"31.24",Maharashtra
    13,Nagpur,"24.05",Maharashtra
    6,Chennai,"46.46",Tamil Nadu
    59,Salem,"8.31",Tamil Nadu


    Sample Output

    {"key":"India,Tamil Nadu","value":54.77}
    {"key":"India,Maharashtra","value":179.72}


    Explanation

    The population of India,Tamil Nadu is obtained by adding the population of 
    Chennai and Salem. 
    This process is repeated for India,Maharashtra. 


    Refer to population.csv


"""

"""
Code Challenge

# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

1 Get the corresponding `celsius` values in list

2 Create the `celsius` dictionary

3 convert a dictionary of Fahrenheit temperatures into celsius




Solution:
#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)


# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
print(celsius_dict)


"""




"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""










# Create a new Code Challenge from this 
"""
stopchars = ['a', 'b', 'c', 'd']

def  normalize_word(word):
    word =  word.strip().lower()
    word = "".join([char for char in word if char not in stopchars])
    return word

stopchars = ['a', 'b', 'c', 'd']

def  normalize_word(word, stops=stopchars):
    word =  word.strip().lower()
    word = "".join([char for char in word if char not in stops])
    return word

"""
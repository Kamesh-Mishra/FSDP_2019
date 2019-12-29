
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


#[{names[i] : random.choice(code_names)} for i in range(len(names))]

#map and Reduce func

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

list1 = list(map(lambda x: x+'  ->  '+random.choice(code_names),names))

for i in list1:
    print(i)

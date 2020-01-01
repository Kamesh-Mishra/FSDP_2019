
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

import functools

list1 = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]


list2 = list(map(lambda x : x[0],list1))
#print(list2)



list3 = list(map(lambda x : x[1:],list1))
#print(list3)




list5 = list3[0]
sum1 = list(map(lambda x : x[1]*x[2],list5))

list6 = list3[1]
sum2 = list(map(lambda x : x[1]*x[2],list6))

list7 = list3[2]
sum3 = list(map(lambda x : x[1]*x[2],list7))

list8 = list3[3]
sum4 = list(map(lambda x : x[1]*x[2],list8))

s1 = functools.reduce(lambda a,b:a+b,sum1)
print(s1)

s2 = functools.reduce(lambda a,b:a+b,sum2)

s3 = functools.reduce(lambda a,b:a+b,sum3)

s4 = functools.reduce(lambda a,b:a+b,sum4)

list11=[s1,s2,s3,s4]
final_list =list(zip(list2,list11))
print(final_list)    
lisst=[]
for i in final_list:
    lisst.append(list(i))
print(lisst)   

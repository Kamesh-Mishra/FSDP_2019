#pyramid patterns

"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(" ",end ='')
        for k in range(n-j):
                print("*",end =' ')
        print()

number of rows:6
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * *

 """
"""
n= int(input("number of rows:"))
for i in range(n+1):
        
        for j in range(n-i):
                print("*",end =' ')
        print()
        for k in range(n-j):
                print(" ", end="")

number of rows:6
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     *


"""   


"""

n= int(input("number of rows:"))
for i in range(n+1):
        
        for j in range(n-i):
                print(chr(65+(n-i-1)),end =' ')
        print()
        for k in range(n-j):
                print(" ", end="")



number of rows:6
F F F F F F 
 E E E E E 
  D D D D 
   C C C 
    B B 
     A 
"""
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(" ",end ='')
        for k in range(n-j):
                print(chr(65+i),end =' ')
        print()


        number of rows:6
      A 
     B B 
    C C C 
   D D D D 
  E E E E E 
 F F F F F F
 """

"""
n= int(input("number of rows:"))
for i in range(n+1):
        
        for j in range(n-i+1):
                print(" ",end ='')
        for k in range(n-j):
                print(i,end =' ')
        print()

  
number of rows:6
       
      1 
     2 2 
    3 3 3 
   4 4 4 4 
  5 5 5 5 5 
 6 6 6 6 6 6 
"""
"""
n= int(input("number of rows:"))
for i in range(n+1):
        
        for j in range(n-i+1):
                print(" ",end ='')
        for k in range(n-j):
                print(i,end =' ')
        print()

number of rows:6
       
      1 
     2 2 
    3 3 3 
   4 4 4 4 
  5 5 5 5 5 
 6 6 6 6 6 6 
"""
"""
n= int(input("number of rows:"))
for i in range(n+1):
        
        for j in range(n-i):
                print(n-i,end =' ')
        print()
        for k in range(n-j):
                print(" ", end="")

number of rows:5
5 5 5 5 5 
 4 4 4 4 
  3 3 3 
   2 2 
    1 

"""

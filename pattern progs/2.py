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

"""
n= int(input("number of rows:"))
for i in range(n+1):
        
        for j in range(n-i+1):
            
            print(" ",end ='')
            
        for k in range(n-j):
            if (i%2!=0):
                print(i,end =' ')
            
        print()


number of rows:6
       
      1 
     
    3 3 3 
   
  5 5 5 5 5

  """

"""

n= int(input("number of rows:"))
for i in range(n+1):
        
        for j in range(n-i+1):
            
            print(" ",end ='')
            
        for k in range(n-j):
            if (i%2!=0):
                print(chr(65+i-1),end =' ')
            
        print()

number of rows:6
       
      A 
     
    C C C 
   
  E E E E E 
 """
"""
n= int(input("number of rows:"))
for i in range(n+1):
        
        for j in range(n-i+1):
                print(" ",end ='')
        for k in range(n-j):
                print(j,end =' ')
        print()


number of rows:5
      
     4 
    3 3 
   2 2 2 
  1 1 1 1 
 0 0 0 0 0
 """

"""
import keyword
print(keyword.kwlist)
"""
"""
n = int(input("enter number of rowa:"))
for a in range(n):
        
        for b in range(n-a):
                print("", end=" ")
        
        for c in range(1,n-b):
                
                print(c+a-1,end =' ')
        
        print()
    
enter number of rowa:6
      
     1 
    2 3 
   3 4 5 
  4 5 6 7 
 5 6 7 8 9

 """
"""

n = int(input("enter number of rowa:"))
for a in range(n):
        
        for b in range(n-a):
                print("", end=" ")
        
        for c in range(1,n-b):
                        
                print(c+b-1,end =' ')
        
        print()


enter number of rowa:6
      
     4 
    3 4 
   2 3 4 
  1 2 3 4 
 0 1 2 3 4         


"""
"""
n= int(input("number of rows:"))
for i in range(n-1):
        
        for j in range(n-i):
                print(" ", end=" ")
        print()
        for k in range(n-j):
                print("*",end =' ')
        
for i in range(n):
        
        for j in range(n-j):
                print(' ',end ='')
        print()
        for k in range(n-i):
                print("*", end=" ")
        


number of rows:6
            
*           
* *         
* * *       
* * * *     
* * * * *   
* * * * * *       
* * * * * *  
* * * * *       
* * * *  
* * *       
* *  
* 


"""

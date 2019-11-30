##ractangle patterns


"""
for i in range(6):
        
        for j in range(6):
                print(chr(65+i),end =' ')
        print()

"""



"""
for i in range(6):
        
        for j in range(6):
                print(chr(65+j),end =' ')
        print()
        
"""
"""
for i in range(ord("A"),ord("D")):
        for j in range(ord("A"),ord('D')):
                print((chr), end = " ")
        print()

        
"""
"""
for i in range(6):
        
        for j in range(6):
                print(chr(65),end =' ')
        print()
"""
##triangle patterns


"""
for i in range(6):
        
        for j in range(1,i):
                print(chr(65),end =' ')
        print()

"""        
"""
for i in range(6):
        
        for j in range(i):
                print(chr(65+j),end =' ')
        print()
"""
#inverted triangle of numbers
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print((j+1),end =' ')
        print()
                        
"""
# inverted triangle for char 

"""                
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(chr(65+j),end =' ')
        print()



        number of rows:5
A B C D E 
A B C D 
A B C 
A B 
A

"""


"""

n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print((i+1),end =' ')
        print()


number of rows:5
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

"""
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print((n),end =' ')
        print()

number of rows:6
6 6 6 6 6 6 
6 6 6 6 6 
6 6 6 6 
6 6 6 
6 6 
6

"""
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(j,end =' ')
        print()

number of rows:6
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1 
0
"""
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(i,end =' ')
        print()


number of rows:6
0 0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
"""

"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(n-i,end =' ')
        print()

number of rows:6
6 6 6 6 6 6 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
"""
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(n-j,end =' ')
        print()

6 5 4 3 2 1 
6 5 4 3 2 
6 5 4 3 
6 5 4 
6 5 
6 
"""
'''
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(chr(65+j),end =' ')
        print()


number of rows:6
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A 


'''
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(chr(65+i),end =' ')
        print()

number of rows:6
A A A A A A 
B B B B B 
C C C C 
D D D 
E E 
F 
"""
"""
n= int(input("number of rows:"))
for i in range(n+1):
        
        for j in range(n-i):
                print(chr(65+(n-i-1)),end =' ')
        print()

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
                print(chr(65+(n-i-1)),end =' ')
        print()
        for k in range(n-j):
                print(" ", end=" ")


number of rows:5
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
                print(chr(65+(n-j-1)),end =' ')
        print()
        for k in range(n-j):
                print(" ", end=" ")


number of rows:6
F E D C B A 
  F E D C B 
    F E D C 
      F E D 
        F E 
          F 

"""

"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(chr(65+(n-1)),end =' ')
        print()
        for k in range(n-j):
                print(" ", end=" ")

number of rows:5
E E E E E 
  E E E E 
    E E E 
      E E 
        E

"""
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(" ", end=" ")
        
        for k in range(n-j):
                print(chr(65+(n-1)),end =' ')
        print()

number of rows:5
          E 
        E E 
      E E E 
    E E E E 
  E E E E E


  """

"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(" ", end=" ")
        
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
for i in range(n):
        
        for j in range(n-i):
                print(" ", end=" ")
        
        for k in range(1,n-j):
                print(i,end =' ')
        print()


        number of rows:6
            
          1 
        2 2 
      3 3 3 
    4 4 4 4 
  5 5 5 5 5

  """

"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(" ", end=" ")
        
        for k in range(1,n-j):
                print(k,end =' ')
        print()

number of rows:6
            
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5

"""

"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(" ", end=" ")
        
        for k in range(1,n-j):
                print(chr(65+k-1),end =' ')
        print()

number of rows:6
            
          A 
        A B 
      A B C 
    A B C D 
  A B C D E 


"""
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(chr(65+(i)),end =' ')
        print()
        for k in range(n-j):
                print(" ", end=" ")

number of rows:6
A A A A A A 
  B B B B B 
    C C C C 
      D D D 
        E E 
          F

          """
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(j,end =' ')
        print()
        for k in range(n-j):
                print(" ", end=" ")

number of rows:7
0 1 2 3 4 5 6 
  0 1 2 3 4 5 
    0 1 2 3 4 
      0 1 2 3 
        0 1 2 
          0 1 
            0 


"""
"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(n-j,end =' ')
        print()
        for k in range(n-j):
                print(" ", end=" ")

number of rows:6
6 5 4 3 2 1 
  6 5 4 3 2 
    6 5 4 3 
      6 5 4 
        6 5 
          6 

"""

"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(n-i-1,end =' ')
        print()
        for k in range(n-j):
                print(" ", end=" ")

number of rows:5
4 4 4 4 4 
  3 3 3 3 
    2 2 2 
      1 1 
        0

        """

"""
n= int(input("number of rows:"))
for i in range(n):
        
        for j in range(n-i):
                print(" ", end=" ")
        print()
        for k in range(1,n-j):
                print(i,end =' ')


number of rows:6
            
          
1         
2 2       
3 3 3     
4 4 4 4   
5 5 5 5 5
"""




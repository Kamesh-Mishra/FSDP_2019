
"""
Challenge 4   
    Do all the exception handling for all the extreme use cases 
"""



list1=input('enter comma separated items: ').split(',')
dict1={}
for i in range(len(list1)):
    dict1[i+1]=list1[i]

while True:
    print('''
           enter 'show' to show all items 
          'done' to exit
          'add' to add item at specific index where index is given by user
          'remove' to remover item from a given index''')
    choice=input('what u want to do  : ')
    
    if choice=='show':
        for i, j in dict1.items():
            print(i,' ->',j)
    elif choice.lower()=='add':
        name, pos=input('enter name, position  : ').split(',')
        if int(pos) in dict1.keys():
            pos=int(pos)
            temp1=dict1[pos]
            temp2=''
            n=len(dict1)
            dict1[n+1]=''
            for i in range(n+2):
                if i==pos:
                    dict1[pos]=name
                elif i >pos:
                    temp2=dict1[i]
                    #print(temp2)
                    dict1[i]=temp1
                    temp1=temp2
        else:
            dict1[int(pos)]=name
    elif choice.lower()=='remove' :
        pos=input("enter item's position  : ")
        pos=int(pos)
        dict1.pop(pos)
    elif choice.lower()=='done':
        
        break
        
    else:
        print('Invalid Input')

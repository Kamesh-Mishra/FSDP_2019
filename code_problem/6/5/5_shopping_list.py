
"""
Challenge 5   
    Store the shopping list in a file. 
"""
fp = open("shopping_list_data.txt","w")
list1=input('enter comma separated items: ').split(',')
dict1={}
for i in range(len(list1)):
    dict1[i+1]=list1[i]
# dict1=dict1.fromkeys(list1,0)

while True:
    print('''
           enter 'show' to show all items 
          'done' to exit
          'add' to add item at specific index where index is given by user
          'remove' to remover item from a given index''')
    choice=input('what u want to do  : ')
    
    if choice=='show':
        for i, j in dict1.items():
            fp.writelines(str(i)+'->'+str(j)+"\n")
            print(i,' ->',j)
        fp.close()
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
                    
                         
#             n=len(dict1)+1
#             
#             dict1[pos]=name
#             dict1[n]=temp
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
"""
Name: 
    Supermarket      
Filename:
    supermarket.py 
Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
Sample Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20
""" 




dict1 = {}

while (True):
    entry = input("Enter the record: ")
    if not entry:
        break
    list1 = entry.split()
    value = int(list1[-1])
    key = " ".join(list1[:-1])
   
    if key not in dict1:
        dict1[key] = value
    else:
        dict1[key] = dict1[key] + value

print (dict1)

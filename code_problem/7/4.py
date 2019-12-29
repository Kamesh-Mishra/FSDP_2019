
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

# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

1 Get the corresponding `celsius` values in list

2 Create the `celsius` dictionary

3 convert a dictionary of Fahrenheit temperatures into celsius




Solution:
#Get the corresponding `celsius` values

    

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)


# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
print(celsius_dict)


"""
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}


list1 = list(map(lambda x :(float(5/9)*(x-32)),fahrenheit.values()))
print(list1)



dict1 = dict(zip(fahrenheit.keys(),list1))

print(dict1)




list2 = list(map(lambda x : (x-32)*(5/9),fahrenheit.values()))
dict1 = dict(zip(fahrenheit.keys(),list2))
print(dict1)



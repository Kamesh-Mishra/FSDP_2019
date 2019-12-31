
"""
Challenge 3
    User can enter SHOW or Show or show, 
    similar for DONE and HELP, but the program should do the required job
    Show the item in the list serially starting from 1
    Let us accept items using a comma separated string
        
    Also there should be a functionality to add an item at a specific index
    There should be a functionality to remove items from the list at a specific index using REMOVE
    
    Do all the exception handling for all the extreme use cases 
"""
# User can enter SHOW or Show or show, 
#    similar for DONE and HELP, but the program should do the required job

#   Show the item in the list serially starting from 1

#   Make a list to hold onto our items.
shopping_list = []
def addd(x):
    shopping_list.append(x)
    
# Print out instructions on how to use the app
print ("What should we pick up at the store ?")
print ("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item in ['DONE',"Done","done"]:
        break
    elif new_item in ["SHOW","Show","show"]:
        print("Here is list of all items is:")
        k =  zip(range(1,len(shopping_list)),shopping_list)    
        for i in k:
            print(i)
        
    # add new items to our list
    elif  new_item not in ["SHOW","Show","show",'DONE',"Done","done","HELP","Help","help","CLEAR"]:
        addd(new_item)    
        
    elif new_item in ["HELP","Help","help"]:
        print("Enter 'SHOW' for show all items in list in running progress.")
        print ("Enter 'DONE' to stop adding items.")

    elif new_item == "CLEAR":
        shopping_list.clear()
    
#  print out the list
print("Here’s your list")
for item in shopping_list:
    print ( item )










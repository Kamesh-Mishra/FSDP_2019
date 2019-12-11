
'''########################################################'''
'''########################################################'''
'''########################################################'''


'''Hands On'''
# Take your street address and make it a list variable myaddress
# where each token is an element.

# What would be the code to set the sum of the numerical portions of
# your address list to a variable called address sum?

# What would be the code to change one of the string elements of the
# list to another string (e.g., if your address had "West" in it, how would
# you change that string to "North")?

# Change the street portion of myaddress to have the street first 
# and the building number at the end. 
          



"""
Name:
    Infinite input
Filename: 
    infinite.py    
Problem Statement:
    Write a program that asks the user, again and again, to enter a number.
    When the user enters an empty string, then stop asking for additional inputs.
    Along the way, as the user is entering numbers, 
    I want you to store those numbers in a list. 
    I also want you to keep track of the minimum and maximum values that you've seen so far.
    When the user has finished entering numbers, your program should print out:
         The sum of these numbers
         The average (mean) of these numbers
         The largest and smallest numbers you received from the user
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Use infinite while loop  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available  
    
"""



'''Hand on'''
# remove all 3 from the list
some_list = [1,2,3,5,6,2,4,3,5,6,7,8,1,2,3]



'''########################################################'''
'''########################################################'''
'''########################################################'''

'''Hands On'''
# Take the list of the parts of your street address
# Write a loop that goes through that list and prints out each item in that list
myaddress = [3225, 'West', 'Foster', 'Avenue', 'Chicago', 'IL', 60625]



'''Hands On'''
#Looping through a list of temperatures and applying a test
#Pretend you have the following list of temperatures T:
T = [273.4, 265.5, 277.7, 285.5]
#and a list of flags called Tflags that is initialized to all False
Tflags = [False, False, False, False]
#Write a loop that checks each temperature in T and sets the corresponding
#Tflags element to True if the temperature is above the freezing point of water.





'''Hands On'''
# Clean the Messy salaries into integers for Data Processing
salaries = ['$876,001', '$543,903', '$2453,896'] 


'''Hands On'''
# Create a list of Fibonnaci numbers up to the 50th term.
# The program will then ask the user for which position in the sequence
# they want to know the Fibonacci value for
# The Fibonacci sequence was originally used as a basic model for rabbit population growth:  


'''Hands On'''
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.

words = ['aba', 'xyz', 'aa', 'x', 'bbb']
#words = ['', 'x', 'xy', 'xyx', 'xx']
#words = ['aaa', 'be', 'abc', 'hello']


'''Hands On'''
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

words =['bbb', 'ccc', 'axx', 'xzz', 'xaa']
#words =['ccc', 'bbb', 'aaa', 'xcc', 'xaa']
#words =['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

'''Hands On'''
# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

nums = [1, 2, 2, 3]
#nums = [2, 2, 3, 3, 3]
#nums = []



'''Hands On'''
# Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

list1 = ['aa', 'xx', 'zz'] #['aa', 'xx']         ['aa', 'aa']
list2 = ['bb', 'cc']       #['bb', 'cc', 'zz']   ['aa', 'bb', 'bb']




"""
Name: 
    2 Dimensional Random List         
Filename:
    random_list.py
Problem Statement:
    Create a 2-Dimensional list of list of integers 10 by 10.
    Fill the 2-Dimensional list with random numbers in the range 0 to 255
    Display the array on the screen showing the numbers
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
"""   



"""
Code Challenge
Name: 
    Pattern Builder
Filename: 
    pattern.py
Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input: 
    5
Sample Output:
    Below is the output of execution of this program.
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * 
    * * * 
    * * 
    * 
"""



"""
Name: 
    Treasure Hunt Game         
Filename:
    treasure.py
Problem Statement:
    Create a simple treasure hunt game.
    Create a list of list of integers 10 by 10.
    In a random position in the array store the number 1.
    Get the user to enter coordinates where they think the treasure is.
    If there is a 1 at this position display ‘success’.
    Repeat Until they find the treasure
    Add a feature to say 'hot' 'cold' 'warm' depending on how close their guess 
    was to the actual hidden location.
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
"""   


"""
Name: 
    CodeBreaker         
Filename:
    code_breaker.py
Problem Statement:
    The computer generates a 4 digit code
    The user types in a 4 digit code. Their guess.
    The computer tells them how many digits they guessed correctly
Data:
    Not required
Extension:
    the computer tells them how many digits are guessed correctly 
    in the correct place and how many digits have
    been guessed correctly but in the wrong place.
    The user gets 12 guesses to either 
    WIN – guess the right code. 
    Or
    LOSE – run out of guesses.  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
"""   





"""
Name: 
    Vowels Finder
Filename: 
    vowels.py
Problem Statement:
    Remove all the vowels from the list of states  
Hint: 
    Use nested for loops and while
Data:
    Not required
Extension:
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
Sample Output:
    ['lbm', 'clfrn', 'klhm', 'flrd'] 
"""


"""
Name: 
    Pallindromic Integer
Filename: 
    pallindromic.py
Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)        
Data:
    Not required
Extension:
    Not Available  
Hint: 
    A palindromic number or numeral palindrome is a number that remains the same
    when its digits are reversed. 
    Like 16461, for example, it is "symmetrical"  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    12 9 61 5 14 
Sample Output:
    True     
"""


"""
Name: 
    Centered Average         
Filename:
    centered.py
Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is the 
    mean average of the values, except ignoring the largest and smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. Use int division to produce the final average. 
    You may assume that the array is length 3 or more.
    Take input from user
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    1, 2, 3, 4, 100 
Sample Output:
    3 
"""   


"""
Name: 
    Unlucky 13         
Filename:
    unlucky.py
Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    13, 1, 2, 13, 2, 1, 13 
Sample Output:
    3 
"""   
 

"""
Name: 
    Random Game 2         
Filename:
    randon_game2.py
Problem Statement:
    Write a program for a game where the computer generates a
    random starting number between 20 and 30.
    The player and the computer can remove 1,2 or 3 from the number
    in turns. Something like this...
    Starting number : 25
    How many do you want to remove? 3
    22 left
    Computer removes 2
    20 left
    The player who has to remove the last value to bring the number
    down to 0 is the loser.
    1 left
    Computer removes 1
    You win!
    Easy option
    Get the computer to choose a number between 1—3 at random
    Harder option
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
""" 

"""
Name: 
    Random Game 3         
Filename:
    randon_game3.py
Problem Statement:
    Write a program for a Higher / Lower guessing game
    The computer randomly generates a sequence of up to 10 numbers
    between 1 and 13. The player each after seeing each number
    in turn has to decide whether the next number is higher or lower.
    If you can remember Brucie’s ‘Play your cards right’ it’s basically
    that. If you get 10 guesses right you win the game.
    Starting number : 12
    Higher(H) or lower(L)? L
    Next number 8
    Higher(H) or lower(L)? L
    Next number 11
    You lose
Data:
    Not required
Extension:
    Give the players two lives
    Make sure only H or L can
    be entered  
Hint: 
    Use a condition controlled loop (do until, while etc) to control the
    game. Do not find yourself repeating the same code over and over!
    You don't need to remember all 10 numbers just the current number
    /next number. Don’t forget you’ll have to keep a count of the
    number of turns they’ve had. 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
""" 





'''########################################################'''
'''########################################################'''
'''########################################################'''


'''Hands On'''
# Make a function days_in_month to return the number of days in a specific month of a year

"""
Name: 
    Pangram         
Filename:
    pangram.py
Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    The five boxing wizards jumps. 
    Sphinx of black quartz, judge my vow.
    The jay, pig, fox, zebra and my wolves quack!
    Pack my box with five dozen liquor jugs.
Sample Output:
    NOT PANGRAM 
    PANGRAM
    PANGRAM
    PANGRAM
"""  


"""
Name: 
    Bricks         
Filename:
    bricks.py
Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    2, 2, 11
Sample Output:
    True
""" 



"""
Name: 
    Reverse Function         
Filename:
    reverse.py
Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    I am testing
Sample Output:
    gnitset ma I
""" 



"""
Name: 
    Translate Function         
Filename:
    translate.py
Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    This is fun
Sample Output:
    ToThohisos isos fofunon
""" 



"""
Name: 
    Operations Function         
Filename:
    operation.py
Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    5,2,6,2,3
Sample Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]
""" 

"""
Name: 
    Anagram         
Filename:
    anagram.py
Problem Statement:
    Two words are anagrams if you can rearrange the letters of one to spell the second.  
   For example, the following words are anagrams:
   ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
  
   create a function which takes two arguments and return whether they are angram or no ( True or False)
Data:
    Not required
Extension:
    Not Available  
Hint: 
    How can you tell quickly if two words are anagrams?  
    Try to use set 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 


"""
Name: 
    Playing Cards         
Filename:
    Playing_Cards.py
Problem Statement:
    Write a program that will generate a random playing card 
    e.g. ‘9 Hearts’, ‘Queen Spades’ when the return key is pressed.
    Rather than generate a random number from 1 to 52. 
    Create two random numbers – one for the suit and one for the card.
    However we don't want the same card drawn twice.
Data:
    Not required
Extension:
    Update this program by using an list to prevent the same card being dealt 
    twice from the pack of cards.
    
    Convert this code into a procedure ‘DealCard’ that will display the card dealt or ‘no more cards’.
    Call your procedure 53 times! 
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 


"""
Name: 
    Blackjack         
Filename:
    Blackjack.py
Problem Statement:
    Play a game that draws two random cards.
    The player then decides to draw or stick.
    If the score goes over 21 the player loses (goes ‘bust’).
    Keep drawing until the player sticks.
    After the player sticks draw two computer cards. 
    If the player beats the score they win. 
Data:
    Not required
Extension:
    Aces can be 1 or 11! The number used is whichever gets the highest score.  
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 




'''########################################################'''
'''########################################################'''
'''########################################################'''

"""
Name: 
    Sorting         
Filename:
    sorting.py
Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score 
Data:
    Not required
Extension:
    Aces can be 1 or 11! The number used is whichever gets the highest score.  
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
Sample Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
""" 


"""
Name: 
    generator       
Filename:
    generator.py 
Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    2, 4, 7, 8, 9, 12
Sample Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
""" 

"""
Name: 
    weeks       
Filename:
    weeks.py 
Problem Statement:
    Write a program that adds missing days to existing tuple of days 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
Sample Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
""" 



'''########################################################'''
'''########################################################'''
'''########################################################'''

'''Hands On'''
#Create a dictionary myaddress using your address. 
#Choose relevant keys(they will probably be strings), 
#and separate your address into street address,
#city, state, and postal code portions, all of which are strings (for your ZIP
#Code, don’t enter it in as a number).
myaddress = {'street':'3225 West Foster Avenue','city':'Chicago', 'state':'IL','zip':'60625'}


"""
Name: 
    List of File Names       
Filename:
    list_dict.py 
Problem Statement:
    Assume you’re given the following list of files:
    ist_of_files = ['data0001.txt', 'data0002.txt','data0003.txt']

    Create a dictionary filenum where the keys are the filenames and the
    value is the file number (i.e., data0001.txt has a file number of 1) 
    as an integer.

    Make your code fill the dictionary automatically, assuming that you 
    have a list list of files. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    To convert a string to an integer, use the int function on the string, 
    and the list and array sub-range slicing syntax also works on strings 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 



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


"""
Name: 
    Teen Calculator       
Filename:
    teen_cal.py
Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    from ast import literal_eval
    dict1 = literal_eval("{'a': 2, 'b' : 15, 'c' : 13}") 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    {'a' : 2, 'b' : 15, 'c' : 13}
Sample Output:
    Sum = 17
""" 


"""
Name: 
    Character Frequency       
Filename:
    frequency.py 
Problem Statement:
    This program accepts a string from User and counts the number of characters 
    (character frequency) in the input string. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    www.google.com
Sample Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
""" 

  
"""
Name: 
    Letter Distribution       
Filename:
    letter_dist.py 
Problem Statement:
    Ask the user to enter some text. 
    Display the distribution of letters from within the text. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Use dictionaries to solve 
    import string and use string.ascii_lowercase 
Algorithm:
    Convert all letters to lowercase
    Ignore characters that aren't lowercase letters
    Create a dictionary in which the keys are letters and the values are the counts. 
Boiler Plate Code:
    Not Available 
Sample Input:
    This is a test.  Show me the distribution, already!
Sample Output:
    t: 6 15%
    h: 3 7%
    i: 5 12%
    s: 5 12%
    a: 3 7%
    e: 4 10%
    o: 2 5%
    w: 1 2%
    m: 1 2%
    d: 2 5%
    r: 2 5%
    b: 1 2%
    u: 1 2%
    n: 1 2%
    l: 1 2%
    y: 1 2%
""" 


"""
Name: 
    Digit Letter Counter      
Filename:
    digit_letter_counter.py
Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits 
    and letters. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Store the letters and Digits as keys in the dictionary  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Python 3.2
Sample Output:
    Letters 6 
    Digits 2
""" 


"""
Name: 
    Anagram 2        
Filename:
    anagram2.py
Problem Statement:
    Two words are anagrams if you can rearrange the letters of one to spell the second.  
   For example, the following words are anagrams:
   ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
  
   create a function which takes two arguments and return whether they are angram or no ( True or False)
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Use dictionary to solve it 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 


"""
Name: 
    Sentence       
Filename:
    Sentence.py
Problem Statement:
    You are given a sentence, and want to shift each letter by 2 in alphabet to create a secret code. 
    The sentence you want to encode is the lazy dog jumped over the quick brown 
    fox and the output should be ’vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz’ 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Not Available 
Algorithm:
    Create a dictionary mapping each letter to its number in the alphabet
    Create a dictionary mapping each number to its letter in the alphabet
    Go through each letter in the sentence and find the corresponding number, add 2 and then find the new corresponding letter
    Make sure to take care of the edge cases so that if you get the letter z, it maps to b… ect
    Print the encoded string  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 

 



'''########################################################'''
'''########################################################'''
'''########################################################'''

"""
Name: 
    Intersection       
Filename:
    Intersection.py 
Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 


"""
Name: 
    Duplicate       
Filename:
    Duplicate.py 
Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values with original 
    order reserved 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Distance = (Acceleration*Time*Time ) / 2 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 


"""
Name: 
    Mailing List       
Filename:
    mailing.py 
Problem Statement:
    I recently decided to move a popular community  mailing list 
    (3,000 subscribers, 60-80 postings/day) from my server to Google Groups. 
    I asked people to join the Google-based list themselves, 
    and added many others myself, as the list manager. 
    However, after nearly a week, only half of the list had been moved. 
    I somehow needed to learn which people on the old list hadn't yet signed up 
    for the new list.


    Fortunately, Google will let you export a list of members of a group to CSV format. 
    Also, Mailman (the list-management program I was using on
    my server) allows you to list all of the e-mail addresses being used 
    for a list. Comparing these lists, I think, offers a nice chance to look
    at several different aspects of Python, and to consider how we can 
    solve this real-world problem in a "Pythonic" way.


    The goal of this project is thus to find all of the e-mail addresses on 
    the old list that aren't on the new list. The old list is in a file 
    containing one e-mail address per line
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 

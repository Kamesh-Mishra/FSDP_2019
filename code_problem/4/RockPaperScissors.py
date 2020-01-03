"""
Make a game of rock, paper scissors against the computer. 
Algorithm
    Tell user to enter either rock,paper or scissors
    Get the response
    Generate a random number from 1 to 3 (1=rock,2=paper,3=scissors)
    Compare user selection and computer selection
    Display who wins.

Extension
    Make sure the user enters a valid entry.
    Add a loop structure to play several times and keep a running score
    Make an enumerated variable type to store choices.
"""



while True:
    inp = input("Enter input: ")
    import random
    comp = random.choice([1,2,3])
    
    if inp == "rock":
        i = 1
        if i == comp:
            print("YOU WON")
            continue
        else:
            print("Computer wins")
            continue
    elif inp == "paper":
        i = 2
        if i == comp:
            print("YOU WON")
            continue
        else:
            print("Computer wins")
            continue
    elif inp == "scissors":
        i = 3
        if i == comp:
            print("YOU WON")
            continue
        else:
            print("Computer wins")
            continue
    else:
        print("Please Enter Valid Input.")
        continue

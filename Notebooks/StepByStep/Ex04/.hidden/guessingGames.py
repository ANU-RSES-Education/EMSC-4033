import numpy as np
import time

def guessingGame(nmax=10):
    print("I am thinking of a number between 1 and {}".format(nmax))
    target = np.random.randint(1,nmax+1)
    count = 1
    while True:
        try:
            guess = int(input("Make a guess:"))
        except ValueError:
            print("Please enter an integer.")
            continue
        if guess==target:
            print("Well done! You needed %i guesses."%count)
            break
        else:
            count += 1
            print("Sorry, try again.")
                
        
def higherOrLower(nmax=10):
    print("I am thinking of a number between 1 and {}".format(nmax))
    target = np.random.randint(1,nmax+1)
    count = 1
    while True:
        try:
            guess = int(input("Make a guess:"))
        except ValueError:
            print("Please enter an integer.")
            continue
        if guess<target:
            print("Too low... try again!")
        elif guess>target:
            print("Too high... try again!")
        else:
            print("Well done! You needed %i guesses."%count)
            break
        count +=1

        
def montyHall(nBoxes=3):
    iCash = np.random.randint(1,nBoxes+1)
    #print(iCash)
    print("You have %i numbered boxes. One of them contains $1 million; the\n"
            "others are empty. Which one do you think contains the money?\n"%nBoxes)
    time.sleep(0.5)
    iBox = int(input("Enter a box number: "))
    iMH = iBox
    while iMH==iBox or iMH==iCash:
        iMH = np.random.randint(1,nBoxes+1)
    print("\nYou selected box %i. Let me help you out by opening box %i."%(iBox,iMH))
    print("Look, it's empty. Now which box do you want to choose?\n")
    while True:
        iBox = int(input("Enter a box number: "))
        if iBox == iMH:
            print("I already opened that one! Try again.")
        else:
            break
    print("\nYou selected box %i. Let's open it..."%iBox)

    if iBox==iCash:
        print("\n$$$$$ You won! $$$$$")
    else:
        print("\nSorry! You leave with nothing!")
            
    
import random

comGuess = random.randint(0,100)

while True:
    userguess=int(input("Guess a number between 0-100:"))
    if userguess > comGuess:
        print("Guess lower")
    elif userguess < comGuess:
        print ("Guess higher")
    else:
        print("Congrats, you've guessed the correct number")
        break

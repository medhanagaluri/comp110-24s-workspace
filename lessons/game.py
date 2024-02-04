"""Number guessing game."""
from random import randint

SECRET: int = randint(1,5)
correct: bool = False

while not correct: #correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the number!")
        #something to help us exit
        correct = True
    elif guess > SECRET:
        print(f"{guess} is too high!")
    elif guess < SECRET:
        print(f"{guess} is too low!")
    else:
        print("Guess again!")
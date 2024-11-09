# Question : Number Guessing Game

import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100 : "))
    
    if guess < number:
        print("Too Low! try again...")
    elif guess > number:
        print("Too High! try again...")
    else:
        print("You Won!")
        break

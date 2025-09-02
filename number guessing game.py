import random

number = random.randint(0, 200)
guess = 0

while guess != number:
    guess = int(input("Guess a number (0-200):"))
    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("Correct! The Number Was", number)
        break

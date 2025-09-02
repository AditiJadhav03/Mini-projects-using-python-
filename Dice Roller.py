import random

while True:
    roll = input("Roll the dice? (y/n): ")
    if roll.lower() == 'y':
        dice_roll = random.randint(1, 6)
        print(f"You rolled a {dice_roll}!")
    elif roll.lower() == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
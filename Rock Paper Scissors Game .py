import random
import emoji

choices = ["rock", "paper", "scissors"]
user = input("Enter rock, paper or scissors:").lower()
computer = random.choice(choices)

print("Computer Choices:", computer)

if user == computer:
    print("its a tie! \U0001F60E")
elif user == "rock":
    if computer == "scissors":
        print("You win! \U0001F389")
    else:
        print("You lose! \U0001F622")
elif user == "paper":
    if computer == "rock":
        print("You win! \U0001F389")
    else:
        print("You lose! \U0001F622")
elif user == "scissors":
    if computer == "paper":
        print("You win! \U0001F389")
    else:
        print("You lose! \U0001F622")


# or we can also write the code like this 
#if user == computer:
#print("Its a Tie!")
# elif (user == "rock" and computer == "scissors") or\
#      (user == "paper" and computer == "rock") or\
#      (user == "scissors" and computer == "paper"): 
#    print("You win!")
#  else:
#    print("You lose!")
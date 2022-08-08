import ascii
import random

player = input("What do you choose? Rock, Paper or Scissors.\n")
list_choice = ["Rock", "Paper", "Scissors"]
computer = list_choice[random.randint(0, 2)]

if player.lower() == "rock":
    print("\n" + player)
    print(ascii.rock)
    if computer == "Rock":
        print(computer)
        print(ascii.rock)
        print ("Draw")
    elif computer == "Paper":
        print(computer)
        print(ascii.paper)
        print("You lose")
    elif computer == "Scissors":
        print(computer)
        print(ascii.scissors)
        print("You WIN!")

elif player.lower() == "paper":
    print("\n" + player)
    print(ascii.paper)
    if computer == "Rock":
        print(computer)
        print(ascii.rock)
        print("You WIN!")
    elif computer == "Paper":
        print(computer)
        print(ascii.paper)
        print("Draw")
    elif computer == "Scissors":
        print(computer)
        print(ascii.scissors)
        print("You lose")

elif player.lower() == "scissors":
    print("\n" + player)
    print(ascii.scissors)
    if computer == "Rock":
        print(computer)
        print(ascii.rock)
        print("You lose")
    elif computer == "Paper":
        print(computer)
        print(ascii.paper)
        print("You WIN!")
    elif computer == "Scissors":
        print(computer)
        print(ascii.scissors)
        print("Draw")
else:
    "You didn't choose Rock, Paper or Scissors."

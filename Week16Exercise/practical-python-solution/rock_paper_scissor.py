import random

computer_choice = random.choice(["scissors", "rock", "paper"])

user_choice = input("Do you want - rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "scissors":
    print("WIN")
elif user_choice == "paper" and computer_choice == "rock":
    print("WIN")
else:
    print(f"You lose, computer chose {computer_choice} and wins!!!")
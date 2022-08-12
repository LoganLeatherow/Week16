import random

computer_choice = random.choice(["scissors", 'rock', 'paper'])

user_choice = input('Do you want - rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print('TIE, the computer had ' + computer_choice)
elif user_choice == "rock" and computer_choice == "scissors":
    print('Win, the computer had ' + computer_choice)
elif user_choice == "paper" and computer_choice == "rock":
    print('Win, the computer had ' + computer_choice)
elif user_choice == 'Scissors' and computer_choice == "paper":
    print ('Win, the computer had ' + computer_choice)
else:
    print('Computer Wins, computer had '+ computer_choice)
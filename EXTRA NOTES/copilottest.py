'''
Make a python script that allows you to play rock paper scissors against the computer
until you say quit
'''

import random

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter rock (r), paper (p), scissors (s) or quit: ").lower()
    if user_input == "r":
        user_input = "rock"
    elif user_input == "p":
        user_input = "paper"
    elif user_input == "s":
        user_input = "scissors"
    if user_input == "quit":
        break
    if user_input not in options:
        print("Invalid input. Please try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
        
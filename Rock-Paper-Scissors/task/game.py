# Write your code here
import random

win_pairs = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
while True:
    computer_option = random.choice(["rock", "paper", "scissors"])
    user_option = input()
    if user_option == "!exit":
        break
    elif user_option not in ["rock", "paper", "scissors"]:
        print("Invalid input")
    elif user_option == computer_option:
        print(f"There is a draw ({user_option})")
    elif user_option == win_pairs[computer_option]:
        print(f"Well done. The computer chose {computer_option} and failed")
    elif computer_option == win_pairs[user_option]:
        print(f"Sorry, but the computer chose {computer_option}")


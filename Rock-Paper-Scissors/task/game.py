# Write your code here
import random


class RockPaperScissors:
    win_pairs = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

    def check_result(self, user_opt, computer_opt, user_rate):
        if user_opt == computer_opt:
            print(f"There is a draw ({user_option})")
            user_rate += 50
        elif user_opt == self.win_pairs[computer_opt]:
            print(f"Well done. The computer chose {computer_opt} and failed")
            user_rate += 100
        elif computer_opt == self.win_pairs[user_opt]:
            print(f"Sorry, but the computer chose {computer_opt}")
        return user_rate


class Rating:
    def __init__(self):
        self.rate_dict = {}

    def rate_record(self, file_name, name):
        rate_file = open(file_name, "r")
        rate_list = rate_file.readlines()
        for item in rate_list:
            rate_item = item.split()
            self.rate_dict[rate_item[0]] = rate_item[1]
        rate_file.close()
        user_rate = int(self.rate_dict.get(name, 0))
        return user_rate


my_game = RockPaperScissors()
my_rate = Rating()

name = input("Enter your name: ")
print("Hello,", name)
rate = my_rate.rate_record("rating.txt", name)
while True:
    computer_option = random.choice(["rock", "paper", "scissors"])
    user_option = input()
    if user_option == "!exit":
        print("Bye!")
        break
    elif user_option == "!rating":
        print(f"Your rating: {rate}")
    elif user_option not in ["rock", "paper", "scissors"]:
        print("Invalid input")
    else:
        rate = my_game.check_result(user_option, computer_option, rate)



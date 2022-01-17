# Write your code here
import random


class RockPaperScissors:

    def __init__(self):
        self.win_pairs = {}

    def create_win_pairs(self, opts):
        # create win pair for the first option
        end = int((len(opts) - 1) / 2)
        self.win_pairs[opts[0]] = opts[1:end + 1]
        # create win pair for the last option
        self.win_pairs[opts[-1]] = opts[:end]
        # create win pairs for 1 to len(opts) - 2
        for i in range(1, len(opts) - 1):
            list1 = opts[i + 1:]
            list2 = opts[:i]
            list3 = list1 + list2
            end = int(len(list3) / 2)
            self.win_pairs[opts[i]] = list3[: end]

    def check_result(self, user_opt, computer_opt, user_rate):
        if user_opt == computer_opt:
            print(f"There is a draw ({user_option})")
            user_rate += 50
        elif user_opt in self.win_pairs[computer_opt]:
            print(f"Well done. The computer chose {computer_opt} and failed")
            user_rate += 100
        elif computer_opt in self.win_pairs[user_opt]:
            print(f"Sorry, but the computer chose {computer_opt}")
        return user_rate


class Rating:
    def __init__(self):
        self.rate_dict = {}

    def rate_record(self, file_name, r_name):
        rate_file = open(file_name, "r")
        rate_list = rate_file.readlines()
        for item in rate_list:
            rate_item = item.split()
            self.rate_dict[rate_item[0]] = rate_item[1]
        rate_file.close()
        user_rate = int(self.rate_dict.get(r_name, 0))
        return user_rate


my_game = RockPaperScissors()
my_rate = Rating()

name = input("Enter your name: ")
print("Hello,", name)
rate = my_rate.rate_record("rating.txt", name)
user_in = input()
if user_in:
    options = user_in.split(",")
else:
    options = ["rock", "paper", "scissors"]
print("Okay, let's start")
my_game.create_win_pairs(options)
while True:
    computer_option = random.choice(options)
    user_option = input()
    if user_option == "!exit":
        print("Bye!")
        break
    elif user_option == "!rating":
        print(f"Your rating: {rate}")
    elif user_option not in options:
        print("Invalid input")
    else:
        rate = my_game.check_result(user_option, computer_option, rate)

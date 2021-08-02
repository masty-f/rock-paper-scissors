import random

input("Would you like to play rock, paper, scissors? ")
if "yes":
    print("Okay. Let's play.")

user_wins = 0
ai_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock, paper, or scissors to play, or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue
        # this makes it so that if user does not input rock, paper or scissors, the loop will start back asking them to type rock paper or scissors.

    random_number = random.randint(0, 2) #rock is 0, paper 1, scissors 2
    ai_pick = options[random_number]
    print("AI picked", ai_pick + ".")

    if user_input == "rock" and ai_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and ai_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and ai_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == ai_pick:
        print("That was a tie.")

    else:
        print("You lost.")
        ai_wins += 1

print("Goodbye.")
print("You won", user_wins, "times. The AI won", ai_wins, "times.")




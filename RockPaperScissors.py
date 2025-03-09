import random

Player_wins = 0
Computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    player_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if player_input == "q":
        break

    if player_input not in options:
        continue
    random_number =  random.randint(0, 2) # To represent rock : 0,paper : 1,scissors : 2

    computer_pick = options[random_number]
    print("computer picked",computer_pick + ".")
    if player_input == "rock" and computer_pick == "scissors":
        print("You won!")
        Player_wins += 1

    elif player_input == "paper" and computer_pick == "rock":
        print("You won!")
        Player_wins += 1


    elif player_input == "scissors" and computer_pick == "paper":
        print("You won!")
        Player_wins += 1


    else:
        print("You lost!")
        Computer_wins += 1

print("You won", Player_wins, "times")
print("The computer won", Computer_wins, "times")
if Player_wins < Computer_wins:
    print("You suck at this game! pull up your socks, damn! ")
else:
    print("Not bad at all keep going! ")

print("Try agin next time, you can do better,just keep practicing!")         
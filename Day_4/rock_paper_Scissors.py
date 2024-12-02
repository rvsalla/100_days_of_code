import random

list_rps = ["Rock", "Paper", "Scissors"]

player_choice = list_rps[int(input("Select 0 for Rock, 1 for Paper an 2 fro Scissors: " ))]

machine_choice = random.choice(list_rps)

print(f"you chose -> {player_choice}\n")
print(f"computer chose -> {machine_choice}\n")

if player_choice == machine_choice:
    print("Draw")
elif player_choice == "Rock" and machine_choice == "Scissors" or player_choice == "Paper" and machine_choice == "Rock" or player_choice == "Scissors" and machine_choice == "Paper":
    print("you win")
else:
    print("you lose")
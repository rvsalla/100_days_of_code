import random
import hl_data

def select_option():
    op_a = random.choice(hl_data.data)
    op_b = random.choice(hl_data.data)
    while op_a == op_b:
        op_b = random.choice(hl_data.data)
    return op_a, op_b



print(hl_data.logo)

option_a, option_b = select_option()

print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}. {option_a['follower_count']}")
print(hl_data.vs)
print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}. {option_b['follower_count']}")
player_enter = input("Who has more followers? Type 'A' or 'B': ").upper()

if player_enter == 'A':
    player_choice = option_a
elif player_enter == 'B':
    player_choice = option_b

if player_choice['follower_count'] == max(option_a['follower_count'], option_b['follower_count']):
    print("pass")
else:
    print("not pass")
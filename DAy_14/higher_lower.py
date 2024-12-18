import random
import hl_data

def select_option(player_e):
    if player_e == 0:
        op_a = random.choice(hl_data.data)
    else:
        op_a = player_e
    
    op_b = random.choice(hl_data.data)
    while op_a == op_b:
        op_b = random.choice(hl_data.data)
    return op_a, op_b

def player_enter_check(enter):
    loop = True
    while loop == True:
        if enter in ('A','B'):
            loop = False
            return enter
        else:
            enter = input("\nWrong entry, type 'A' or 'B'. Who has more followers?: ").upper()

def player_enter_compare (op_a, op_b, player_e):
    if player_e == 'A':
        player_choice = op_a
    elif player_e == 'B':
        player_choice = op_b

    if player_choice['follower_count'] == max(op_a['follower_count'], op_b['follower_count']):
        return True, player_choice
    else:
        return False, player_choice

correct_answer = 0
cont = True

print(hl_data.logo)

while cont == True:
    if correct_answer == 0:
        option_a, option_b = select_option(0)
    else:
        option_a, option_b = select_option(player_choice)

    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}. {option_a['follower_count']}")
    print(hl_data.vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}. {option_b['follower_count']}")

    player_enter = player_enter_check(input("Who has more followers? Type 'A' or 'B': ").upper())
    
    cont, player_choice = player_enter_compare(option_a, option_b, player_enter)

    if cont:
        correct_answer += 1
        print("\n"*20)
        print(hl_data.logo)
        print(f"You're right! Current score: {correct_answer}.\n")
    else:
        print(f"\nSorry, that's wrong. Final score: {correct_answer}\n")


import random

it = 0
delaer_cards = []
player_cards = []
dealer_score = -1
is_game_over = False

def draw_card():
    card_list  = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(card_list)

def calc_score(cards):
    '''take a list of cards and return the score calculated from the cards'''
    if sum(cards) == 21 and len(cards) == 2: #blackjack
        return 0
    if 11 in cards and sum(cards) > 11:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(player , dealer):
    if player == dealer:
        return "It's a Draw!"
    elif dealer == 0:
        return "You lose, dealer has Blackjack!"
    elif player == 0:
        return "You win, you have Blackjack!"
    elif dealer > 21:
        return "You lose, you went over 21!"
    elif player > 21:
        return "You win, dealer went over 21!"
    elif player > dealer:
        return "You win!"
    else:
        return "You lose!"

for i in range(2):
    delaer_cards.append(draw_card())
    player_cards.append(draw_card())

while not is_game_over:
    player_score = calc_score(player_cards)
    dealer_score = calc_score(delaer_cards)
    print(f"\nYour cards are {player_cards}, current score: {sum(player_cards)}")
    print(f"Dealer frist card: {delaer_cards[0]}")

    if player_score == 0 or dealer_score == 0 or player_score > 21:
        is_game_over = True
    else:
        hit = input("Do you want another card? (y/n)").lower()
        if hit == 'y':
            player_cards.append(draw_card())
        else:
            is_game_over = True

while dealer_score != 0 and dealer_score < 17:
    delaer_cards.append(draw_card())
    dealer_score = calc_score(delaer_cards)

print(f"\nYour final hand is {player_cards}, final score: {sum(player_cards)}")
print(f"Dealer final hans is {delaer_cards}, final score: {sum(delaer_cards)}")
print(compare_scores(player_score, dealer_score))

#continue_play = input(" Do you want to play some blackjack? (y/n): ").lower()
#
#while continue_play == 'y':
#    hit = 'y'
#    print(f"Your cards are {player_cards}, current score: {sum(player_cards)}")
#    print(f"Dealer frist card: {delaer_cards[1]}")
#    
#
#    while hit == 'y' and sum(player_cards)<21:
#        hit = input("Do you want another card? (y/n)").lower()
#        if hit == 'y':
#            player_cards.append(draw_card())
#            print(f"Your cards are {player_cards}, current score: {sum(player_cards)}")
#            print(f"Dealer frist card: {delaer_cards}")
#        elif hit == 'n':
#            while sum(delaer_cards) < 21:
#                delaer_cards.append(draw_card())
#    
#    print(f"\nYour final hand is {player_cards}, final score: {sum(player_cards)}")
#    print(f"Dealer frist hans: {delaer_cards}, final score: {sum(delaer_cards)}")
#
#
#    continue_play = input(" Do you wanto to continue playing? (y/n): ").lower()
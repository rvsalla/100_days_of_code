#Create base variables

cont = 'Y'
bid_dic = {}

while cont == 'Y':
    name = input('Enter your name: ')
    bid = int(input("Enter your bid: "))
    
    bid_dic[name] = bid
    cont = input("There are any mora bids? (type 'Y' for yes and 'N for no)? ").upper()
    print('\n' *100)

max_bid = 0
winner = ''

for i in bid_dic:
    if bid_dic[i] > max_bid:
        max_bid = bid_dic[i]
        winner = i

print(f"the max bid was ${max_bid}, the winner is {winner}")
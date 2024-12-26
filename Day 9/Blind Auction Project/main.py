# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art

print(art.logo)

def highest_bidder(players):
    winner = ''
    highest_bid = 0
    for i in players:
        if players[i] > highest_bid:
            highest_bid = players[i]
            winner = i
    print(f"The winner is {winner} with highest bid {highest_bid}")

bidding_continue = True
players = {}
while bidding_continue:
    name = input("Enter your name:")
    bid = int(input("Enter your bid:"))
    players[name] = bid
    cont = input("Do you have any other players(yes/no):")
    if cont == 'yes':
        print('\n' * 30)
    else:
        bidding_continue = False
        highest_bidder(players)
import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score, user_cards, computer_cards):
    if u_score == c_score:
        print(f"Your cards {user_cards}. Your score {u_score}. Computer cards {computer_cards}. computer score {c_score}")
        print("It is a draw")
        return
    elif c_score == 0:
        print(f"Your cards {user_cards}. Your score {u_score}. Computer cards {computer_cards}. computer score {c_score}")
        print("Computer wins")
        return
    elif u_score == 0:
        print(f"Your cards {user_cards}. Your score {u_score}. Computer cards {computer_cards}. computer score {c_score}")
        print("You win")
        return
    elif u_score > 21:
        print(f"Your cards {user_cards}. Your score {u_score}. Computer cards {computer_cards}. computer score {c_score}")
        print("Computer wins")
        return
    elif c_score > 21:
        print(f"Your cards {user_cards}. Your score {u_score}. Computer cards {computer_cards}. computer score {c_score}")
        print("You win")
        return
    else:
        if c_score > u_score:
            print(f"Your cards {user_cards}. Your score {u_score}. Computer cards {computer_cards}. computer score {c_score}")
            print("Computer wins")
            return
        else:
            print(f"Your cards {user_cards}. Your score {u_score}. Computer cards {computer_cards}. computer score {c_score}")
            print("You win")
            return

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_cards(user_cards)
        computer_score = calculate_cards(computer_cards)
        print(f"Your cards: {user_cards}, Your total score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Do you wanna add another card? (y/n): ").lower()
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score !=0 and computer_score!=21:
        computer_cards.append(deal_card())
        computer_score = calculate_cards(computer_cards)

    compare(user_score,computer_score, user_cards, computer_cards)

while input("Do you wanna play a game of blackjack?(y/n): ") == 'y':
    print('\n' * 20)
    play_game()

import art
import random
from game_data import data

print(art.logo)

def is_winner(choice_data, compare_data):
    if choice_data['follower_count'] > compare_data['follower_count']:
        return True
    else:
        return False

def end_game():
    global game_over
    print(f"Sorry that's wrong. Final score: {count}")
    game_over = False

count = 0
game_over = True
celebrities = data

choice1 = random.choice(celebrities)
celebrities.remove(choice1)
choice2 = random.choice(celebrities)
celebrities.remove(choice2)


while len(celebrities) > 0 and game_over == True:
    print(f"Compare A: {choice1['name']}, {choice1['description']}, from {choice1['country']}")
    print(art.vs)
    print(f"Compare B: {choice2['name']}, {choice2['description']}, from {choice2['country']}")

    user_choice = input("Who has more followers? ('A'/'B'): ").lower()

    if user_choice == 'a':
        winner = is_winner(choice1,choice2)
        if winner:
            count += 1
            print(f"You're right. Current score: {count}")
            choice2 = random.choice(celebrities)
            celebrities.remove(choice2)
        else:
            end_game()
    else:
        winner = is_winner(choice2, choice1)
        if winner:
            count += 1
            print(f"You're right. Current score: {count}")
            choice1 = choice2
            choice2 = random.choice(celebrities)
            celebrities.remove(choice2)
        else:
            end_game()

import random

print("Welcome to number guessing name!")

game_continue = True

def number_operation():
    print("Choose number range: ")
    num1 = int(input("Enter low end number: "))
    num2 = int(input("Enter high end number: "))
    print(f"I am thinking a number between {num1} and {num2}")
    return random.randint(num1,num2)

def lives_operation(choice):
    global game_continue
    if choice == 'easy':
        return 10
    elif choice == 'hard':
        return 5
    else:
        print("Wrong value entered")
        print("Goodbye")
        game = False
        return 0

def game(random_number, lives):
    for i in range(lives):
        print(f"You have {lives} lives remaining: to guess the number")
        player = int(input("Make a guess: "))
        if player > random_number:
            print("Too high")
            lives -= 1
        elif random_number > player:
            print("Too low")
            lives -= 1
        else:
            print("You win")
            return


while game_continue:
    random_number = number_operation()
    choice = input("Choose a difficulty: ('easy'/ 'hard'): ")
    lives = lives_operation(choice)
    game(random_number,lives)
    play_again = input("Do you wanna play again? ('y'/'n')").lower()
    if play_again == 'n':
        print("Goodbye")
        game_continue = False





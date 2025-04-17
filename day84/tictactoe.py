def print_board(board):
    
    print("\n")

    for row in board:

        print(" | ".join(row))

        print("-" * 9)

    print()



def check_winner(board, player):

    # Check rows, columns, and diagonals

    for row in board:

        if all(cell == player for cell in row):

            return True

    for col in range(3):

        if all(board[row][col] == player for row in range(3)):

            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):

        return True

    return False



def is_full(board):

    return all(cell != " " for row in board for cell in row)



def tic_tac_toe():

    board = [[" " for _ in range(3)] for _ in range(3)]

    current_player = "X"



    print("Welcome to Tic Tac Toe!")

    print_board(board)



    while True:

        try:

            move = input(f"Player {current_player}, enter your move (row and column: 1 2): ")

            row, col = map(int, move.split())

            row -= 1

            col -= 1



            if board[row][col] != " ":

                print("That spot is taken. Try again.")

                continue



            board[row][col] = current_player

            print_board(board)



            if check_winner(board, current_player):

                print(f"? Player {current_player} wins!")

                break



            if is_full(board):

                print("It's a draw! ?")

                break



            # Switch players

            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):

            print("Invalid input. Please enter row and column numbers between 1 and 3.")



if __name__ == "__main__":

    tic_tac_toe()


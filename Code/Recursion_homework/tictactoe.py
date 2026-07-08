wins = [
    (0, 1, 2), (0, 3, 6), (3, 4, 5), (1, 4, 7),
    (6, 7, 8), (2, 5, 8), (0, 4, 8), (2, 4, 6)
]

print("Wwelcome to Tic Tac Toe!")


def is_win(board, player):
    for num1, num2, num3 in wins:
        if board[num1] == player and board[num2] == player and board[num3] == player:
            return True
    return False


def turn(board, turns, player):
    num = int(input(f"Player {player}'s turn! Which square do you want to take (1-9): "))

    if num < 1 or num > 9:
        print("Please choose a number between 1 and 9.")
        return turn(board, turns, player)

    if board[num - 1] == num:
        board[num - 1] = player
        turns += 1
    else:
        print("This square is already taken try again!")
        return turn(board, turns, player)

    return turns


def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("-----------")
    print(board[3], "|", board[4], "|", board[5])
    print("-----------")
    print(board[6], "|", board[7], "|", board[8])
    print()


def tic_tac_toe():
    X_wins = 0
    O_wins = 0
    ties = 0
    rounds_played = 0

    play_again = "Y"

    while play_again.upper() == "Y":

        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        player = "X"
        turns = 0
        win = False

        while turns < 9 and not win:

            print_board(board)

            turns = turn(board, turns, player)

            if is_win(board, player):
                print_board(board)
                print(f" Player {player} wins!")

                if player == "X":
                    X_wins += 1
                else:
                    O_wins += 1

                win = True

            elif turns == 9:
                print_board(board)
                print("it's a tie!")
                ties += 1

            if not win:
                if player == "X":
                    player = "O"
                else:
                    player = "X"

        rounds_played += 1

        print(f"Rounds Played: {rounds_played}")
        print(f"X Wins: {X_wins}")
        print(f"O Wins: {O_wins}")
        print(f"Ties: {ties}")


        play_again = input("Do you want to play another round? (y for yes, n for noo): ")

    print("Thanks for playying!")



tic_tac_toe()
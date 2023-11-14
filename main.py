import copy

X = 'X'
O = 'O'


def print_board(matrix):
    hr = "----------------"
    for row in matrix:
        print(hr)

        line = ""
        for x in list(row):
            line += f"  {x}  |"
        print(line[:-1])

    print(hr)


def get_player_sign():
    while True:
        choice = input("Pick up your sign: x/o\n")
        if choice.lower() == 'x':
            return X, O
        elif choice.lower() == 'o':
            return O, X
        else:
            print("Invalid input. Please choose 'x' or 'o'.")


def get_player_move(board):
    print("Your turn. What's your move?")
    print("Type x-y, x for row and y for column. From 1 to 3")

    while True:
        try:
            choice = input()
            row, column = map(int, choice.split('-'))

            # Adjust indices to 0-based
            row -= 1
            column -= 1

            # Check if indices are within the valid range and the selected cell is empty
            if 0 <= row < 3 and 0 <= column < 3 and board[row][column] == '':
                return row, column
            else:
                print("Invalid choice, please pick a cell that exists and isn't picked")
        except (ValueError, IndexError):
            print("Invalid input. Please use the format 'x-y', where x and y are numbers from 1 to 3.")


def draw(player, board, row, column):
    board[row][column] = player


def get_agent_move(agent, board):
    moves = []

    for row in range(3):
        for column in range(3):
            if board[row][column] == '':
                temp_board = copy.deepcopy(board)
                temp_board[row][column] = agent
                value = calculate_board_value(temp_board)
                moves.append((value, row, column))

    if agent == 'X':
        best_move = max(moves, key=lambda x: x[0])
    else:
        best_move = min(moves, key=lambda x: x[0])

    return best_move[1], best_move[2]


def calculate_line_value(line):
    """
    Calculate the value of a line (row, column, or diagonal) for a player.
    Positive values represent the player's signs, and negative values represent the agent's signs.
    """
    x_count = line.count(X)
    o_count = line.count(O)
    empty_count = line.count('')

    if x_count == 3:
        return 1000  # X wins
    elif o_count == 3:
        return -1000  # O wins
    elif x_count == 2 and empty_count == 1:
        return 50  # Two in a row for x
    elif o_count == 2 and empty_count == 1:
        return -50  # Two in a row for o
    elif x_count == 1 and empty_count == 2:
        return 10  # One for x
    elif o_count == 1 and empty_count == 2:
        return -10  # One for o
    else:
        return 0  # No one can win this line


def calculate_board_value(board):
    value = 0
    for row in board:
        value += calculate_line_value(row)

    for col in range(3):
        column = [board[row][col] for row in range(3)]
        value += calculate_line_value(column)

    diagonal = []
    for i in range(3):
        diagonal.append(board[i][i])
        value += calculate_line_value(diagonal)

    diagonal = []
    for i in range(3):
        diagonal.append(board[i][2 - i])
        value += calculate_line_value(diagonal)

    return value


def game_won(value):
    return value > 500 or value < -500  # Arbitrary value, if passed we can tell game's over


def game_tied(board):
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True


def player_turn(board, player):
    while True:
        row, column = get_player_move(board)
        if board[row][column] == '':
            board[row][column] = player
            break
        else:
            print("Cell is already taken. Try again.")


def agent_turn(board, agent):
    row, column = get_agent_move(agent, board)
    board[row][column] = agent


def decide_start(board, agent):
    choice = input("Press ! if you want the agent to play first\n")
    if choice == '!':
        draw(agent, board, 1, 1)
        print_board(board)


def main():
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    print("Welcome to x/o! Good luck")

    player, agent = get_player_sign()

    decide_start(board, agent)

    while True:
        player_turn(board, player)
        print_board(board)
        print_board(board)
        if game_result(board, player):
            print("Nice one!")
            break

        agent_turn(board, agent)
        print_board(board)
        if game_result(board, agent):
            print("Better luck next time!")
            break


def game_result(board, current_player):
    value = calculate_board_value(board)
    if game_won(value):
        print(f"{current_player} wins!")
        return True
    elif game_tied(board):
        print("Game tied")
        return True
    return False


if __name__ == '__main__':
    main()

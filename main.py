import copy

X = 'X'
O = 'O'
WIN = 1000
TWO_ROW = 50
SINGLE_ROW = 10


def print_board(matrix):
    """
    Receives a board and prints it nicely
    :param matrix: A list of 3 lists, each contains 3 values.
    :return: Nothing, just prints
    """
    hr = "----------------"
    for row in matrix:
        print(hr)

        line = ""
        for x in list(row):
            line += f"  {x}  |"
        print(line[:-1])

    print(hr)


def get_player_sign():
    """
    Here the player choose whether he wants to play as X or O
    :return: Player's symbol and agent's symbol, in their order
    """
    while True:
        choice = input("Pick up your sign: x/o\n")
        if choice.lower() == 'x':
            return X, O
        elif choice.lower() == 'o':
            return O, X
        else:
            print("Invalid input. Please choose 'x' or 'o'.")


def get_player_move(board):
    """
    Asks the player to provide next move, and validate the syntax and move
    :param board: The current board
    :return: The row and column to update in the board
    """
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
    """
    Updates the board with the player's sign in the received row and column
    :param player: The player's sign, X or O
    :param board: The current board
    :param row: Row to update
    :param column: Column to update
    :return: Nothing, just updates the board
    """
    board[row][column] = player


def get_agent_move(agent, board):
    """
    The agent tests all possible moves, calculates their values and picks
    The row and column that will give him the best value
    :param agent: The agent's symbol, X or O
    :param board: The current board
    :return: The row and column that will work best for agent
    """
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
    Positive values represent X signs, and negative values represent O signs.
    :param line: A list of 3 values, can represnt row, column or diagonal
    :return: The value of the received line
    """
    x_count = line.count(X)
    o_count = line.count(O)
    empty_count = line.count('')

    if x_count == 3:
        return WIN  # X wins
    elif o_count == 3:
        return -WIN  # O wins
    elif x_count == 2 and empty_count == 1:
        return TWO_ROW  # Two in a row for x
    elif o_count == 2 and empty_count == 1:
        return -TWO_ROW  # Two in a row for o
    elif x_count == SINGLE_ROW and empty_count == 2:
        return 10  # One for x
    elif o_count == SINGLE_ROW and empty_count == 2:
        return -10  # One for o
    else:
        return 0  # No one can win this line


def calculate_board_value(board):
    """
    Returns the value that represents the current state of the board
    Positive value is good for X. Negative value is good for O.
    :param board: The current board
    :return: The value of the current board
    """
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
    """
    Returns whether this game is won by X or Y
    Since 1000/-1000 represent a win, and at most the loser can gain 150 value,
    Checking above or below win value should be sufficient
    :param value: A value of a board
    :return: True if the game is won by any side, false otherwise
    """
    return value > WIN - 3 * TWO_ROW or value < -WIN + 3 * TWO_ROW  # Arbitrary value, if passed we can tell game's over


def game_tied(board):
    """
    Checks if there are no more valid moves left
    :param board: The current board
    :return: True if there are no more valid moves left, false otherwise
    """
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True


def player_turn(board, player):
    """
    Represents the player's turn
    Calls a function to get input then validate it
    Updates the board when good input received
    :param board: The current board
    :param player: The player's sign, X or O
    :return: Nothing, just updates the board
    """
    while True:
        row, column = get_player_move(board)
        if board[row][column] == '':
            draw(player, board, row, column)
            break
        else:
            print("Cell is already taken. Try again.")


def agent_turn(board, agent):
    """
    Represents agent turn, picks a move and draws it
    :param board: The current board
    :param agent: The agent's sign, X or O
    :return: Nothing, just updates the board
    """
    row, column = get_agent_move(agent, board)
    draw(agent, board, row, column)


def decide_start(board, agent):
    """
    Decides whether player starts or agent starts.
    If agent starts, it will always pick cell [2,2] as it's the optimal choice
    :param board: The current board
    :param agent: The agent's sign, X or Y
    :return: Nothing, just updates the board if needed
    """
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

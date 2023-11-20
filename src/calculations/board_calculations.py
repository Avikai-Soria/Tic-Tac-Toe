from typing import Union

from src.states.board_states import is_game_won, is_game_tied
from src.utils import X, O, WIN, TWO_ROW, SINGLE_ROW


def calculate_line_value(line: list[str]) -> int:
    """
    Calculate the value of a line (row, column, or diagonal) for a player.
    Positive values represent X signs, and negative values represent O signs.
    :param line: A list of 3 values, can represent row, column or diagonal
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
    elif x_count == 1 and empty_count == 2:
        return SINGLE_ROW  # One for x
    elif o_count == 1 and empty_count == 2:
        return -SINGLE_ROW  # One for o
    return 0  # No one can win this line


def calculate_board_value(board: list[list[str]]) -> int:
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


def get_game_result(board) -> Union[str, None]:
    """
    Calculates the current board's result
    :param board: The current board
    :return: If there's a result, return the winner (X/Y) or "Tie".
    If the game isn't over, returns None
    """
    if is_game_tied(board):  # Quicker check so better to run first
        return "Tie"

    value = calculate_board_value(board)
    if is_game_won(value):
        if value > 0:  # Positive values are good for X, negative for O
            return "X"
        else:
            return "O"

    return None  # The game isn't over

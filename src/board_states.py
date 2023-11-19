from src.utility import WIN, TWO_ROW


def is_game_won(value: int) -> bool:
    """
    Returns whether this game is won by X or Y
    Since 1000/-1000 represent a win, and at most the loser can gain 150 value,
    Checking above or below win value should be sufficient
    :param value: A value of a board
    :return: True if the game is won by any side, false otherwise
    """
    return value > WIN - 3 * TWO_ROW or value < -WIN + 3 * TWO_ROW  # Arbitrary value, if passed we can tell game's over


def is_game_tied(board: list[list[str]]) -> bool:
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

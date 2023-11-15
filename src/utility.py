from src.logger_setup import global_logger as logger

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
        logger.info(hr)

        line = ""
        for x in list(row):
            line += f"  {x}  |"
        logger.info(line[:-1])

    logger.info(hr)


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

import copy

from src.calculations.board_calculations import calculate_board_value
from src.utils.utils import draw


def play_agent_turn(board, agent):
    """
    Represents agent turn, picks a move and draws it
    :param board: The current board
    :param agent: The agent's sign, X or O
    :return: Nothing, just updates the board
    """
    row, column = get_agent_move(agent, board)
    draw(board, agent, row, column)


def get_agent_move(agent, board) -> tuple[int, int]:
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

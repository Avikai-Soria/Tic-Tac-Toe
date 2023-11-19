from src.utils.logger_setup import global_logger as logger
from src.utils.utils import X, O, draw, print_board


def decide_players_marks():
    """
    Here the player choose whether he wants to play as X or O
    Includes input's validation
    :return: Player's symbol and agent's symbol, in their order
    """
    while True:
        choice = input("Pick up your sign: x/o\n").lower()
        if choice == 'x':
            return X, O
        elif choice == 'o':
            return O, X
        else:
            logger.info("Invalid input. Please choose 'x' or 'o'.")


def decide_player_turn(board: list[list[str]], player: str):
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
            draw(board, player, row, column)
            break
        else:
            logger.info("Cell is already taken. Try again.")


def get_player_move(board: list[list[str]]):
    """
    Asks the player to provide next move, and validate the syntax and move
    :param board: The current board
    :return: The row and column to update in the board
    """
    logger.info("Your turn. What's your move?")
    logger.info("Type x-y, x for row and y for column. From 1 to 3")

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
                logger.info("Invalid choice, please pick a cell that exists and isn't picked")
        except (ValueError, IndexError):
            logger.info("Invalid input. Please use the format 'x-y', where x and y are numbers from 1 to 3.")


def decide_who_starts(board: list[list[str]], agent_mark: str):
    """
    Decides whether the player starts first.
    If agent starts, it will always pick cell [2,2] as it's the optimal choice.
    :param board: The current board.
    :param agent_mark: The agent's sign, X or Y.
    :return: Nothing, just updates the board if needed.
    """
    while True:
        choice = input("Do you want to play first? (y/n): ").lower()

        if choice == 'y':
            return
        elif choice == 'n':
            draw(board, agent_mark, 1, 1)  # Assuming draw is a function that makes a move on the board
            print_board(board)
            return
        else:
            logger.info("Invalid input. Please enter 'y' or 'n'.")

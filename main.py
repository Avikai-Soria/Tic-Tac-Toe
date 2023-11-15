from src.agent_logic import agent_turn
from src.board_calculations import calculate_board_value
from src.board_states import game_won, game_tied
from src.handle_player_choice import get_player_sign, decide_start, player_turn
from src.logger_setup import global_logger as logger
from src.utility import print_board


def main():
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    logger.info("Let's play tic tac toe! Good luck")

    player, agent = get_player_sign()

    decide_start(board, agent)

    while True:
        player_turn(board, player)
        print_board(board)
        if game_result(board, player):
            logger.info("Nice one!")
            break

        agent_turn(board, agent)
        print_board(board)
        if game_result(board, agent):
            logger.info("Better luck next time!")
            break


def game_result(board, current_player):
    value = calculate_board_value(board)
    if game_won(value):
        logger.info(f"{current_player} wins!")
        return True
    elif game_tied(board):
        logger.info("Game tied")
        return True
    return False


if __name__ == '__main__':
    main()

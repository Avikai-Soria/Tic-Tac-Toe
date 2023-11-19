from src.handle_player_choice import decide_players_marks, decide_who_starts, decide_player_turn
from src.logger_setup import global_logger as logger
from src.run_game import run_game

EMPTY_BOARD: list[list[str]] = [['', '', ''], ['', '', ''], ['', '', '']]


def main():
    board: list[list[str]] = EMPTY_BOARD
    logger.info("Let's play tic tac toe! Good luck")

    player_mark: str
    agent_mark: str

    player_mark, agent_mark = decide_players_marks()

    decide_who_starts(board, agent_mark)

    result: str = run_game(board, player_mark, agent_mark)

    logger.info(f"The result of the match is {result}.")

    if result == player_mark:
        logger.info("Nice one!")
    elif result == "Tie":
        logger.info("Good try")
    else:
        logger.info("Better luck next time!")


if __name__ == '__main__':
    main()

from src.logic.agent_logic import play_agent_turn
from src.calculations.board_calculations import get_game_result
from src.user_input.handle_player_choice import decide_player_turn
from src.utils.utils import print_board


def run_game(board: list[list[str]], player_mark: str, agent_mark: str) -> None:
    """
    This function lets the player pick moves, then lets the agent pick his move, until someone wins.
    :param board: The initial board.
    :param player_mark: The mark of the player, x or o.
    :param agent_mark: The mark of the agent, x or o.
    :return: The result of the game (winner or "Tie").
    """
    while True:
        decide_player_turn(board, player_mark)
        print_board(board)
        result: str = get_game_result(board)
        if result is not None:  # Game is over
            return result

        play_agent_turn(board, agent_mark)
        print_board(board)
        result: str = get_game_result(board)
        if result is not None:  # Game is over
            return result

import unittest
from unittest.mock import patch, MagicMock
from src.logger_setup import global_logger as logger
from src.handle_player_choice import get_player_sign, get_player_move, decide_start, player_turn
from src.utility import X, O, draw


class TestHandlePlayerChoiceFunctions(unittest.TestCase):

    def setUp(self):
        # Initialize a 3x3 empty board for testing
        self.empty_board = [['', '', ''],
                            ['', '', ''],
                            ['', '', '']]

    def test_get_player_sign_x(self):
        with patch('builtins.input', return_value='x'):
            player_sign, agent_sign = get_player_sign()
        self.assertEqual(player_sign, X)
        self.assertEqual(agent_sign, O)

    def test_get_player_sign_o(self):
        with patch('builtins.input', return_value='o'):
            player_sign, agent_sign = get_player_sign()
        self.assertEqual(player_sign, O)
        self.assertEqual(agent_sign, X)

    @patch('builtins.input', side_effect=['2-2'])
    def test_get_player_move_valid(self, mock_input):
        player_move = get_player_move(self.empty_board)  # Assuming you have self.empty_board in your class
        self.assertEqual(player_move, (1, 1))

    @patch('builtins.input', side_effect=['4', '2-2'])
    def test_get_player_move_invalid_then_valid(self, mock_input):
        player_move = get_player_move(self.empty_board)  # Assuming you have self.empty_board in your class
        self.assertEqual(player_move, (1, 1))

    @patch('builtins.input', side_effect=['1-1', '0-2', '2-2'])
    def test_get_player_move_invalid_then_valid_twice(self, mock_input):
        player_move = get_player_move(self.empty_board)  # Assuming you have self.empty_board in your class
        self.assertEqual(player_move, (0, 0))


class TestGameLogicFunctions(unittest.TestCase):

    def setUp(self):
        # Initialize a 3x3 empty board for testing
        self.empty_board = [['', '', ''],
                            ['', '', ''],
                            ['', '', '']]

    @patch('builtins.input', return_value='!')
    def test_decide_start_agent_starts(self, mock_input):
        with patch('src.utility.draw') as mock_draw:
            decide_start(self.empty_board, O)
        mock_draw.assert_called_with(O, self.empty_board, 1, 1)

    @patch('builtins.input', return_value='anything_but_exclamation_mark')
    def test_decide_start_player_starts(self, mock_input):
        with patch('src.utility.draw') as mock_draw:
            decide_start(self.empty_board, O)
        mock_draw.assert_not_called()

    @patch('src.handle_player_choice.get_player_move', return_value=(1, 1))
    @patch('src.utility.draw')
    def test_player_turn_valid_move(self, mock_draw, mock_get_player_move):
        player_turn(self.empty_board, X)
        mock_get_player_move.assert_called_once()
        mock_draw.assert_called_once_with(X, self.empty_board, 1, 1)

    @patch('src.handle_player_choice.get_player_move', side_effect=[(1, 1), (0, 0)])
    @patch('src.utility.draw')
    @patch('src.logger_setup.logger.info')
    def test_player_turn_invalid_then_valid_move(self, mock_logger_info, mock_draw, mock_get_player_move):
        player_turn(self.empty_board, X)
        self.assertEqual(mock_get_player_move.call_count, 2)
        mock_draw.assert_called_once_with(X, self.empty_board, 0, 0)
        mock_logger_info.assert_called_with("Cell is already taken. Try again.")


if __name__ == '__main__':
    unittest.main()

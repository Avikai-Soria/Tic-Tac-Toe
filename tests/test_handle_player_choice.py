import unittest
from unittest.mock import patch, MagicMock
from src.logger_setup import global_logger as logger
from src.handle_player_choice import decide_players_marks, get_player_move, decide_who_starts, decide_player_turn
from src.utility import X, O, draw


class TestHandlePlayerChoiceFunctions(unittest.TestCase):

    def setUp(self):
        # Initialize a 3x3 empty board for testing
        self.empty_board = [['', '', ''],
                            ['', '', ''],
                            ['', '', '']]

    def test_get_player_sign_x(self):
        with patch('builtins.input', return_value='x'):
            player_sign, agent_sign = decide_players_marks()
        self.assertEqual(player_sign, X)
        self.assertEqual(agent_sign, O)

    def test_get_player_sign_o(self):
        with patch('builtins.input', return_value='o'):
            player_sign, agent_sign = decide_players_marks()
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
                decide_who_starts(self.empty_board, 'O')
            mock_input.assert_called_with("Do you want to play first? (y/n): ")
            mock_draw.assert_not_called()

        @patch('builtins.input', side_effect=['y'])
        def test_decide_start_player_starts(self, mock_input):
            with patch('src.utility.draw') as mock_draw:
                decide_who_starts(self.empty_board, 'O')
            mock_input.assert_called_with("Do you want to play first? (y/n): ")
            mock_draw.assert_called_once()

        @patch('builtins.input', side_effect=['n'])
        def test_decide_start_player_does_not_start(self, mock_input):
            with patch('src.utility.draw') as mock_draw:
                decide_who_starts(self.empty_board, 'O')
            mock_input.assert_called_with("Do you want to play first? (y/n): ")
            mock_draw.assert_not_called()

        @patch('builtins.input', side_effect=['anything_but_exclamation_mark'])
        def test_decide_start_invalid_input(self, mock_input):
            with patch('builtins.print') as mock_print:
                with self.assertRaises(SystemExit):
                    decide_who_starts(self.empty_board, 'O')
            mock_input.assert_called_with("Do you want to play first? (y/n): ")
            mock_print.assert_called_with("Invalid input. Please enter 'y' or 'n'.")

    @patch('src.handle_player_choice.get_player_move', return_value=(1, 1))
    def test_player_turn_valid_move(self, mock_get_player_move):
        decide_player_turn(self.empty_board, X)
        mock_get_player_move.assert_called_once()


if __name__ == '__main__':
    unittest.main()

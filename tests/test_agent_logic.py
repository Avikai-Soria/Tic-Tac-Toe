import unittest
from unittest.mock import patch
from src.logic.agent_logic import play_agent_turn, get_agent_move
from src.utils import X, O


class TestAgentLogicFunctions(unittest.TestCase):

    @patch('src.logic.get_agent_move', return_value=(1, 1))
    def test_agent_turn(self, mock_get_agent_move):
        board = [
            ['X', '', 'O'],
            ['', 'O', ''],
            ['', 'X', 'X']
        ]
        play_agent_turn(board, X)
        mock_get_agent_move.assert_called_once_with(X, board)

    def test_get_agent_move_x_agent(self):
        board = [
            ['X', '', 'O'],
            ['', 'O', ''],
            ['', 'X', 'X']
        ]
        result = get_agent_move(X, board)
        self.assertIn(result, [(0, 1), (2, 0), (2, 2)])

    def test_get_agent_move_o_agent(self):
        board = [
            ['X', '', 'O'],
            ['', 'O', ''],
            ['O', 'X', 'X']
        ]
        result = get_agent_move(O, board)
        self.assertIn(result, [(0, 1), (1, 0), (1, 2)])


if __name__ == '__main__':
    unittest.main()

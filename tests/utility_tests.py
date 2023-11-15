import unittest
from unittest.mock import patch
from src.utility import print_board, draw, X, O


class TestUtilityFunctions(unittest.TestCase):

    def setUp(self):
        # Initialize a 3x3 empty board for testing
        self.empty_board = [["", "", ""],
                            ["", "", ""],
                            ["", "", ""]]

    def test_print_board(self):
        with patch('src.utility.logger') as mock_logger:
            print_board(self.empty_board)

        self.assertEqual(mock_logger.info.call_count, 7)

    def test_draw(self):
        player = X
        row = 0
        column = 1

        draw(player, self.empty_board, row, column)

        # Check if the board was updated correctly
        self.assertEqual(self.empty_board[row][column], player)


if __name__ == '__main__':
    unittest.main()

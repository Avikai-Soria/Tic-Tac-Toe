import unittest
from src.utility import WIN, TWO_ROW
from src.board_states import is_game_won, is_game_tied


class TestGameStateFunctions(unittest.TestCase):

    def test_game_won_positive(self):
        # Test when value is greater than WIN - 3 * TWO_ROW
        value = WIN - 2 * TWO_ROW
        result = is_game_won(value)
        self.assertTrue(result)

    def test_game_won_negative(self):
        # Test when value is less than -WIN + 3 * TWO_ROW
        value = -WIN + 2 * TWO_ROW
        result = is_game_won(value)
        self.assertTrue(result)

    def test_game_won_not_won(self):
        # Test when value is within the range to not be considered a win
        value = 0
        result = is_game_won(value)
        self.assertFalse(result)

    def test_game_tied_not_tied(self):
        # Test when there are still valid moves left on the board
        board = [['X', 'O', ''],
                 ['', 'X', 'O'],
                 ['O', 'X', '']]
        result = is_game_tied(board)
        self.assertFalse(result)

    def test_game_tied_tied(self):
        # Test when there are no more valid moves left on the board
        board = [['X', 'O', 'X'],
                 ['X', 'O', 'O'],
                 ['O', 'X', 'X']]
        result = is_game_tied(board)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

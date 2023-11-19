import unittest
from src.utils import X, O, WIN, TWO_ROW, SINGLE_ROW
from src.calculations.board_calculations import calculate_line_value, calculate_board_value


class TestBoardCalculationsFunctions(unittest.TestCase):

    def test_calculate_line_value_x_wins(self):
        line = [X, X, X]
        result = calculate_line_value(line)
        self.assertEqual(result, WIN)

    def test_calculate_line_value_o_wins(self):
        line = [O, O, O]
        result = calculate_line_value(line)
        self.assertEqual(result, -WIN)

    def test_calculate_line_value_two_row_x(self):
        line = [X, X, '']
        result = calculate_line_value(line)
        self.assertEqual(result, TWO_ROW)

    def test_calculate_line_value_two_row_o(self):
        line = [O, O, '']
        result = calculate_line_value(line)
        self.assertEqual(result, -TWO_ROW)

    def test_calculate_line_value_single_row_x(self):
        line = [X, '', '']
        result = calculate_line_value(line)
        self.assertEqual(result, SINGLE_ROW)

    def test_calculate_line_value_single_row_o(self):
        line = [O, '', '']
        result = calculate_line_value(line)
        self.assertEqual(result, -SINGLE_ROW)

    def test_calculate_line_value_no_one_wins(self):
        line = [X, O, '']
        result = calculate_line_value(line)
        self.assertEqual(result, 0)

    def test_calculate_board_value_x_wins(self):
        board = [
            [X, O, O],
            ['', X, ''],
            ['', O, X]
        ]
        result = calculate_board_value(board)
        self.assertTrue(result > WIN - 3 * TWO_ROW)

    def test_calculate_board_value_o_wins(self):
        board = [
            [X, O, ''],
            ['', O, ''],
            [X, O, X]
        ]
        result = calculate_board_value(board)
        self.assertTrue(result < -WIN + 3 * TWO_ROW)

    def test_calculate_board_value_no_one_wins(self):
        board = [
            [X, O, ''],
            ['', '', ''],
            ['O', 'X', '']
        ]
        result = calculate_board_value(board)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()

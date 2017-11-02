
import unittest
from GameBoard import GameBoard


class Test_GameBoard(unittest.TestCase):

    # Kinda dumb test, but it's a start!
    def test_board_grid(self):
        gb = GameBoard()
        grid = gb.grid

        self.assertEqual(len(grid), gb.size, "Grid row count OK")
        for row in grid:
            self.assertEqual(len(row), gb.size, "Grid row count OK")

    #
    def test_create_board(self):
        gb = GameBoard()
        gb.create_board("0A1 0A1 0A1")

if __name__ == '__main__':
	unittest.main(verbosity=2)



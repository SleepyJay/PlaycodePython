
import unittest
from battleboat.GameBoard import GameBoard


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
        size = 10
        gb = GameBoard(size)

        player_expected = ''.join( ['U0' for i in range(0,100)] )
        self.assertEquals(player_expected, gb.to_player_repr(),
            'Created open player grid')

        opponent_expected = ''.join( ['U_' for i in range(0,100)] )
        self.assertEquals(opponent_expected, gb.to_opponent_repr(),
            'Created open opponent grid')

        # TODO: make this a better test than just "do not error"
        positions = gb.load_board(size, player_expected)
        print(positions)


if __name__ == '__main__':
	unittest.main(verbosity=2)



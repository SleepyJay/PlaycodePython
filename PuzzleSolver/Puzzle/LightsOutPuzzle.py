# LightsOut Puzzle

import math
from PuzzleSolver.Solver import Solver

DEF_START = ('0' * 25)
DEF_GOAL = ('1' * 25)


class LightsOutPuzzle(Solver):

    def __init__(self, starting_point=DEF_START , goal=DEF_GOAL ):
        super(LightsOutPuzzle, self).__init__(starting_point, goal)

    def create_board(self):
        size = len(self.starting_point)
        dims = math.sqrt(size)
        if not float.is_integer(dims):
            raise ValueError('Board is not a square')

        # first row
        for i in range(r):
            self.board.append({'value': self.starting_point[i], 'affects': affected[0]})

        for i in range(size):
            affected = [i, i+r, i-r, i+1, i-1]
            self.board.append({'value': self.starting_point[i], 'affects': affected})

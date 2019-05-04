# Diamond Puzzle

from PuzzleSolver.Solver import Solver

# Constants for named-board positions, "YT" is "yellow-top", etc.
(YT, BL, BR, YB, RL, RR, PT, GL, GR, PB) = range(10)

DEF_START = '1010010101'
DEF_GOAL = '1100100011'


class DiamondPuzzle(Solver):

    def __init__(self, starting_point=DEF_START, goal=DEF_GOAL ):
        self.board = None
        super(DiamondPuzzle, self).__init__(starting_point, goal)

    def create_board(self):
        self.board = [
            {'value': 0, 'affects': (YT, YB, PB)}, # YT 0 : 0, 3, 9
            {'value': 0, 'affects': (BL, BR, YB)}, # BL 1 : 1, 2, 3
            {'value': 0, 'affects': (BR, YT, YB)}, # BR 2 : 2, 0, 3
            {'value': 0, 'affects': (YB, BR, RR)}, # YB 3 : 3, 2, 5
            {'value': 0, 'affects': (RL, YB, PT)}, # RL 4 : 4, 3, 6
            {'value': 0, 'affects': (RR, BR, GR)}, # RR 5 : 5, 2, 8
            {'value': 0, 'affects': (PT, GR, GL)}, # PT 6 : 6, 8, 7
            {'value': 0, 'affects': (GL, RR)    }, # GL 7 : 7, 5
            {'value': 0, 'affects': (GR, RL)    }, # GR 8 : 8, 4
            {'value': 0, 'affects': (PB, PT, YT)}  # PB 9 : 9, 6, 0
        ]



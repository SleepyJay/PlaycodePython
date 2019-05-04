# Diamond Puzzle Solver: tests.py

# Unit tests

from Puzzles.DiamondPuzzle import DiamondPuzzle
import unittest

dp = DiamondPuzzle(starting_point = '1010010101', goal = '1100100011')

class Test_DiamondPuzzle(unittest.TestCase):

    def test_reset(self):
        dp.reset()
        board_str = dp.get_board_state()
        self.assertEqual(board_str, dp.starting_point, "Reset OK")


    def test_moving(self):
        expected_changes = [
            [0, 3, 9],
            [1, 2, 3],
            [0, 2, 3],
            [2, 3, 5],
            [3, 4, 6],
            [2, 5, 8],
            [6, 7, 8],
            [5, 7],
            [4, 8],
            [0, 6, 9]
        ]

        for i in range(len(expected_changes)):
            mv = i
            orig = dp.get_board_state()
            dp.move(mv)
            curr = dp.get_board_state()

            expected = expected_changes[i]
            ok = 1
            changed = []
            for j in range(10):
                if(orig[j] != curr[j]):
                    changed.append(j)
                    if(j in expected):
                        ok = 1
                    else:
                        ok = 0
                        break
            self.assertTrue(ok, "{}. move [{}] = ({}) ==> ({}) -> {}".format(i, mv, orig, curr, changed))

    def test_solve(self):
        expected = [0, 1, 3, 4, 5, 7, 9]
        self.isBoardSolved(expected)
        self.isBoardSolved(reversed(expected))

        dp.solveAttempts = 0
        best = sorted(dp.solve_shortest(1))
        self.isBoardSolved(best)
        print("Best ({}): {}".format(dp.solveAttempts, best))


        # TEST: pruning
        starting = [7, 1, 7, 3, 0, 0, 0, 6, 4, 5, 5, 0, 2, 8, 6, 3, 7, 9, 9, 3, 4,
                    0, 0, 5, 1, 5, 5, 7, 1, 3, 0, 1, 4, 3, 8, 2, 2, 0, 8, 0, 0, 1,
                    7, 6, 8, 9, 9, 7, 3, 9, 6, 2, 8, 7, 4, 6, 3, 8, 0, 9, 7, 3, 9,
                    7, 6, 5, 3, 2, 2, 9, 5, 2, 6, 6, 9, 1, 3, 1, 6, 0, 1, 4, 5, 3,
                    8, 3, 4, 4, 9, 9, 6, 3, 9, 8, 8, 2, 9, 0, 6, 4, 7, 2, 8, 4, 1,
                    3, 3, 7, 7, 7, 6, 7, 5, 9, 2, 1, 9, 7, 4, 1, 4]

        actual = dp.prune(starting)

        self.assertEqual(expected, sorted(actual), "Prunning ({}) == ({}) OK".format(expected, actual))

    #
    def isBoardSolved(self, solution):
        ok = dp.confirm_solution(solution)
        ok_str = ("PASS" if ok else "FAIL")
        curr = dp.get_board_state()
        print("Solved: {} == {} : {}".format(curr, dp.goal, ok_str))


if __name__ == '__main__':
    unittest.main(verbosity=2)

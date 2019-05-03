# Diamond Puzzle Solver: tests.py

# Unit tests

import string
import unittest

from GridMenu.GridMenu import GridMenu

alphabet = list(string.ascii_lowercase)
grid = GridMenu(6, alphabet)

class Test_GridMenu(unittest.TestCase):
	def test_moving(self):
		tests = [
			{'moves': ['E'],      'expected': 'a'},
			{'moves': ['D', 'E'], 'expected': 'g'},
			{'moves': ['U', 'E'], 'expected': 'y'},
			{'moves': ['R', 'E'], 'expected': 'b'},
			{'moves': ['L', 'E'], 'expected': 'f'},
			{'moves': ['R', 'L', 'E'], 'expected': 'a'},
			{'moves': ['U', 'R', 'R', 'E'], 'expected': 'y'}
		]
		
		for test in tests:
			actual = grid.move_many(test['moves'])
			message = "Testing Moves: {} => {} ? {}".format(test['moves'], test['expected'], actual)
			self.assertEqual(actual, test['expected'], message)
			print(message)
			
			grid.clear()
			



# a b c d e f
# g h i j k l
# m n o p q r
# s t u v w x
# y z


if __name__ == '__main__':
	unittest.main(verbosity=2)

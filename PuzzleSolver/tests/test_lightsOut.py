# LightOut Puzzle Solver

# Unit tests

from Puzzles.LightsOutPuzzle import LightsOutPuzzle
import unittest

dp = LightsOutPuzzle(starting_point = '1010010101', goal = '1100100011')

__package__ = "tests.test_lightsOut"

class Test_LightsOutPuzzle(unittest.TestCase):
	
	def test_regions(self):
		region = ''
		size = 25
		dims = 5
		for row in range(dims):
			for col in range(dims):
				if row == 0:
					if col == 0:
						region = 'cellTopLeft'
					elif col == dims - 1:
						region = 'cellTopRight'
					else:
						region = 'cellTopMid'
						
				elif row == dims-1:
					if col == 0:
						region = 'cellBottomLeft'
					elif col == dims - 1:
						region = 'cellBottomRight'
					else:
						region = 'cellBottomMid'
						
				else:
					if col == 0:
						region = 'cellMidLeft'
					elif col == dims - 1:
						region = 'cellMidRight'
					else:
						region = 'cellMidMid'
				
		


if __name__ == '__main__':
	unittest.main(verbosity=2)

# Unit tests

import unittest
from datetime import datetime
from Engine import Engine
from time import gmtime, strftime

class Test_Engine(unittest.TestCase):
	
	def test_BuildWalls(self):
		print('')
		tests = [
			{'name': 'Build 7.5 x 0', 'width': 7.5, 'height': 0,  'expected': 0},
			{'name': 'Build 7.5 x 1', 'width': 7.5, 'height': 1,  'expected': 2},
			{'name': 'Build 7.5 x 2', 'width': 7.5, 'height': 2,  'expected': 2},
			{'name': 'Build  12 x 3', 'width': 12,  'height': 3,  'expected': 4},
			{'name': 'Build  27 x 5', 'width': 27,  'height': 5,  'expected': 7958},
			{'name': 'Build  48 x 2', 'width': 48,  'height': 2,  'expected': 37120},
			{'name': 'Build  48 x 4', 'width': 48,  'height': 4,  'expected': 10178548},
			{'name': 'Build  48 x 6', 'width': 48,  'height': 6,  'expected': 3919649942},
			{'name': 'Build  48 x 8', 'width': 48,  'height': 8,  'expected': 1722438038790},
			{'name': 'Build  48 x 10','width': 48,  'height': 10, 'expected': 806844323190414},
		]

		for test in tests:
			started = datetime.now()
			engine = Engine()
			engine.buildBlocks(3, 4.5)
			engine.buildLayers(test['width'])
			actual = engine.countWalls(test['height'])
			print("Testing: {} ==> {}".format(test['name'], actual))

			self.assertEqual(actual, test['expected'],
				"{}: Got: {}, Expected: {}".format(
					test['name'], actual, test['expected'] ))
			
			ended = datetime.now()
			duration = ended - started
			print("Ran in: ~ {}.{} seconds".format(duration.seconds, duration.microseconds))

if __name__ == '__main__':
	unittest.main(verbosity=2)

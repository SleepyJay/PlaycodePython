# NameDistro

# Unit tests

import unittest

from NameDistro import NameDistro

class Test_NameDistro(unittest.TestCase):

	def test_ItemDistros(self):
		nd = NameDistro()
		funcs = nd.group_functions

		group_count = 3
		#print "\n"
		
		for test in nd.group_data:
			print "\n"
			for func in funcs:
				total = 0
				count = 0

				result = func.func(group_count, test.items)

				print("{} passed to {} results in: {}".format(
					test.name, func.name, result
				))

				# Test: correct number of groups returned?
				actual_group_count = len(result.groups)
				self.assertEqual(actual_group_count, group_count,
					"Correct number of groups ({} == {})".format(actual_group_count, group_count))

				# Test: sum of items in groups is correct?
				for grp in result.groups:
					group_sum = 0
					count += len(grp.items)
					for i in grp.items:
						group_sum += test.items[i]

					self.assertEqual(group_sum, grp.sum,
						"Correct sum of items ({} == {})".format(group_sum,grp.sum))
					total += group_sum

				# Test: total sum ok?
				self.assertEqual(result.total, total,
					"Correct total sum ({} == {})".format(result.total, total))

				# correct total items returned?
				self.assertEqual(len(test.items), count,
					"Correct total items ({} == {})".format(len(test.items), count))

	# 
	def test_Evalutate(self):
		nd = NameDistro()
		result = nd.Result([
			nd.GroupTuple([], 30),
			nd.GroupTuple([], 30),
			nd.GroupTuple([], 40),
		], 100)

		diff = nd.evaluate(result)
		self.assertEqual(diff, 10,
			"Correct evaulated diff ({})".format(diff))
		

if __name__ == '__main__':
	unittest.main(verbosity=2)




# NameDistro Evaluate

import unittest

from NameDistro import NameDistro


nd = NameDistro()
funcs = nd.group_functions
group_count = 3

for data in nd.group_data:
	for func in funcs:
		result = func.func(group_count, data.items)
		spread = nd.evaluate(result)
		print("{} passed to {} has spread of: {}".format(
			data.name, func.name, spread
		))
	print "\n"





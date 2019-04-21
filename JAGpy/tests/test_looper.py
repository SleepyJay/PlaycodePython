#!/usr/bin/python

import unittest
from collections import Counter
import JAGpy.Looper as Looper
from JAGpy.tests.helpers import loop_to_3


class TestLooper(unittest.TestCase):
    #
    def test_combos(self):
        items = Looper.combos(0, 2, 3)
        boring = loop_to_3()

        self.assertEqual(Counter(map(str, items)), Counter(map(str, boring)))

    #
    def test_value_to_list(self):
        self.assertEqual(Looper.value_to_list(2, 3), [1, 1] )
        self.assertEqual(Looper.value_to_list(2, 3, 3), [0, 1, 1])
        self.assertEqual(Looper.value_to_list(2, 5), [1, 0, 1])
        self.assertEqual(Looper.value_to_list(2, 34), [1, 0, 0, 0, 1, 0])
        self.assertEqual(Looper.value_to_list(5, 34), [1, 1, 4])

        items = []
        for x in range(0, 8):
            items.append(Looper.value_to_list(2, x, 3))

        boring = loop_to_3()
        self.assertEqual(Counter(map(str, items)), Counter(map(str, boring)))

    #
    def test_list_to_value(self):
        self.assertEqual(Looper.list_to_value(2, [1, 1]), 3 )
        self.assertEqual(Looper.list_to_value(2, [0, 1, 1]), 3)
        self.assertEqual(Looper.list_to_value(2, [1, 0, 1]), 5)
        self.assertEqual(Looper.list_to_value(2, [1, 0, 0, 0, 1, 0]), 34)

        items = []
        for x in loop_to_3():
            items.append(Looper.list_to_value(2, x))

        boring = range(0, 8)
        self.assertEqual(Counter(map(str, items)), Counter(map(str, boring)))

    #
    def test_combo_step(self):
        my_step = [[0], [1]]
        for i in (0, 1):
            my_step = Looper.combo_step(0, 2, my_step)

        boring = loop_to_3()
        self.assertEqual(Counter(map(str, my_step)), Counter(map(str, boring)))


if __name__ == '__main__':
    unittest.main(verbosity=2)

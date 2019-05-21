
import unittest
from collections import namedtuple
from BlockStacking.LayerSearchTree import LayerSearchTree

StackTest = namedtuple('stack_test', "data, exp_data")
LayerMock = namedtuple('layer_mock', "width, width_set, mock_expected")


class TestLayerSearchTree(unittest.TestCase):

    def test_add(self):
        my_stree = LayerSearchTree()

        keys_1 = [3,4,5,6]
        expect = {3: {4: {5: {6: keys_1}}}}
        my_stree.add(keys_1, keys_1)
        self.assertDictEqual(my_stree.tree, expect, 'Correctly keyed')

        keys_2 = [3,4,5,7]
        expect = {3: {4: {5: {6: keys_1, 7: keys_1}}}}
        my_stree.add(keys_2, keys_1)
        self.assertDictEqual(my_stree.tree, expect, 'Correctly keyed')

        keys_3 = [3,4,5,7]
        expect = {3: {4: {5: {6: keys_1, 7: keys_3}}}}
        my_stree.add(keys_3, keys_3)
        self.assertDictEqual(my_stree.tree, expect, 'Correctly keyed')

    def test_stackable(self):
        my_stree = LayerSearchTree()

        tests = [
            StackTest([3, 6, 9, 12], None),
            StackTest([4.5, 9, 12], {3, 7.5, 12}),
            StackTest([3, 7.5, 12], {4.5, 9, 12}),
        ]

        width = 12

        layers = []
        # Prepare layers and SearchTree...
        for test in tests:
            width_set = set(test.data)

            layer = LayerMock(width, width_set, test.exp_data)
            my_stree.add(test.data, layer)
            layers.append(layer)

        # Now test stackable
        for layer in layers:
            found = my_stree.find_stackable(layer)

            if found:
                print(f"found: {found[0].width_set}, expect: {layer.mock_expected}")
                self.assertSetEqual(found[0].width_set, layer.mock_expected, 'found')
            else:
                print(f"found: None, expect: None")
                self.assertListEqual(found, [], 'empty')




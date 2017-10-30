from RandRanger import RandRanger
import unittest
from functools import partial

##
rr = RandRanger(500)

class Test_RandRanger(unittest.TestCase):

    #
    def test_rand5(self):
        # TODO: Make this better!
        res = rr.rand_n(5)
        self.assertLess(res, 6, "value is less than 6")
        self.assertGreaterEqual(res, 1, "value is greater than 1")

    #
    def test_does_picks(self):
        self.assertEqual(rr.does_rand_even(4, 8), rr.randX_from_randY_even, "4,8 uses even")
        self.assertEqual(rr.does_rand_reject(5, 7), rr.randX_from_randY_reject, "5,7 uses reject")

    #
    def test_rand_even(self):
        fn = rr.does_rand_even(4, 8)
        val = fn(4,8, partial(rr.rand_always_n, 2))
        self.assertEqual(val, 1, "rand4_from_rand8 when value 2")
        
    #
    def test_rand_always_n(self):
        always_value = 5
        for run in range(1,5):
            n = rr.rand_always_n(always_value, run)
            self.assertEqual(n, always_value, "Always same value")

        for run in range(1,5):
            n = (partial(rr.rand_always_n, always_value))(run)
            self.assertEqual(n, always_value, "Always same value")



if __name__ == '__main__':
	unittest.main(verbosity=2)



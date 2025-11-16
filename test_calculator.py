# https://github.com/patsofatso/lab11-BT-JY
# Partner 1: Brandon Tran
# Partner 2: Jacob Young

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 2), 4)
    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_sub(self):
        self.assertEqual(sub(2, 1), 1)
        self.assertEqual(sub(2, 2), 0)
        self.assertEqual(sub(3, 1), 2)

    ######## Partner 1
    def test_multiply(self):
        self.assertTrue(mul(2, 4) == 8)
        self.assertTrue(mul(0, 5) == 0)
        self.assertTrue(mul(1, 1) == 1)

    def test_divide(self):
        self.assertTrue(div(2, 10) == 5)
        self.assertTrue(div(5, 5) == 1)
        self.assertTrue(div(10, 5) == 0.5)

    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 0, 5)
    # def test_logarithm(self): # 3 assertions
    #     fill in code
    def test_logarithm(self):
        self.assertEqual(logarithm(2, 2), 1)
        self.assertEqual(logarithm(10, 1), 0)
        self.assertEqual(logarithm(5, 1), 0)
    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    def test_log_invalid_base(self):
        self.assertRaises(ValueError, logarithm, -1, 2)
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(-1, -1), 1.41421356237)
        self.assertTrue(hypotenuse(0, 0) == 0.0)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.41421356237)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(2), 1.41421356237)
        self.assertTrue(square_root(4) == 2)

# Do not touch this
if __name__ == "__main__":
    unittest.main()

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
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -10), -15)
        self.assertEqual(add(2, 2), 4)
    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_sub(self):
        self.assertEqual(sub(2, 1), 1)
        self.assertEqual(subtract(-2, -2), 0)
        self.assertEqual(sub(-5, 1), -6)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2, 4), 8)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(mul(1, -1), -1)

    def test_divide(self):
        self.assertEqual(div(-2, 10), -5)
        self.assertEqual(div(5, 0), 0)
        self.assertEqual(div(10, 5), 0.5)

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
        self.assertEqual(log(10, 1), 0)
        self.assertEqual(logarithm(5, 1), 0)
    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    def test_log_invalid_base(self):
        self.assertRaises(ValueError, log, -1, 2)
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(-1, -1), 1.41421356237)
        self.assertEqual(hypotenuse(0, 0), 0.0)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.41421356237)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertAlmostEqual(square_root(2), 1.41421356237)
        self.assertEqual(square_root(4), 2)

# Do not touch this
if __name__ == "__main__":
    unittest.main()

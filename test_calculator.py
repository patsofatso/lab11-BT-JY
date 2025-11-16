# https://github.com/patsofatso/lab11-BT-JY
# Partner 1: Brandon Tran
# Partner 2: Jacob Young

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertTrue(multiply(2, 4) == 8)
        self.assertTrue(multiply(0, 5) == 0)
        self.assertTrue(multiply(1, 1) == 1)

    def test_divide(self):
        self.assertTrue(divide(2, 10) == 5)
        self.assertTrue(divide(5, 5) == 1)
        self.assertTrue(divide(10, 5) == 0.5)

    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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

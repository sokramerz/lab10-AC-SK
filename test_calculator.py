#https://github.com/sokramerz/lab10-AC-SK
#Adrian de la Cruz
#Stephen Kramer

import unittest
from calculator import *
class TestCalculator(unittest.TestCase):
    
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 1), 3)
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(2, 0), 2)
    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-4, 0), -4)
    # ##########################
    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 5), 15)
        self.assertEqual(mul(-4, 2), -8)
        self.assertEqual(mul(0, 99), 0)
    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5.0)
        self.assertEqual(div(4, 20), 5.0)
        with self.assertRaises(ZeroDivisionError):
            div(0, 1)
    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 1)
    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(logarithm(4, 16), 2.0)
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)
    def test_sqrt(self):  # 3 assertions
        self.assertAlmostEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-9)
    ##########################
# Do not touch this

if __name__ == "__main__":
    unittest.main()


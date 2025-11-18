#https://github.com/camiladleong/lab-11-CD-MA.git
import unittest

#Partner 1: Camila D' Leon
#Partner 2: Muhammad Athar

from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 100), 100)
        

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(-2, -5), 3)
        self.assertEqual(subtract(0, 7), -7)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-9, 3), -3)
        self.assertAlmostEqual(div(5, 2), 2.5)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)
            
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(5, 1), 0)
    

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(0, 7), 7.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()

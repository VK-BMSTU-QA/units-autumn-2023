import unittest
import math
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_mult(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_subtr(self):
        self.assertEqual(self.calculator.subtraction(4, 2), 2)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_div(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertEqual(self.calculator.division(0, 0), None)

    def test_ads(self):
        self.assertEqual(self.calculator.adsolute(-4), 4)
        self.assertEqual(self.calculator.adsolute(0), 0)
    
    def test_deg(self):
        self.assertEqual(self.calculator.degree(2, 1), 2)
        self.assertEqual(self.calculator.degree(0, 0), 1)
        self.assertEqual(self.calculator.degree(1, 0), 1)
    
    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertEqual(self.calculator.ln(1), 0)
    
    def test_log(self):
        self.assertEqual(self.calculator.log(2, 2), 1)
        self.assertEqual(self.calculator.log(8, 2), 3)
    
    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(6, 1), 6)
        self.assertEqual(self.calculator.nth_root(4, 2), 2)

if __name__ == "__main__":
    unittest.main()

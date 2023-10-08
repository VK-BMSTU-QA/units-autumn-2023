import unittest
from src.calculator import Calculator
import math

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)

    def test_division_correct(self):
        self.assertEqual(self.calculator.division(6, 2), 3)

    def test_zero_division(self):
        self.assertEqual(self.calculator.division(3, 0), None)

    def test_absolute_positive(self):
        self.assertEqual(self.calculator.adsolute(13), 13)
    
    def test_absolute_negative(self):
        self.assertEqual(self.calculator.adsolute(-13), 13)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
    
    def test_ln_positive(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
    
    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_log_correct_base(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
    
    def test_log_incorrect_base(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 2, 1)

    def test_log_negative_arg(self):
        self.assertRaises(ValueError, self.calculator.log, -3, 2)

    def test_sqrt_positive(self):
        self.assertEqual(self.calculator.sqrt(9), 3)

    def test_sqrt_negative(self):
        self.assertEqual(self.calculator.sqrt(-4).imag, 2)

    def test_nth_root_valid_base(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)

    def test_nth_root_zero_base(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 8, 0)

if __name__ == "__main__":
    unittest.main()

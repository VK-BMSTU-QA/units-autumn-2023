import unittest
from src.calculator import Calculator
import math

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertAlmostEqual(self.calculator.addition(1.5, 2), 3.5)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(1, -1), 0)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertAlmostEqual(self.calculator.addition(-1.5, -0.8), -2.3)

    def test_zero_add(self):
        self.assertEqual(self.calculator.addition(0, 1), 1)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertAlmostEqual(self.calculator.addition(0.5, 0), 0.5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertAlmostEqual(self.calculator.multiplication(2.5, 3), 7.5)

    def test_multiply_negative(self):
        self.assertEqual(self.calculator.multiplication(-2, 2), -4)
        self.assertEqual(self.calculator.multiplication(2, -2), -4)
        self.assertEqual(self.calculator.multiplication(-2, -2), 4)
        self.assertAlmostEqual(self.calculator.multiplication(-2.5, 3), -7.5)

    def test_zero_multiply(self):
        self.assertEqual(self.calculator.multiplication(2, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 2), 0)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)
        self.assertAlmostEqual(self.calculator.subtraction(2.5, 0.1), 2.4)

    def test_sub_zero(self):
        self.assertEqual(self.calculator.subtraction(1, 0), 1)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertAlmostEqual(self.calculator.subtraction(0.5, 0), 0.5)

    def test_sub_negative(self):
        self.assertEqual(self.calculator.subtraction(1, -2), 3)
        self.assertEqual(self.calculator.subtraction(-1, -1), 0)
        self.assertAlmostEqual(self.calculator.subtraction(1, -0.5), 1.5)

    def test_division_positive(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertEqual(self.calculator.division(0, 1), 0)
        self.assertAlmostEqual(self.calculator.division(0.5, 2), 0.25)

    def test_division_negative(self):
        self.assertEqual(self.calculator.division(-6, 2), -3)
        self.assertEqual(self.calculator.division(0, -1), 0)
        self.assertEqual(self.calculator.division(6, -2), -3)
        self.assertEqual(self.calculator.division(-6, -2), 3)
        self.assertAlmostEqual(self.calculator.division(-1.5, 2), -0.75)

    def test_zero_division(self):
        self.assertEqual(self.calculator.division(3, 0), None)
        self.assertEqual(self.calculator.division(-1, 0), None)
        self.assertEqual(self.calculator.division(0, 0), None)
        self.assertEqual(self.calculator.division(0.5, 0), None)

    def test_absolute_positive(self):
        self.assertEqual(self.calculator.adsolute(13), 13)
        self.assertAlmostEqual(self.calculator.adsolute(0.5), 0.5)
    
    def test_absolute_zero(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.adsolute(-13), 13)
        self.assertAlmostEqual(self.calculator.adsolute(-1.5), 1.5)

    def test_degree_positive_arg(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertAlmostEqual(self.calculator.degree(2, -1), 0.5)
        self.assertEqual(self.calculator.degree(2, 0), 1)
        self.assertAlmostEqual(self.calculator.degree(4, 0.5), 2)
        self.assertAlmostEqual(self.calculator.degree(4, 1.5), 8)
        self.assertAlmostEqual(self.calculator.degree(1.5, 2), 2.25)
    
    def test_degree_zero_arg(self):
        self.assertEqual(self.calculator.degree(0, 1), 0)
        self.assertEqual(self.calculator.degree(0, 0), 1)
        self.assertRaises(ZeroDivisionError, self.calculator.degree, 0, -1)
        self.assertAlmostEqual(self.calculator.degree(0, 1.5), 0)

    def test_degree_negative_arg(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertEqual(self.calculator.degree(-1, 0), 1)
        self.assertAlmostEqual(self.calculator.degree(-4, 0.5), 2j)
        self.assertAlmostEqual(self.calculator.degree(-1.5, 2), 2.25)

    def test_ln_positive(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_log_correct_base(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertAlmostEqual(self.calculator.log(2.25, 1.5), 2)
    
    def test_log_incorrect_base(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 2, 1)
        self.assertRaises(ValueError, self.calculator.log, 2, 0)
        self.assertRaises(ValueError, self.calculator.log, 2, -1)

    def test_log_negative_arg(self):
        self.assertRaises(ValueError, self.calculator.log, -3, 2)

    def test_sqrt_positive(self):
        self.assertEqual(self.calculator.sqrt(9), 3)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-4), 2j)

    def test_nth_root_valid_base(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        self.assertAlmostEqual(self.calculator.nth_root(8, 1.5), 4)

    def test_nth_root_zero_base(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 8, 0)

if __name__ == "__main__":
    unittest.main()

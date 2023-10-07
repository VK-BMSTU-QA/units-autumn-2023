import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertAlmostEqual(self.calculator.addition(1.2, 2), 3.2)

    def test_add_zero(self):
        self.assertAlmostEqual(self.calculator.addition(2.3, 0), 2.3)

    def test_add_negative(self):
        self.assertAlmostEqual(self.calculator.addition(3, -2.1), 0.9)

    def test_sub(self):
        self.assertAlmostEqual(self.calculator.subtraction(5.1, 1), 4.1)

    def test_sub_zero(self):
        self.assertAlmostEqual(self.calculator.subtraction(3, 0), 3)

    def test_sub_negative(self):
        self.assertAlmostEqual(self.calculator.subtraction(5, -3.5), 8.5)

    def test_mult(self):
        self.assertAlmostEqual(self.calculator.multiplication(5.1, 2), 10.2)

    def test_mult_zero(self):
        self.assertAlmostEqual(self.calculator.multiplication(3, 0), 0)

    def test_mult_negative(self):
        self.assertAlmostEqual(self.calculator.multiplication(5, -3.2), -16)

    def test_mult_one(self):
        self.assertAlmostEqual(self.calculator.multiplication(6.5, 1), 6.5)

    def test_div(self):
        self.assertAlmostEqual(self.calculator.division(6, 4), 1.5)

    def test_div_zero_divident(self):
        self.assertAlmostEqual(self.calculator.division(0, 5.1), 0)

    def test_div_zero_divisor(self):
        self.assertEqual(self.calculator.division(3, 0), None)

    def test_div_zero_by_zero(self):
        self.assertEqual(self.calculator.division(0, 0), None)

    def test_div_negative(self):
        self.assertAlmostEqual(self.calculator.division(5, -2), -2.5)

    def test_div_one(self):
        self.assertAlmostEqual(self.calculator.division(6.5, 1), 6.5)

    def test_abs_positive(self):
        self.assertAlmostEqual(self.calculator.adsolute(3.3), 3.3)

    def test_abs_negative(self):
        self.assertAlmostEqual(self.calculator.adsolute(-5.3), 5.3)

    def test_abs_zero(self):
        self.assertAlmostEqual(self.calculator.adsolute(0), 0)

    def test_degree_positive(self):
        self.assertAlmostEqual(self.calculator.degree(2, 3), 8)

    def test_degree_negative(self):
        self.assertAlmostEqual(self.calculator.degree(2, -3), 0.125)

    def test_degree_zero(self):
        self.assertAlmostEqual(self.calculator.degree(8.5, 0), 1)

    def test_degree_float(self):
        self.assertAlmostEqual(self.calculator.degree(9, 1.5), 27)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.exp(1.5)), 1.5)

    def test_ln_error(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)

    def test_log_one_base(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 12, 1)

    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, 8, -3)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-4), 2j)

    def test_sqrt_zero(self):
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(16, 4), 2)

    def test_nth_root_negative(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, -3), 0.5)

    def test_nth_root_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 8, 0)

    def test_nth_root_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(3, 0.5), 9)


if __name__ == "__main__":
    unittest.main()

import math
import unittest

from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_zero(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertEqual(self.calculator.addition(0, 1), 1)
        self.assertAlmostEqual(self.calculator.addition(0, 0.1), 0.1)

    def test_add_pos(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(15, 17), 32)
        self.assertAlmostEqual(self.calculator.addition(15, 17.35), 32.35)

    def test_add_neg(self):
        self.assertEqual(self.calculator.addition(0, -23), -23)
        self.assertEqual(self.calculator.addition(11, -23), -12)
        self.assertEqual(self.calculator.addition(-11, 23), 12)
        self.assertEqual(self.calculator.addition(-11, -23), -34)
        self.assertAlmostEqual(self.calculator.subtraction(11, -34.1), 45.1)

    def test_sub_zero(self):
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(1, 0), 1)
        self.assertEqual(self.calculator.subtraction(0, 1), -1)
        self.assertAlmostEqual(self.calculator.subtraction(0, -0.1), 0.1)

    def test_sub_pos(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
        self.assertEqual(self.calculator.subtraction(15, 17), -2)
        self.assertAlmostEqual(self.calculator.subtraction(32, 17.7), 14.3)

    def test_sub_neg(self):
        self.assertEqual(self.calculator.subtraction(0, -23), 23)
        self.assertEqual(self.calculator.subtraction(11, -23), 34)
        self.assertEqual(self.calculator.subtraction(-11, 23), -34)
        self.assertEqual(self.calculator.subtraction(-11, -23), 12)
        self.assertAlmostEqual(self.calculator.subtraction(-11, -23.5), 12.5)

    def test_mul_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)
        self.assertEqual(self.calculator.multiplication(1, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 1), 0)
        self.assertAlmostEqual(self.calculator.multiplication(0, 0.74), 0)

    def test_mul_pos(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(15, 17), 255)
        self.assertAlmostEqual(self.calculator.multiplication(32.5, 17), 552.5)

    def test_mul_neg(self):
        self.assertEqual(self.calculator.multiplication(0, -23), 0)
        self.assertEqual(self.calculator.multiplication(11, -23), -253)
        self.assertEqual(self.calculator.multiplication(-11, 23), -253)
        self.assertEqual(self.calculator.multiplication(-11, -23), 253)
        self.assertAlmostEqual(self.calculator.multiplication(-11, -23.8),
                               261.8)

    def test_div_zero(self):
        self.assertEqual(self.calculator.division(0, 1), 0)
        self.assertEqual(self.calculator.division(0, -1), 0)
        self.assertAlmostEqual(self.calculator.division(0, -0.6), 0)

    def test_div_by_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)
        self.assertEqual(self.calculator.division(-1, 0), None)
        self.assertEqual(self.calculator.division(0, 0), None)
        self.assertEqual(self.calculator.division(0.32, 0), None)

    def test_div_pos(self):
        self.assertAlmostEqual(self.calculator.division(1, 2), 0.5)
        self.assertEqual(self.calculator.division(32, 16), 2)
        self.assertEqual(self.calculator.division(32, 4), 8)
        self.assertAlmostEqual(self.calculator.division(32, 2.5), 12.8)

    def test_div_neg(self):
        self.assertEqual(self.calculator.division(0, -23), 0)
        self.assertEqual(self.calculator.division(12, -3), -4)
        self.assertEqual(self.calculator.division(-16, 4), -4)
        self.assertEqual(self.calculator.division(-32, -4), 8)
        self.assertAlmostEqual(self.calculator.division(-32, -2.5), 12.8)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_abs_pos(self):
        self.assertEqual(self.calculator.adsolute(1), 1)
        self.assertEqual(self.calculator.adsolute(123), 123)
        self.assertAlmostEqual(self.calculator.adsolute(32.8), 32.8)

    def test_abs_neg(self):
        self.assertEqual(self.calculator.adsolute(-1), 1)
        self.assertEqual(self.calculator.adsolute(-123), 123)
        self.assertAlmostEqual(self.calculator.adsolute(-32.8), 32.8)

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)
        self.assertEqual(self.calculator.degree(1, 0), 1)
        self.assertEqual(self.calculator.degree(-1, 0), 1)
        self.assertAlmostEqual(self.calculator.degree(-1.78, 0), 1)

    def test_degree_pos(self):
        self.assertEqual(self.calculator.degree(1, 2), 1)
        self.assertEqual(self.calculator.degree(2, 2), 4)
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertAlmostEqual(self.calculator.degree(4, 0.5), 2)
        self.assertAlmostEqual(self.calculator.degree(3, 0.7), 2.157669279974)

    def test_degree_neg_value(self):
        self.assertEqual(self.calculator.degree(-1, 2), 1)
        self.assertEqual(self.calculator.degree(-2, 2), 4)
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_degree_neg_degree(self):
        self.assertAlmostEqual(self.calculator.degree(2, -2), 0.25)
        self.assertAlmostEqual(self.calculator.degree(2, -3), 0.125)
        self.assertAlmostEqual(self.calculator.degree(4, -0.5), 0.5)
        self.assertAlmostEqual(self.calculator.degree(3, -0.7), 0.46346305677)

    def test_ln_zero(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_pos(self):
        self.assertAlmostEqual(self.calculator.ln(2), 0.6931471805599453)
        self.assertAlmostEqual(self.calculator.ln(3), 1.0986122886681098)
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)

    def test_ln_neg(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertRaises(ValueError, self.calculator.ln, -1)
        self.assertRaises(ValueError, self.calculator.ln, -1.5)

    def test_log_zero(self):
        self.assertEqual(self.calculator.log(1, 2), 0)
        self.assertEqual(self.calculator.log(1, 3), 0)
        self.assertAlmostEqual(self.calculator.log(1, 3.5), 0)

    def test_log_pos(self):
        self.assertEqual(self.calculator.log(2, 2), 1)
        self.assertAlmostEqual(self.calculator.log(3, 2), 1.5849625007211563)

    def test_log_neg_value(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 2)
        self.assertRaises(ValueError, self.calculator.log, -1, 2)

    def test_log_neg_base(self):
        self.assertRaises(ValueError, self.calculator.log, 2, 0)
        self.assertRaises(ValueError, self.calculator.log, 2, -1)

    def test_log_base_one(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 2, 1)
        self.assertRaises(ZeroDivisionError, self.calculator.log, 2.45, 1)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_pos(self):
        self.assertEqual(self.calculator.sqrt(1), 1)
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(16), 4)
        self.assertAlmostEqual(self.calculator.sqrt(0.16), 0.4)

    def test_sqrt_neg(self):
        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)
        self.assertAlmostEqual(self.calculator.sqrt(-4), 2j)
        self.assertAlmostEqual(self.calculator.sqrt(-16), 4j)

    def test_nth_root_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 2), 0)
        self.assertEqual(self.calculator.nth_root(0, 3), 0)
        self.assertAlmostEqual(self.calculator.nth_root(0, 3.5), 0)

    def test_nth_root_pos(self):
        self.assertEqual(self.calculator.nth_root(1, 2), 1)
        self.assertEqual(self.calculator.nth_root(4, 2), 2)
        self.assertEqual(self.calculator.nth_root(16, 2), 4)
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        self.assertAlmostEqual(self.calculator.nth_root(8, 0.5), 64)

    def test_nth_root_neg_value(self):
        self.assertAlmostEqual(self.calculator.nth_root(-4, 2), 2j)
        self.assertAlmostEqual(self.calculator.nth_root(-16, 2), 4j)

    def test_nth_root_neg_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(4, -2), 0.5)
        self.assertAlmostEqual(self.calculator.nth_root(16, -2), 0.25)
        self.assertAlmostEqual(self.calculator.nth_root(8, -3), 0.5)
        self.assertAlmostEqual(self.calculator.nth_root(8, -0.5), 0.015625)

    def test_nth_root_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 4, 0)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 16, 0)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 8, 0)


if __name__ == "__main__":
    unittest.main()

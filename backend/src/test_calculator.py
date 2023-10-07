import math
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Add tests
    # int tests
    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_neg(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_opposite(self):
        self.assertEqual(self.calculator.addition(-1, 1), 0)

    def test_add_zero(self):
        self.assertEqual(self.calculator.addition(1, 0), 1)

    # inf test
    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(1, math.inf), math.inf)

    # Mul tests
    # int tests
    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(3, 4), 12)

    def test_mul_neg(self):
        self.assertEqual(self.calculator.multiplication(-3, -4), 12)

    def test_mul_sign(self):
        self.assertEqual(self.calculator.multiplication(3, -4), -12)

    def test_mul_zero(self):
        self.assertEqual(self.calculator.multiplication(3, 0), 0)


    # inf tests
    def test_mul_inf(self):
        self.assertEqual(self.calculator.multiplication(3, math.inf), math.inf)

    # Sub tests
    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(4, 3), 1)

    def test_sub_zero(self):
        self.assertEqual(self.calculator.subtraction(4, 0), 4)

    def test_sub_neg(self):
        self.assertEqual(self.calculator.subtraction(4, -1), 5)

    def test_sub_neg_from_neg(self):
        self.assertEqual(self.calculator.subtraction(-4, -1), -3)

    def test_sub_inf(self):
        self.assertEqual(self.calculator.subtraction(10, math.inf), -math.inf)

    # Div tests
    def test_div(self):
        self.assertEqual(self.calculator.division(12, 4), 3.0)

    def test_div_neg(self):
        self.assertEqual(self.calculator.division(12, -4), -3.0)

    def test_div_one(self):
        self.assertEqual(self.calculator.division(12, 1), 12.0)

    def test_div_zero(self):
        self.assertEqual(self.calculator.division(12, 0), None)

    # Abs tests
    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(1), 1)
    def test_abs_neg(self):
        self.assertEqual(self.calculator.adsolute(-1), 1)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    # Degree tests
    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree(self):
        self.assertAlmostEqual(self.calculator.degree(2, -3), 0.125)

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(2, 0), 1)


    # Ln tests
    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(9), 2.1972245773362196)

    def test_ln_exp(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_neg(self):
        self.assertRaises(ValueError, self.calculator.ln, -9)

    # Log tests
    def test_log(self):
        self.assertEqual(self.calculator.log(8, 2), 3)

    def test_log_base_neg(self):
        self.assertRaises(ValueError, self.calculator.log, 8, -2)

    def test_log_base_one(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 8, 1)

    # Sqrt tests
    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(4), 2.0)

    def test_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    # Nth_root tests
    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)

    def test_nth_root_neg(self):
        self.assertEqual(self.calculator.nth_root(-8, 3), 1.0000000000000002+1.7320508075688772j)

    def test_nth_root_base_one(self):
        self.assertEqual(self.calculator.nth_root(8, 1), 8)

    def test_nth_root_float(self):
        self.assertEqual(self.calculator.nth_root(8, 0.5), 64)

if __name__ == "__main__":
    unittest.main()

import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_mul_negative(self):
        self.assertEqual(self.calculator.multiplication(2, -3), -6)

    def test_mul_double_negative(self):
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)

    def test_mul_float(self):
        self.assertEqual(self.calculator.multiplication(2, 3.5), 7.0)

    def test_mul_zero(self):
        self.assertEqual(self.calculator.multiplication(12, 0), 0)

    def test_mul_inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 12), math.inf)

    def test_mul_zero_inf(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(math.inf, 0)))

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(3, 3), 0)

    def test_div(self):
        self.assertAlmostEqual(self.calculator.division(6, 2), 3.0)

    def test_div_negative(self):
        self.assertAlmostEqual(self.calculator.division(6, -2), -3.0)
   
    def test_div_float(self):
        self.assertAlmostEqual(self.calculator.division(7, 2), 3.5)

    def test_div_float_negative(self):
        self.assertAlmostEqual(self.calculator.division(7, -2), -3.5)

    def test_div_by_zero(self):
        self.assertEqual(self.calculator.division(4, 0), None)

    def test_abs_positive(self):
        self.assertEqual(self.calculator.adsolute(5), 5)

    def test_abs_negative(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)
    
    def test_abs_zero(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_degree_positive(self):
        self.assertAlmostEqual(self.calculator.degree(2, 4), 16.0)

    def test_degree_negative(self):
        self.assertAlmostEqual(self.calculator.degree(2, -3), 0.125)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(5), 1.60943791243)

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(16, 2), 4.0)

    def test_log_base_1(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 5, 1)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(16), 4.0)

    def test_sqrt_imaginary(self):
        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)

    def test_nth_root_negative(self):
        self.assertAlmostEqual(self.calculator.nth_root(-8, 3), 1 + 1.732050807568877293527j)    

    def test_nth_root_imaginary(self):
        self.assertAlmostEqual(self.calculator.nth_root(-16, 4), complex(2 ** 0.5, 2 ** 0.5))   


if __name__ == "__main__":
    unittest.main()

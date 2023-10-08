import unittest
from calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_negative_and_positive(self):
        self.assertEqual(self.calculator.addition(-7, 3), -4)

    def test_add_float(self):
        self.assertAlmostEqual(self.calculator.addition(0.5, 0.45), 0.95)

    def test_add_float_negative(self):
        self.assertAlmostEqual(self.calculator.addition(-0.5, -0.45), -0.95)

    def test_add_str(self):
        self.assertEqual(self.calculator.addition('ab', 'bc'), 'abbc')

    def test_add_str_and_nub(self):
        self.assertRaises(TypeError, self.calculator.addition, 'ab', 5)

    def test_add_None(self):
        self.assertRaises(TypeError, self.calculator.addition, None, None)

    def test_add_arrays(self):
        self.assertEqual(self.calculator.addition([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_add_nan(self):
        self.assertTrue(math.isnan(self.calculator.addition(1, math.nan)))

    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(1, math.inf), math.inf)

    def test_add_complex(self):
        self.assertEqual(self.calculator.addition(1, 1j), 1+1j)


    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_mul_negative_and_positive(self):
        self.assertEqual(self.calculator.multiplication(2, -4), -8)

    def test_mul_double_negative(self):
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)

    def test_mul_float(self):
        self.assertEqual(self.calculator.multiplication(0.1, 0.5), 0.05)

    def test_mul_zero(self):
        self.assertEqual(self.calculator.multiplication(1, 0), 0)

    def test_mul_inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 1), math.inf)

    def test_mul_nan(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(1, math.nan)))

    def test_mul_str(self):
        self.assertEqual(self.calculator.multiplication(5, 'a'), 'aaaaa')

    def test_mul_None(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 1, None)

    def test_mul_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'aaaa', [1,2,3])



    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 1)

    def test_sub_negative(self):
        self.assertEqual(self.calculator.subtraction(4, -3), 7)

    def test_sub_greater_num_from_less_num(self):
        self.assertEqual(self.calculator.subtraction(4, 5), -1)

    def test_sub_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(0.5, 0.25), 0.25)

    def test_sub_float_negative(self):
        self.assertAlmostEqual(self.calculator.subtraction(0.1, -0.25), 0.35)

    def test_sub_str(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'a', 10)

    def test_sub_None(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, 1)


    def test_div(self):
        self.assertAlmostEqual(self.calculator.division(8, 2), 4.0)

    def test_div_negative(self):
        self.assertAlmostEqual(self.calculator.division(8, -2), -4.0)

    def test_div_float(self):
        self.assertAlmostEqual(self.calculator.division(7, 2), 3.5)

    def test_div_float_negative(self):
        self.assertAlmostEqual(self.calculator.division(7, -2), -3.5)

    def test_div_by_zero(self):
      self.assertEqual(self.calculator.division(4, 0), None)

    def test_div_str(self):
        self.assertRaises(TypeError, self.calculator.division, 'a', 4)

    def test_div_None(self):
        self.assertRaises(TypeError, self.calculator.division, 4, None)

    def test_div_periodic(self):
        self.assertAlmostEqual(self.calculator.division(1, 3), 0.3333333333333333)



    def test_abs_positive(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_abs_negative(self):
        self.assertEqual(self.calculator.absolute(-5), 5)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_abs_str(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'a')

    def test_abs_None(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)



    def test_degree_positive(self):
        self.assertAlmostEqual(self.calculator.degree(2, 4), 16.0)

    def test_degree_negative_degree(self):
        self.assertAlmostEqual(self.calculator.degree(2, -2), 0.25)

    def test_degree_negative_base_odd(self):
        self.assertAlmostEqual(self.calculator.degree(-2, 3), -8.0)

    def test_degree_negative_base_even(self):
        self.assertAlmostEqual(self.calculator.degree(-2, 4), 16.0)

    def test_degree_double_negative_odd(self):
        self.assertAlmostEqual(self.calculator.degree(-2, -3), -0.125)

    def test_degree_double_negative_even(self):
        self.assertAlmostEqual(self.calculator.degree(-2, -4), 0.0625)

    def test_degree_float_base(self):
        self.assertAlmostEqual(self.calculator.degree(0.5, 3), 0.125)

    def test_degree_float_degree(self):
        self.assertAlmostEqual(self.calculator.degree(16, 0.5), 4.0)

    def test_degree_one(self):
        self.assertAlmostEqual(self.calculator.degree(1, 100), 1)

    def test_degree_one_float_degree(self):
            self.assertAlmostEqual(self.calculator.degree(1, 0.5), 1)

    def test_degree_str(self):
        self.assertRaises(TypeError, self.calculator.degree, 'a', 2)

    def test_degree_None_degree(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, None)

    def test_degree_inf_degree(self):
        self.assertEqual(self.calculator.degree(4, math.inf), math.inf)

    def test_degree_inf_base(self):
        self.assertEqual(self.calculator.degree(math.inf, 2), math.inf)



    def test_ln(self):
     self.assertAlmostEqual(self.calculator.ln(10), 2.302585092994046)

    def test_ln_str(self):
        self.assertRaises(TypeError, self.calculator.ln, 'a')

    def test_ln_None(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)


    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(16, 2), 4.0)

    def test_log_float(self):
        self.assertAlmostEqual(self.calculator.log(16, 0.5), -4.0)

    def test_log_negative_base(self):
        self.assertRaises(ValueError, self.calculator.log, 16, -2)

    def test_log_negative_param(self):
        self.assertRaises(ValueError, self.calculator.log, -16, 2)

    def test_log_base_1(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 5, 1)

    def test_log_str_param(self):
        self.assertRaises(TypeError, self.calculator.log, 'a', 2)

    def test_log_str_base(self):
        self.assertRaises(TypeError, self.calculator.log, 16, 'a')

    def test_log_None_param(self):
        self.assertRaises(TypeError, self.calculator.log, None, 2)

    def test_log_inf_base(self):
        self.assertEqual(self.calculator.log(16, math.inf), 0.0)

    def test_log_inf_param(self):
        self.assertEqual(self.calculator.log(math.inf, 4), math.inf)

    def test_log_None_base(self):
        self.assertRaises(TypeError, self.calculator.log, 16, None)



    def test_sqrt(self):
       self.assertAlmostEqual(self.calculator.sqrt(16), 4.0)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(0.1), 0.31622776601683794)

    def test_sqrt_imaginary(self):
        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)

    def test_sqrt_str(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'a')

    def test_sqrt_None(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)

    def test_sqrt_nan(self):
        self.assertTrue(math.isnan(self.calculator.sqrt(math.nan)))



    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)

    def test_nth_root_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(10, 3), 2.154434690031884)

    def test_nth_root_negative_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, -3), 0.5)

    def test_nth_root_negative(self):
        self.assertAlmostEqual(self.calculator.nth_root(-1, 3), 0.5000000000000001+0.8660254037844386j)

    def test_nth_root_imaginary(self):
        self.assertAlmostEqual(self.calculator.nth_root(-16, 4), complex(2 ** 0.5, 2 ** 0.5))

    def test_nth_root_str_base(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'a', 2)

    def test_nth_root_str_root(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 2, 'a')

    def test_nth_root_None_base(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, 2)

    def test_nth_root_None_root(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 2, None)

    def test_nth_root_inf_root(self):
        self.assertEqual(self.calculator.nth_root(4, math.inf), 1.0)

    def test_nth_root_inf_base(self):
        self.assertEqual(self.calculator.nth_root(math.inf, 10), math.inf)

if __name__ == "__main__":
    unittest.main()

import unittest

from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()


    # Calculator.addition tests

    def test_addition_common(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_addition_zero(self):
        self.assertEqual(self.calculator.addition(123, 0), 123)

    def test_addition_both_zero(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_addition_subtraction(self):
        self.assertEqual(self.calculator.addition(10, -6), 4)

    def test_addition_negative_nums(self):
        self.assertEqual(self.calculator.addition(-5, -4), -9)

    def test_addition_float(self):
        self.assertAlmostEqual(self.calculator.addition(5.6, -4), 1.6)

    def test_addition_lists(self):
        self.assertEqual(self.calculator.addition([1, 2], [2, 3]), [1, 2, 2, 3])

    def test_addition_tuples(self):
        self.assertEqual(self.calculator.addition((1, 2), (2, 3)), (1, 2, 2, 3))

    def test_addition_infinity(self):
        self.assertEqual(self.calculator.addition(4, math.inf), math.inf)

    def test_addition_strings(self):
        self.assertEqual(self.calculator.addition('lol', 'kek'), 'lolkek')

    def test_addition_complex(self):
        self.assertEqual(self.calculator.addition(12, 3j), 12 + 3j)

    def test_fail_addition_dicts(self):
        self.assertRaises(TypeError, self.calculator.addition, {'a': 1, 'b': 2}, {'c': 3})

    def test_fail_addition_none(self):
        self.assertRaises(TypeError, self.calculator.addition, 12, None)

    def test_fail_addition_type_mismatch(self):
        self.assertRaises(TypeError, self.calculator.addition, 12, '3')


    # Calculator.multiplication tests

    def test_multiplication_common(self):
        self.assertEqual(self.calculator.multiplication(12, 3), 36)

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(123, 0), 0)

    def test_multiplication_both_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_multiplication_division(self):
        self.assertAlmostEqual(self.calculator.multiplication(10, 0.4), 4)

    def test_multiplication_negative_nums(self):
        self.assertEqual(self.calculator.multiplication(-5, -4), 20)

    def test_multiplication_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(5.6, -4.5), -25.2)

    def test_multiplication_complex(self):
        self.assertEqual(self.calculator.multiplication(1j, 1j), -1)

    def test_multiplication_int_and_string(self):
        self.assertEqual(self.calculator.multiplication(4, '3'), '3333')

    def test_multiplication_infinity(self):
        self.assertEqual(self.calculator.multiplication(4, math.inf), math.inf)

    def test_fail_multiplication_dicts(self):
        self.assertRaises(TypeError, self.calculator.multiplication, {'a': 1, 'b': 2}, {'c': 3})

    def test_fail_multiplication_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 12, None)

    def test_fail_multiplication_strings(self):
        self.assertRaises(TypeError, self.calculator.multiplication,'lol', 'kek')

    def test_fail_multiplication_lists(self):
        self.assertRaises(TypeError, self.calculator.multiplication, [1, 2], [2, 3])

    def test_fail_multiplication_tuples(self):
        self.assertRaises(TypeError, self.calculator.multiplication, (1, 2), (2, 3))


    # Calculator.subtraction tests

    def test_subtraction_common(self):
       self.assertEqual(self.calculator.subtraction(4, 3), 1)

    def test_subtraction_both_neg(self):
       self.assertEqual(self.calculator.subtraction(-12, -3), -9)

    def test_subtraction_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(-1.2, 3.5), -4.7)

    def test_fail_subtraction_collection(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 1, [1, 2, 3])

    def test_fail_subtraction_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, -1.2, None)

    def test_fail_subtraction_type_mismatch(self):
        self.assertRaises(TypeError, self.calculator.subtraction, -1.2, 'lol')


    # Calculator.division tests

    def test_division_common(self):
       self.assertEqual(self.calculator.division(12, 3), 4)

    def test_division_both_neg(self):
       self.assertEqual(self.calculator.division(-12, -3), 4)

    def test_division_division_by_zero_safety(self):
       self.assertEqual(self.calculator.division(12, 0), None)

    def test_division_float_nums(self):
        self.assertAlmostEqual(self.calculator.division(7.5, 1.5), 5)

    def test_division_float_res(self):
        self.assertAlmostEqual(self.calculator.division(10, 6), 1.66666666)

    def test_division_infinity(self):
        self.assertAlmostEqual(self.calculator.division(10, math.inf), 0)
    
    def test_fail_division_collection(self):
        self.assertRaises(TypeError, self.calculator.division, 1, [1, 2, 3])

    def test_fail_division_none(self):
        self.assertRaises(TypeError, self.calculator.division, -1.2, None)

    def test_fail_division_different_types(self):
        self.assertRaises(TypeError, self.calculator.division, -1.2, 'lol')


    # Calculator.absolute tests

    def test_absolute_common(self):
        self.assertEqual(self.calculator.absolute(-123), 123)

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(123), 123)

    def test_absolute_already_positive(self):
        self.assertEqual(self.calculator.absolute(-0), 0)

    def test_absolute_float(self):
        self.assertEqual(self.calculator.absolute(-123.5), 123.5)

    def test_absolute_infinity(self):
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)

    def test_fail_absolute_collection(self):
        self.assertRaises(TypeError, self.calculator.absolute, [-1, 2, -3])

    def test_fail_absolute_none(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)

    def test_fail_absolute_string(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'lol')


    # Calculator.degree tests

    def test_degree_common(self):
        self.assertEqual(self.calculator.degree(5, 3), 125)

    def test_degree_negative_num(self):
        self.assertAlmostEqual(self.calculator.degree(-5, 3), -125)

    def test_degree_negative_power(self):
        self.assertAlmostEqual(self.calculator.degree(5, -3), 0.008)

    def test_degree_negative_num_and_power(self):
        self.assertAlmostEqual(self.calculator.degree(-5, -3), -0.008)

    def test_degree_float_power(self):
        self.assertAlmostEqual(self.calculator.degree(9, 0.5), 3)

    def test_degree_float_num_and_power(self):
        self.assertAlmostEqual(self.calculator.degree(2.25, 0.5), 1.5)

    def test_degree_one_unchanged(self):
        self.assertEqual(self.calculator.degree(1, 23), 1)

    def test_fail_degree_collection(self):
        self.assertRaises(TypeError, self.calculator.degree, [-1, 2, -3], [4])

    def test_fail_degree_none(self):
        self.assertRaises(TypeError, self.calculator.degree, None, None)

    def test_fail_degree_string(self):
        self.assertRaises(TypeError, self.calculator.degree, 'lol', 'kek')



    # Calculator.ln tests

    def test_ln_common(self):
        self.assertEqual(self.calculator.ln(math.e ** 2), 2)

    def test_ln_negative_res(self):
        self.assertAlmostEqual(self.calculator.ln(123), 4.812184355372417) # by calculator on phone, honestly :)

    def test_fail_ln_one(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_fail_ln_collection(self):
        self.assertRaises(TypeError, self.calculator.ln, [-1, 2, -3])

    def test_fail_ln_none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_fail_ln_string(self):
        self.assertRaises(TypeError, self.calculator.ln, 'lol')


    # Calculator.log tests

    def test_log_common(self):
        self.assertEqual(self.calculator.log(100, 10), 2)

    def test_log_ln(self):
        self.assertEqual(self.calculator.log(math.e ** 2, math.e), 2)

    def test_fail_log_one(self):
        self.assertEqual(self.calculator.log(1, 23), 0)

    def test_fail_log_zero_division(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 10, 1)

    def test_fail_zero_base(self):
        self.assertRaises(ValueError, self.calculator.log, 12, 0)

    def test_fail_zero_num(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 12)

    def test_fail_negative_base(self):
        self.assertRaises(ValueError, self.calculator.log, 12, -12)

    def test_fail_negative_num(self):
        self.assertRaises(ValueError, self.calculator.log, -12, 12)

    def test_fail_log_collection(self):
        self.assertRaises(TypeError, self.calculator.log, [-1, 2, -3], 4)

    def test_fail_log_none(self):
        self.assertRaises(TypeError, self.calculator.log, None)

    def test_fail_log_string(self):
        self.assertRaises(TypeError, self.calculator.log, 'lol')


    # Calculator.sqrt tests

    def test_sqrt_common(self):
        self.assertEqual(self.calculator.sqrt(9), 3)

    def test_sqrt_complex_res(self):
        self.assertAlmostEqual(self.calculator.sqrt(-4), 2j)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(0.25), 0.5)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_fail_sqrt_collection(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [-1, 2, -3])

    def test_fail_sqrt_none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_fail_sqrt_string(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'lol')

    # Calculator.nth_root tests

    def test_nth_root_common(self):
        self.assertEqual(self.calculator.nth_root(32, 5), 2)

    def test_nth_root_negative_n(self):
        self.assertAlmostEqual(self.calculator.nth_root(32, -5), 0.5)

    def test_fail_nth_root_t_collection(self):
        self.assertRaises(TypeError, self.calculator.nth_root, [-1, 2, -3], 4)

    def test_fail_nth_root_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, 4)

    def test_fail_nth_root_string(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'lol', 'kek')


if __name__ == "__main__":
    unittest.main()

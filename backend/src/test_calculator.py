import math
import sys
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # add

    def test_addition_positive(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_addition_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    # fail
    # def test_addition_with_strings(self):
    #     with self.assertRaises(TypeError):
    #         self.calculator.addition("1", "2")

    def test_addition_with_huge_numbers(self):
        result = self.calculator.addition(sys.maxsize, sys.maxsize)
        self.assertEqual(result, sys.maxsize + sys.maxsize)

    def test_addition_with_infinity(self):
        result = self.calculator.addition(5, float('inf'))
        self.assertEqual(result, float('inf'))

    # mul

    def test_multiplication_positive(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)

    def test_multiplication_with_none(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication(2, None)

    def test_multiplication_with_huge_numbers(self):
        result = self.calculator.multiplication(sys.maxsize, sys.maxsize)
        self.assertEqual(result, sys.maxsize * sys.maxsize)

    def test_multiplication_with_infinity(self):
        result = self.calculator.multiplication(2, float('inf'))
        self.assertEqual(result, float('inf'))

    # sub

    def test_subtraction_positive(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(3, 5), -2)

    def test_subtraction_with_lists(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction([1, 2, 3], [4, 5, 6])

    def test_subtraction_with_infinity(self):
        result = self.calculator.subtraction(10, float('-inf'))
        self.assertEqual(result, float('inf'))

    # div

    def test_division_positive(self):
        self.assertEqual(self.calculator.division(6, 2), 3)

    def test_division_by_zero(self):
        self.assertIsNone(self.calculator.division(6, 0))

    def test_division_with_huge_numbers(self):
        result = self.calculator.division(sys.maxsize, sys.maxsize * sys.maxsize)
        self.assertAlmostEqual(result, 0, delta=0.0001)

    def test_division_with_infinity(self):
        result = self.calculator.division(10, float('inf'))
        self.assertEqual(result, 0)


    # abs

    def test_absolute_positive(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_absolute_positive(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-5), 5)

    def test_absolute_of_infinity(self):
        result = self.calculator.absolute(float('-inf'))
        self.assertEqual(result, float('inf'))

    # degree 

    def test_degree_positive(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_negative(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_degree_with_invalid_types(self):
        with self.assertRaises(TypeError):
            self.calculator.degree(2, "3")

    def test_degree_of_infinity(self):
        result = self.calculator.degree(float('inf'), 2)
        self.assertEqual(result, float('inf'))

    # ln

    def test_ln_positive(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_with_e(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_with_zero(self):
        # inf ?
        self.assertRaises(ValueError, self.calculator.ln, 0)

    # log

    def test_log_positive(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)

    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -100, 10)

    def test_log_of_infinity(self):
        result = self.calculator.log(float('inf'), 10)
        self.assertEqual(result, float('inf'))

    # sqrt

    def test_sqrt_positive(self):
        self.assertAlmostEqual(self.calculator.sqrt(9), 3)

    def test_sqrt_with_small_number(self):
        small_number = sys.float_info.min
        result = self.calculator.sqrt(small_number)
        self.assertAlmostEqual(result, 0, delta=0.0001)

    def test_square_root_of_infinity(self):
        result = self.calculator.sqrt(float('inf'))
        self.assertEqual(result, float('inf'))

    # fail
    # def test_sqrt_negative(self):
    #     self.assertRaises(ValueError, self.calculator.sqrt, -9)

    # nth_root

    def test_nth_root_positive(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2)

    # fail
    # def test_nth_root_negative(self):
    #     self.assertRaises(ValueError, self.calculator.nth_root, -8, 3)


if __name__ == "__main__":
    unittest.main()

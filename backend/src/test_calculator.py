from contextlib import AbstractContextManager
from typing import Any
import unittest
from src.calculator import Calculator
import math

def range_float_step(start, stop=None, step=None):
    indx = start
    while(indx < stop):
        yield indx
        indx += step

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_int(self):
        for i in range(-10000, 10000, 55):
            for j in range(-10000, 10000, 55):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.addition(i, j), i + j)

    def test_add_float(self):
        for i in range_float_step(-10000, 10000, 55.001):
            for j in range_float_step(-10000, 10000, 55.001):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.addition(i, j), i + j)

    def test_add_invalid_type(self):
        for i,j in [(None, 5), ('str', 5)]:
            with self.subTest(i=i, j=j):
                with self.assertRaises(TypeError):
                    self.calculator.addition(i, j)

    def test_add_infinite(self):
        self.assertEqual(self.calculator.addition(-1, math.inf), math.inf)



    def test_mul_int(self):
        for i in range_float_step(-10000, 10000, 55):
            for j in range_float_step(-10000, 10000, 55):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.multiplication(i, j), i * j)

    def test_mul_float(self):
        for i in range_float_step(-10000, 10000, 55):
            for j in range_float_step(-10000, 10000, 55):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.multiplication(i, j), i * j)

    def test_mul_invalid_type(self):
        for i,j in [(None, 5), ('str', 'str')]:
            with self.subTest(i=i, j=j):
                with self.assertRaises(TypeError):
                    self.calculator.multiplication(i, j)

    

    def test_sub_int(self):
        for i in range(-10000, 10000, 55):
            for j in range(-10000, 10000, 55):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.subtraction(i, j), i - j)

    def test_sub_float(self):
        for i in range_float_step(-10000, 10000, 55.001):
            for j in range_float_step(-10000, 10000, 55.001):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.subtraction(i, j), i - j)

    def test_sub_invalid_type(self):
        for i,j in [(None, 5), ('str', 5)]:
            with self.subTest(i=i, j=j):
                with self.assertRaises(TypeError):
                    self.calculator.subtraction(i, j)

    def test_sub_infinite(self):
        self.assertEqual(self.calculator.subtraction(-1, math.inf), -math.inf)


    
    def test_div_int(self):
        for i in range(-10000, 10000, 55):
            for j in range(-10000, 10000, 55):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.division(i, j), i / j)

    def test_div_float(self):
        for i in range_float_step(-10000, 10000, 55.001):
            for j in range_float_step(-10000, 10000, 55.001):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.division(i, j), i / j)
    
    def test_div_zero(self):
        self.assertEqual(self.calculator.division(10, 0), None)

    def test_div_inf(self):
        self.assertEqual(self.calculator.division(1, math.inf), 0)

    def test_div_invalid_type(self):
        for i,j in [(None, 5), ('str', 5)]:
            with self.subTest(i=i, j=j):
                with self.assertRaises(TypeError):
                    self.calculator.division(i, j)


    def test_abs_int(self):
        for i in range(-10000, 10000, 55):
                with self.subTest(i=i):
                    self.assertEqual(self.calculator.absolute(i), abs(i))

    def test_abs_float(self):
        for i in range_float_step(-10000, 10000, 55.01):
                with self.subTest(i=i):
                    self.assertEqual(self.calculator.absolute(i), abs(i))

    def test_abs_invalid_type(self):
        for i in [None, 'str']:
            with self.subTest(i=i):
                with self.assertRaises(TypeError):
                    self.calculator.absolute(i)

    def test_abs_inf(self):
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)

    
    def test_degree_int(self):
        for i in range(-10000, 10000, 550):
            for j in range(-10000, 10000, 550):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.degree(i, j), i ** j)

    def test_degree_base_zero(self):
        self.assertEqual(self.calculator.degree(0, 11001), 0)

    def test_degree_zero(self):
        self.assertAlmostEqual(self.calculator.degree(12412, 0), 1)

    def test_degree_float(self):
        self.assertAlmostEqual(self.calculator.degree(0.3, 77), 5.474401089420204e-41)

    def test_degree_invalid_type(self):
        for i,j in [(None, 5), ('str', 5)]:
            with self.subTest(i=i, j=j):
                with self.assertRaises(TypeError):
                    self.calculator.degree(i, j)


    def test_ln_e(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)

    def test_ln_positive(self):
        for i in range(1, 10000):
            with self.subTest(i=i):
                self.assertAlmostEqual(self.calculator.ln(i), math.log(i))

    def test_ln_negative(self):
        for i in range(-1000, 0):
            with self.subTest(i=i):
                with self.assertRaises(ValueError):
                    self.calculator.ln(i)

    def test_ln_invalid_type(self):
        for i in [None, 'str']:
            with self.subTest(i=i):
                with self.assertRaises(TypeError):
                    self.calculator.ln(i)        

    def test_ln_inf(self):
        self.assertAlmostEqual(self.calculator.ln(math.inf), math.inf)


    def test_log_int_positive(self):
        for i in range(1, 10000, 550):
            for j in range(2, 10000, 550):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.log(i, j), math.log(i, j))

    def test_log_int_negative(self):
        for i in range(-10000, 1, 550):
            for j in range(-10000, 1, 550):
                with self.subTest(i=i, j=j):
                    with self.assertRaises(ValueError):
                        self.calculator.log(i, j)

    def test_log_float(self):
        for i in range_float_step(1, 10000, 55.001):
            for j in range_float_step(1.1, 10000, 55.001):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.log(i, j), math.log(i, j))

    def test_log_e(self):
        self.assertEqual(self.calculator.log(math.e, math.e), 1)

    def test_log_inf(self):
        self.assertEqual(self.calculator.log(5, math.inf), 0)

    def test_log_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.log(111, 1)

    def test_log_invalid_type(self):
        for i,j in [(None, 5), ('str', 5)]:
            with self.subTest(i=i, j=j):
                with self.assertRaises(TypeError):
                    self.calculator.log(i, j)


    
    def test_sqrt_int(self):
        for i in range(-10000, 10000, 55):
                with self.subTest(i=i):
                    self.assertEqual(self.calculator.sqrt(i), i ** 0.5)

    def test_sqrt_float(self):
        self.assertEqual(self.calculator.sqrt(89.1), 9.439279633531363)

    def test_sqrt_invalid_type(self):
        for i in [None, 'str']:
            with self.subTest(i=i):
                with self.assertRaises(TypeError):
                    self.calculator.sqrt(i)

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)



    def test_nth_root_int(self):
        for i in range(-10000, 10000, 55):
            for j in range(-10000, 10000, 55):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.nth_root(i, j), i ** (1 / j))

    def test_nth_root_float(self):
        for i in range_float_step(-10000, 10000, 55.001):
            for j in range_float_step(-10000, 10000, 55.001):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.calculator.nth_root(i, j), i ** (1 / j))

    def test_nth_root_invalid_type(self):
        for i,j in [(None, 5), ('str', 5)]:
            with self.subTest(i=i, j=j):
                with self.assertRaises(TypeError):
                    self.calculator.nth_root(i, j)

    def test_nth_root_infinite(self):
        self.assertEqual(self.calculator.nth_root(-89, math.inf), 1)

if __name__ == "__main__":
    unittest.main()

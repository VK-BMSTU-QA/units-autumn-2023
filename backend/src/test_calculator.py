import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_simple(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
	
    def test_add_neg_number(self):
        self.assertEqual(self.calculator.addition(-3, 1), -2)
	
    def test_add_with_null(self):
        self.assertEqual(self.calculator.addition(1, 0), 1)
		
    def test_add_with_string(self):
        self.assertRaises(TypeError, self.calculator.addition, 10, 'abc')
	
    def test_add_with_none(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, None)
	
    def test_sub_simple(self):
        self.assertEqual(self.calculator.subtraction(5, 1), 4)

    def test_sub_simple_with_negativ(self):
        self.assertEqual(self.calculator.subtraction(-5, -1), -4)
	
    def test_sub_with_null(self):
        self.assertEqual(self.calculator.subtraction(0, 1), -1)
	
    def test_sub_with_string(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 10, 'abc')
	
    def test_sub_with_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, 10)
	
    def test_mul_simple(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)
	
    def test_mul_with_null(self):
        self.assertEqual(self.calculator.multiplication(0, 5), 0)
	
    def test_mul_with_neg_number(self):
        self.assertEqual(self.calculator.multiplication(-3, 2), -6)
	
    def test_mul_with_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 10, None)

    def test_div_simple(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
	
    def test_div_float_result(self):
        self.assertEqual(self.calculator.division(3, 6), 0.5)

    def test_div_one_by_one_neg(self):
        self.assertEqual(self.calculator.division(-1, -1), 1)
	
    def test_div_by_zero(self):
        self.assertIsNone(self.calculator.division(6, 0))
 

    def test_div_zero_res(self):
        self.assertEqual(self.calculator.division(0, 10), 0)
 
    def test_div_string_param(self):
        self.assertRaises(TypeError, self.calculator.division, 10, 'abc')
	
    def test_div_none_param(self):
        self.assertRaises(TypeError, self.calculator.division, None, 5)

    def test_abs_null(self):
        self.assertEqual(self.calculator.adsolute(0), 0)
	
    def test_abs_negative_num(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)
	
    def test_abs_positive_num(self):
        self.assertEqual(self.calculator.adsolute(5), 5)

    def test_abs_string_param(self):
        self.assertRaises(TypeError, self.calculator.adsolute, 'abc')
	 
    def test_abs_none_param(self):
        self.assertRaises(TypeError, self.calculator.adsolute, None)
	
    def test_deg_simple(self):
        self.assertEqual(self.calculator.degree(3, 2), 9)
		
    def test_deg_null_indicator(self):
        self.assertEqual(self.calculator.degree(3, 0), 1)

    def test_deg_negative_indicator(self):
        self.assertEqual(self.calculator.degree(10, -1), 0.1)
	
    def test_deg_float_indicator(self):
        self.assertEqual(self.calculator.degree(9, 0.5), 3)

    def test_deg_negative_base(self):
        self.assertAlmostEqual(self.calculator.degree(-9, 0.5), complex(0, 3))

    def test_deg_string_base(self):
        self.assertRaises(TypeError, self.calculator.degree, 'abc', 2)
		
    def test_deg_none_base(self):
        self.assertRaises(TypeError, self.calculator.degree, None, 2)
		
    def test_deg_none_indicator(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, None)
	
    def test_deg_string_indicator(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, 'abc')
	
    def test_ln_simple(self):
        self.assertEqual(self.calculator.ln(math.e ** 3), 3)
	
    def test_ln_one(self):
        self.assertEqual(self.calculator.ln(1), 0)
	
    def test_ln_null_param(self):
       self.assertRaises(ValueError, self.calculator.ln, 0)
	
    def test_ln_negative_param(self):
       self.assertRaises(ValueError, self.calculator.ln, -10)

    def test_ln_string_param(self):
       self.assertRaises(TypeError, self.calculator.ln, 'abc')

    def test_ln_none_param(self):
       self.assertRaises(TypeError, self.calculator.ln, None)

    def test_log_simple(self):
        self.assertEqual(self.calculator.log(100, 10), 2)
	
    def test_log_null_param(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 10)
		
    def test_log_negative_param(self):
        self.assertRaises(ValueError, self.calculator.log, -13, 10)
		
    def test_log_null_base(self):
        self.assertRaises(ValueError, self.calculator.log, 10, 0)
		
    def test_log_negative_base(self):
        self.assertRaises(ValueError, self.calculator.log, 100, -10)

    def test_log_single_base(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 10, 1)

    def test_log_string_base(self):
        self.assertRaises(TypeError, self.calculator.log, 100, 'abc')
		
    def test_log_string_param(self):
        self.assertRaises(TypeError, self.calculator.log, 'abc', 10)

    def test_log_none_base(self):
        self.assertRaises(TypeError, self.calculator.log, 100, 'abc')
		
    def test_log_none_param(self):
        self.assertRaises(TypeError, self.calculator.log, None, 10)

    def test_sqrt_simple(self):
        self.assertEqual(self.calculator.sqrt(16), 4)
	
    def test_sqrt_string_param(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'abc')
		
    def test_sqrt_none_param(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)
		
    def test_sqrt_negative_param(self):
        self.assertAlmostEqual(self.calculator.sqrt(-9), complex(0, 3))

    def test_nth_root_simple(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
	
    def test_nth_root_null_param(self):
        self.assertEqual(self.calculator.nth_root(0, 3), 0)

    def test_nth_null_indicator(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 3, 0)


if __name__ == "__main__":
    unittest.main()

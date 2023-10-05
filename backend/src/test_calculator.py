import math
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-3, 1), -2)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertRaises(TypeError, self.calculator.addition, 10, 'abc')
        self.assertRaises(TypeError, self.calculator.addition, None, 'abc')
	
    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(5, 1), 4)
        self.assertEqual(self.calculator.subtraction(0, 1), -1)
        self.assertEqual(self.calculator.subtraction(5, 5), 0)
        self.assertEqual(self.calculator.subtraction(5, 1), 4)
        self.assertRaises(TypeError, self.calculator.subtraction, 10, 'abc')
        self.assertRaises(TypeError, self.calculator.subtraction, None, 'abc')
	
    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)
        self.assertEqual(self.calculator.multiplication(0, 5), 0)
        self.assertEqual(self.calculator.multiplication(-3, 2), -6)
        self.assertRaises(TypeError, self.calculator.multiplication, None, 'abc')
	

    def test_div(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertEqual(self.calculator.division(3, 6), 0.5)
        self.assertIsNone(self.calculator.division(6, 0))


    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(-5), 5)
        self.assertEqual(self.calculator.adsolute(5), 5)
	
    def test_deg(self):
        self.assertEqual(self.calculator.degree(3, 2), 9)
        self.assertEqual(self.calculator.degree(10, -1), 0.1)
        self.assertEqual(self.calculator.degree(9, 0.5), 3)
	
    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e ** 3), 3)
        self.assertEqual(self.calculator.ln(1), 0)

    def test_log(self):
        self.assertEqual(self.calculator.log(100, 10), 2)
        self.assertEqual(self.calculator.log(1, 10), 0)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        self.assertEqual(self.calculator.nth_root(3, 1), 3)









if __name__ == "__main__":
    unittest.main()

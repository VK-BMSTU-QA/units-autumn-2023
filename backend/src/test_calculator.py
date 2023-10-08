import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3, "Simple")
        self.assertEqual(self.calculator.addition(-12, -32), -44, "Negative numbers")
        self.assertEqual(self.calculator.addition(0, 32), 32, "1st number 0")
        self.assertEqual(self.calculator.addition(33, 0), 33, "2nd number 0")
        self.assertEqual(self.calculator.addition(33, -33), 0, "Result equal to 0")
        self.assertRaises(TypeError, self.calculator.addition, None, None)
        self.assertRaises(TypeError, self.calculator.addition, 'face', 5)
        self.assertRaises(TypeError, self.calculator.addition, 5, 'face')

    def test_substraction(self):
        self.assertEqual(self.calculator.subtraction(10, 6), 4, "Simple")
        self.assertEqual(self.calculator.subtraction(-10, -6), -4, "Both negative")
        self.assertEqual(self.calculator.subtraction(10, -6), 16, "Second negative")
        self.assertEqual(self.calculator.subtraction(-10, 6), -16, "First negative")
        self.assertEqual(self.calculator.subtraction(22.23, 15.71), 6.52, "Float numbers")
        self.assertEqual(self.calculator.subtraction(13, 0), 13, "Second number 0")
        self.assertEqual(self.calculator.subtraction(0, 13), -13, "First number 0")
        self.assertEqual(self.calculator.subtraction(129, 129), 0, "Result equal to 0")
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)
        self.assertRaises(TypeError, self.calculator.subtraction, 'face', 5)
        self.assertRaises(TypeError, self.calculator.subtraction, 5, 'face')

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(10, 6), 60, "Simple")
        self.assertEqual(self.calculator.multiplication(-10, -6), 60, "Both negative")
        self.assertEqual(self.calculator.multiplication(-10, 6), -60, "First negative")
        self.assertEqual(self.calculator.multiplication(10, -6), -60, "Second negative")
        self.assertEqual(self.calculator.multiplication(0, 24), 0, "First number 0")
        self.assertEqual(self.calculator.multiplication(24, 0), 0, "Second number 0")
        self.assertEqual(self.calculator.multiplication(24.23, 12.56), 304.3288, "Float numbers")
        self.assertEqual(self.calculator.multiplication(1, 55), 55, "Multiplication by 1")
        self.assertEqual(self.calculator.multiplication('face', 2), 'faceface', 'Number by string')
        self.assertEqual(self.calculator.multiplication(2, 'face'), 'faceface', 'String by number')
        self.assertRaises(TypeError, self.calculator.multiplication, 'abc', 'face')
        self.assertRaises(TypeError, self.calculator.multiplication, None, None)

    def test_division(self):
        self.assertEqual(self.calculator.division(10, 5), 2, "Simple")
        self.assertEqual(self.calculator.division(-10, -5), 2, "Both negative")
        self.assertEqual(self.calculator.division(10, -5), -2, "Second negative")
        self.assertEqual(self.calculator.division(-10, 5), -2, "First negative")
        self.assertEqual(self.calculator.division(11, 0), None, "Second number 0")
        self.assertEqual(self.calculator.division(0, 11), 0, "First number 0")
        self.assertEqual(self.calculator.division(24.23, 12.56), 1.929140127388535, "Float numbers")
        self.assertRaises(TypeError, self.calculator.division, 'face', 2)
        self.assertRaises(TypeError, self.calculator.division, 2, 'face')
        self.assertRaises(TypeError, self.calculator.division, None, None)

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(10), 10, "Positive")
        self.assertEqual(self.calculator.adsolute(-10), 10, "Negative")
        self.assertEqual(self.calculator.adsolute(0), 0, "Zero")
        self.assertEqual(self.calculator.adsolute(0.234), 0.234, "Positive float")
        self.assertEqual(self.calculator.adsolute(-0.234), 0.234, "Negative float")
        self.assertRaises(TypeError, self.calculator.adsolute, 'face')
        self.assertRaises(TypeError, self.calculator.adsolute, None)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(10, 2), 100, "Positive degree")
        self.assertEqual(self.calculator.degree(10, -2), 0.01, "Negative degree")
        self.assertEqual(self.calculator.degree(25, 0.5), 5, "Float degree")
        self.assertEqual(self.calculator.degree(25, 0), 1, "Degree=0")
        self.assertEqual(self.calculator.degree(0, 3), 0, "x=0")
        self.assertEqual(self.calculator.degree(-3, 2), 9, "x: negative, n: even")
        self.assertEqual(self.calculator.degree(-3, 3), -27, "x: negative, n: odd")
        self.assertRaises(TypeError, self.calculator.degree, 'face', 2)
        self.assertRaises(TypeError, self.calculator.degree, None, 3)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1, "ln(e)")
        self.assertEqual(self.calculator.ln(8), 2.0794415416798357, "ln(positive number)")
        self.assertEqual(self.calculator.ln(1), 0, "ln(1)")
        self.assertRaises(ValueError, self.calculator.ln, -13)
        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertRaises(TypeError, self.calculator.ln, 'face')
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_log(self):
        self.assertEqual(self.calculator.log(5, 5), 1, "x = n")
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertEqual(self.calculator.log(1, 10), 0)
        self.assertRaises(ZeroDivisionError, self.calculator.log, 5, 1)
        self.assertRaises(ValueError, self.calculator.log, -13, 3)
        self.assertRaises(ValueError, self.calculator.log, 0, 3)
        self.assertRaises(ValueError, self.calculator.log, 3, 0)
        self.assertRaises(ValueError, self.calculator.log, 3, -13)
        self.assertRaises(TypeError, self.calculator.log, 'face', 3)
        self.assertRaises(TypeError, self.calculator.log, None, 3)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(25), 5)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(1), 1)
        self.assertEqual(self.calculator.sqrt(-5), (1.3691967456605067e-16+2.23606797749979j))
        self.assertRaises(TypeError, self.calculator.sqrt, 'face')
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(25, 2), 5)
        self.assertEqual(self.calculator.nth_root(1024, 10), 2)
        self.assertEqual(self.calculator.nth_root(0, 10), 0)
        self.assertEqual(self.calculator.nth_root(-5, 2), (1.3691967456605067e-16 + 2.23606797749979j))
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 3, 0)
        self.assertRaises(TypeError, self.calculator.nth_root, 'face', 2)
        self.assertRaises(TypeError, self.calculator.nth_root, None, 2)


if __name__ == "__main__":
    unittest.main()

import math
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertRaises(TypeError, self.calculator.addition, "face", 5)

    def test_substraction(self):
        self.assertEqual(self.calculator.subtraction(10, 6), 4)
        self.assertEqual(self.calculator.subtraction(-10, -6), -4)
        self.assertEqual(self.calculator.subtraction(10, -6), 16)
        self.assertEqual(self.calculator.subtraction(-10, 6), -16)
        self.assertEqual(self.calculator.subtraction(22.23, 15.71), 6.52)
        self.assertEqual(self.calculator.subtraction(13, 0), 13)
        self.assertEqual(self.calculator.subtraction(0, 13), -13)
        self.assertEqual(self.calculator.subtraction(129, 129), 0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(10, 6), 60)
        self.assertEqual(self.calculator.multiplication(-10, -6), 60)
        self.assertEqual(self.calculator.multiplication(-10, 6), -60)
        self.assertEqual(self.calculator.multiplication(10, -6), -60)
        self.assertEqual(self.calculator.multiplication(0, 24), 0)
        self.assertEqual(self.calculator.multiplication(24, 0), 0)
        self.assertEqual(self.calculator.multiplication(24.23, 12.56), 304.3288)
        self.assertEqual(self.calculator.multiplication(1, 55), 55)

    def test_division(self):
        self.assertEqual(self.calculator.division(10, 5), 2)
        self.assertEqual(self.calculator.division(-10, -5), 2)
        self.assertEqual(self.calculator.division(10, -5), -2)
        self.assertEqual(self.calculator.division(-10, 5), -2)
        self.assertEqual(self.calculator.division(11, 0), None)
        self.assertEqual(self.calculator.division(0, 11), 0)
        self.assertEqual(self.calculator.division(24.23, 12.56), 1.929140127388535)

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(10), 10)
        self.assertEqual(self.calculator.adsolute(-10), 10)
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(0.234), 0.234)
        self.assertEqual(self.calculator.adsolute(-0.234), 0.234)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(10, 2), 100)
        self.assertEqual(self.calculator.degree(10, -2), 0.01)
        self.assertEqual(self.calculator.degree(25, 0.5), 5)
        self.assertEqual(self.calculator.degree(25, 0), 1)
        self.assertEqual(self.calculator.degree(0, 3), 0)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertEqual(self.calculator.ln(8), 2.0794415416798357)
        self.assertEqual(self.calculator.ln(1), 0)

    def test_log(self):
        self.assertEqual(self.calculator.log(5, 5), 1)
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertEqual(self.calculator.log(1, 10), 0)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(25), 5)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(1), 1)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(25, 2), 5)
        self.assertEqual(self.calculator.nth_root(1024, 10), 2)


if __name__ == "__main__":
    unittest.main()

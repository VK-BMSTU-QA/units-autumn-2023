import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_div(self):
        self.assertEqual(self.calculator.division(1, 2), 0.5)

    def test_div_by_0(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(-2), 2)

    def test_deg(self):
        self.assertEqual(self.calculator.degree(2, 4), 16)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(8), math.log(8))

    def test_log(self):
        self.assertEqual(self.calculator.log(27, 3), 3)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(144), 12)

    def test_nth(self):
        self.assertEqual(self.calculator.nth_root(4, 2), 2)

if __name__ == "__main__":
    unittest.main()

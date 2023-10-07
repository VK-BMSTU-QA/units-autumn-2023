import math
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertEqual(self.calculator.addition(1, math.inf), math.inf)
        self.assertEqual(self.calculator.addition('a', 'b'), 'ab')
        self.assertEqual(self.calculator.addition([1, 2], [3]), [1, 2, 3])
        self.assertRaises(TypeError, self.calculator.addition, 1, 'str')

    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(3, 4), 12)
        self.assertEqual(self.calculator.multiplication(-3, -4), 12)
        self.assertEqual(self.calculator.multiplication(3, -4), -12)
        self.assertEqual(self.calculator.multiplication(3, 0), 0)

        self.assertEqual(self.calculator.multiplication(3, math.inf), math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -3), -math.inf)

        self.assertEqual(self.calculator.multiplication('str', 2), 'strstr')
        self.assertRaises(TypeError, self.calculator.multiplication, 'str', 'str')

    # Sub tests
    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(4, 3), 1)
        self.assertEqual(self.calculator.subtraction(4, 0), 4)
        self.assertEqual(self.calculator.subtraction(4, -1), 5)
        self.assertEqual(self.calculator.subtraction(-4, -1), -3)

        self.assertEqual(self.calculator.subtraction(10, math.inf), -math.inf)
        self.assertEqual(self.calculator.subtraction(math.inf, 10), math.inf)
        self.assertTrue(math.isnan(self.calculator.subtraction(math.inf, math.inf)))

        self.assertRaises(TypeError, self.calculator.subtraction, 1, 'str')

    # Div tests
    def test_div(self):
        self.assertEqual(self.calculator.division(12, 4), 3.0)
        self.assertEqual(self.calculator.division(12, -4), -3.0)
        self.assertEqual(self.calculator.division(12, 1), 12.0)
        self.assertEqual(self.calculator.division(12, 0), None)

        self.assertEqual(self.calculator.division(math.inf, 12), math.inf)
        self.assertEqual(self.calculator.division(math.inf, -12), -math.inf)
        self.assertEqual(self.calculator.division(12, math.inf), 0)
        self.assertTrue(math.isnan(self.calculator.division(math.inf, math.inf)))

        self.assertRaises(TypeError, self.calculator.division, 1, 'str')

    # Abs tests
    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(1), 1)
        self.assertEqual(self.calculator.adsolute(-1), 1)
        self.assertEqual(self.calculator.adsolute(0), 0)

        self.assertEqual(self.calculator.adsolute(math.inf), math.inf)
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)

        self.assertRaises(TypeError, self.calculator.adsolute, 'str')

    # Degree tests
    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertAlmostEqual(self.calculator.degree(2, -3), 0.125)
        self.assertEqual(self.calculator.degree(2, 0), 1)

        self.assertEqual(self.calculator.degree(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.degree(2, math.inf), math.inf)

        self.assertRaises(TypeError, self.calculator.degree, 'str', 2)

    # Ln tests
    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(9), 2.1972245773362196)
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertRaises(ValueError, self.calculator.ln, -9)

        self.assertEqual(self.calculator.ln(math.inf), math.inf)

        self.assertRaises(TypeError, self.calculator.ln, 'str')

    # Log tests
    def test_log(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertRaises(ValueError, self.calculator.log, 8, -2)
        self.assertRaises(ZeroDivisionError, self.calculator.log, 8, 1)

        self.assertEqual(self.calculator.log(math.inf, 2), math.inf)
        self.assertTrue(math.isnan(self.calculator.log(math.inf, math.inf)))

        self.assertRaises(TypeError, self.calculator.log, 'str', 1)
        self.assertRaises(TypeError, self.calculator.log, 1, 'str')


    # Sqrt tests
    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(4), 2.0)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.sqrt, 'str')

    # Nth_root tests
    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        self.assertEqual(self.calculator.nth_root(-8, 3), 1.0000000000000002+1.7320508075688772j)
        self.assertEqual(self.calculator.nth_root(8, 1), 8)
        self.assertEqual(self.calculator.nth_root(8, 0.5), 64)

        self.assertEqual(self.calculator.nth_root(0, math.inf), 1)
        self.assertEqual(self.calculator.nth_root(math.inf, 1), math.inf)

        self.assertRaises(TypeError, self.calculator.nth_root, 'str', 1)
        self.assertRaises(TypeError, self.calculator.nth_root, 1, 'str')



if __name__ == "__main__":
    unittest.main()

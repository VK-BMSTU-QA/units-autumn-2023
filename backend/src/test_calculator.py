import math
import unittest

from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    DELTA = 1e-7

    def setUp(self):
        self.calculator = Calculator()


    def assertError(self, method, args, error):
        for arg in args:
            self.assertRaises(error, lambda: method(*arg))

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 4), 5)
        self.assertEqual(self.calculator.addition(3, 0), 3)
        self.assertEqual(self.calculator.addition(0, 4), 4)
        self.assertEqual(self.calculator.addition(-1, 1), 0)

        self.assertEqual(self.calculator.addition(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.addition(-math.inf, 1), -math.inf)
        self.assertTrue(math.isnan(self.calculator.addition(-math.inf, math.inf)))

        self.assertAlmostEqual(self.calculator.addition(-1.5, 1.7), 0.2, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.addition(2e-1, -1.2), -1, delta=self.DELTA)

        self.assertEqual(self.calculator.addition('Yeah', ' Yeah'), 'Yeah Yeah')
        self.assertEqual(self.calculator.addition('', ''), '')

        self.assertEqual(self.calculator.addition([1, 2, 3], [4]), [1, 2, 3, 4])
        self.assertEqual(self.calculator.addition([1, 2, 3], []), [1, 2, 3])
        self.assertRaises(TypeError, self.calculator.addition, 123, 'hello')


    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(3, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 4), 0)
        self.assertEqual(self.calculator.multiplication(-1, 1), -1)
        self.assertEqual(self.calculator.multiplication(-1, -5), 5)

        self.assertEqual(self.calculator.multiplication(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -1), -math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, math.inf), -math.inf)

        self.assertAlmostEqual(self.calculator.multiplication(2.5, 2.5), 6.25, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.multiplication(1e-1, 1e9), 1e8, delta=self.DELTA)

        self.assertEqual(self.calculator.multiplication('a', 4), 'aaaa')
        self.assertRaises(TypeError, self.calculator.multiplication, 'hello', 'hello')

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(7, 5), 2)
        self.assertEqual(self.calculator.subtraction(3, 0), 3)
        self.assertEqual(self.calculator.subtraction(0, 2), -2)
        self.assertEqual(self.calculator.subtraction(2, -2), 4)

        self.assertEqual(self.calculator.subtraction(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.subtraction(-math.inf, 1), -math.inf)
        self.assertTrue(math.isnan(self.calculator.subtraction(math.inf, math.inf)))

        self.assertAlmostEqual(self.calculator.subtraction(1.5, 1.7), -0.2, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.subtraction(2e-1, 1.2), -1, delta=self.DELTA)
        self.assertRaises(TypeError, self.calculator.subtraction, 123, 'hello')

    def test_div(self):
        self.assertEqual(self.calculator.division(8, 2), 4)
        self.assertEqual(self.calculator.division(0, 0), None)
        self.assertEqual(self.calculator.division(4, -2), -2)
        self.assertEqual(self.calculator.division(-3, -3), 1)

        self.assertEqual(self.calculator.division(math.inf, 4), math.inf)
        self.assertEqual(self.calculator.division(-math.inf, 4), -math.inf)
        self.assertEqual(self.calculator.division(1, math.inf), 0)
        self.assertTrue(math.isnan(self.calculator.division(math.inf, math.inf)))

        self.assertAlmostEqual(self.calculator.division(7, 5), 1.4, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.division(5, 25e-1), 2, delta=self.DELTA)

        self.assertIsNone(self.calculator.division(2, 0))
        self.assertRaises(TypeError, self.calculator.division, 123, 'hello')

    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(8), 8)
        self.assertEqual(self.calculator.adsolute(-8), 8)

        self.assertEqual(self.calculator.adsolute(math.inf), math.inf)
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)

        self.assertEqual(self.calculator.adsolute(-8.5), 8.5)
        self.assertEqual(self.calculator.adsolute(-8e-2), 8e-2)
        self.assertRaises(TypeError, self.calculator.adsolute, 'hello')

    def test_degree(self):
        self.assertEqual(self.calculator.degree(1, -1), 1)
        self.assertEqual(self.calculator.degree(-1, -1), -1)
        self.assertEqual(self.calculator.degree(-1, 2), 1)
        self.assertEqual(self.calculator.degree(8, 2), 64)
        self.assertEqual(self.calculator.degree(8, 1), 8)
        self.assertEqual(self.calculator.degree(1, 8), 1)
        self.assertEqual(self.calculator.degree(6, 0), 1)
        self.assertEqual(self.calculator.degree(0, 6), 0)

        self.assertEqual(self.calculator.degree(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.degree(math.inf, 0), 1)
        self.assertEqual(self.calculator.degree(1, math.inf), 1)
        self.assertEqual(self.calculator.degree(2, math.inf), math.inf)

        self.assertAlmostEqual(self.calculator.degree(2, -1), 0.5, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.degree(2e-1, -1), 5, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.degree(4, -0.5), 0.5, delta=self.DELTA)
        self.assertRaises(TypeError, self.calculator.degree, 'hello', 2)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertEqual(self.calculator.ln(math.e ** 2), 2)
        self.assertEqual(self.calculator.ln(math.e ** 1.5), 1.5)
        self.assertEqual(self.calculator.ln(1), 0)

        self.assertEqual(self.calculator.ln(math.inf), math.inf)

        invalid_args = [(-math.inf,), (0,)]
        self.assertError(self.calculator.ln, invalid_args, ValueError)
        self.assertRaises(TypeError, self.calculator.ln, 'hello')

    def test_log(self):
        self.assertEqual(self.calculator.log(4, 2), 2)
        self.assertEqual(self.calculator.log(1, 2), 0)
        self.assertEqual(self.calculator.log(2, 2), 1)

        self.assertEqual(self.calculator.log(math.inf, 2), math.inf)
        self.assertTrue(math.isnan(self.calculator.log(math.inf, math.inf)))

        self.assertAlmostEqual(self.calculator.log(1.5, 2.25), 0.5, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.log(2.25, 1.5), 2, delta=self.DELTA)

        invalid_args = [(123, -math.inf), (123, 0), (0, 123), (-math.inf, 123)]
        self.assertError(self.calculator.log, invalid_args, ValueError)
        self.assertRaises(TypeError, self.calculator.log, 'hello', 1)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(1), 1)
        self.assertEqual(self.calculator.sqrt(4), 2)

        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
        self.assertAlmostEqual(self.calculator.sqrt(2.25), 1.5, delta=self.DELTA)
        self.assertRaises(TypeError, self.calculator.sqrt, 'hello')

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(1, 3), 1)
        self.assertEqual(self.calculator.nth_root(1, 2), 1)
        self.assertEqual(self.calculator.nth_root(8, 3), 2)

        self.assertEqual(self.calculator.nth_root(0, math.inf), 1)
        self.assertEqual(self.calculator.nth_root(math.inf, math.inf), 1)
        self.assertEqual(self.calculator.nth_root(math.inf, 1), math.inf)
        self.assertRaises(TypeError, self.calculator.nth_root, 'hello', 1)


if __name__ == "__main__":
    unittest.main()

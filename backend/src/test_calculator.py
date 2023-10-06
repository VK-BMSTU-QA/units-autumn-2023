import math
import unittest

from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    DELTA = 1e-7

    def setUp(self):
        self.calculator = Calculator()

        self.singles_invalid_types = self.get_invalid_args(num_args=1)
        self.double_invalid_types = self.get_invalid_args(num_args=2)

    @staticmethod
    def get_invalid_args(num_args):
        invalid_types = ['1', None, [1], {1}]
        args = []

        if num_args == 1:
            for cur in invalid_types:
                args.append((cur,))
        else:
            for i in range(len(invalid_types)):
                for j in range(i + 1, len(invalid_types)):
                    args.append((invalid_types[i], invalid_types[j]))

        return args

    def assertError(self, method, args, error):
        for arg in args:
            self.assertRaises(error, lambda: method(*arg))

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertEqual(self.calculator.addition(0, 2), 2)
        self.assertEqual(self.calculator.addition(-1, 1), 0)

        self.assertEqual(self.calculator.addition(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.addition(-math.inf, 1), -math.inf)
        self.assertTrue(math.isnan(self.calculator.addition(-math.inf, math.inf)))

        self.assertAlmostEqual(self.calculator.addition(-1.5, 1.7), 0.2, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.addition(2e-1, -1.2), -1, delta=self.DELTA)

        self.assertEqual(self.calculator.addition('hello', ' world'), 'hello world')
        self.assertEqual(self.calculator.addition('', ''), '')

        self.assertEqual(self.calculator.addition([1, 2, 3], [3]), [1, 2, 3, 3])
        self.assertEqual(self.calculator.addition([1, 2, 3], []), [1, 2, 3])

        self.assertError(self.calculator.addition, self.double_invalid_types, TypeError)

    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(3, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 2), 0)
        self.assertEqual(self.calculator.multiplication(-1, 3), -3)
        self.assertEqual(self.calculator.multiplication(-1, -3), 3)

        self.assertEqual(self.calculator.multiplication(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -1), -math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, math.inf), -math.inf)

        self.assertAlmostEqual(self.calculator.multiplication(1.5, 1.5), 2.25, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.multiplication(1e-1, 1e10), 1e9, delta=self.DELTA)

        self.assertEqual(self.calculator.multiplication('a', 3), 'aaa')

        self.assertError(self.calculator.multiplication, self.double_invalid_types, TypeError)

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

        self.assertError(self.calculator.subtraction, self.double_invalid_types, TypeError)

    def test_div(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertEqual(self.calculator.division(0, 1), 0)
        self.assertEqual(self.calculator.division(2, -2), -1)
        self.assertEqual(self.calculator.division(-2, -2), 1)

        self.assertEqual(self.calculator.division(math.inf, 5), math.inf)
        self.assertEqual(self.calculator.division(-math.inf, 5), -math.inf)
        self.assertEqual(self.calculator.division(1, math.inf), 0)
        self.assertTrue(math.isnan(self.calculator.division(math.inf, math.inf)))

        self.assertAlmostEqual(self.calculator.division(7, 5), 1.4, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.division(5, 25e-1), 2, delta=self.DELTA)

        self.assertIsNone(self.calculator.division(2, 0))

        self.assertError(self.calculator.division, self.double_invalid_types, TypeError)

    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(6), 6)
        self.assertEqual(self.calculator.adsolute(-6), 6)

        self.assertEqual(self.calculator.adsolute(math.inf), math.inf)
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)

        self.assertEqual(self.calculator.adsolute(-1.5), 1.5)
        self.assertEqual(self.calculator.adsolute(-15e-2), 15e-2)

        self.assertError(self.calculator.adsolute, self.singles_invalid_types, TypeError)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(6, 2), 36)
        self.assertEqual(self.calculator.degree(6, 1), 6)
        self.assertEqual(self.calculator.degree(1, 6), 1)
        self.assertEqual(self.calculator.degree(6, 0), 1)
        self.assertEqual(self.calculator.degree(0, 6), 0)
        self.assertEqual(self.calculator.degree(1, -1), 1)
        self.assertEqual(self.calculator.degree(-1, -1), -1)
        self.assertEqual(self.calculator.degree(-1, 2), 1)

        self.assertEqual(self.calculator.degree(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.degree(math.inf, 0), 1)
        self.assertEqual(self.calculator.degree(1, math.inf), 1)
        self.assertEqual(self.calculator.degree(2, math.inf), math.inf)

        self.assertAlmostEqual(self.calculator.degree(2, -1), 0.5, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.degree(2e-1, -1), 5, delta=self.DELTA)
        self.assertAlmostEqual(self.calculator.degree(4, -0.5), 0.5, delta=self.DELTA)

        self.assertError(self.calculator.degree, self.double_invalid_types, TypeError)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertEqual(self.calculator.ln(math.e ** 2), 2)
        self.assertEqual(self.calculator.ln(math.e ** 1.5), 1.5)
        self.assertEqual(self.calculator.ln(1), 0)

        self.assertEqual(self.calculator.ln(math.inf), math.inf)

        invalid_args = [(-math.inf,), (0,)]
        self.assertError(self.calculator.ln, invalid_args, ValueError)
        self.assertError(self.calculator.ln, self.singles_invalid_types, TypeError)

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
        self.assertError(self.calculator.log, self.double_invalid_types, TypeError)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(1), 1)
        self.assertEqual(self.calculator.sqrt(4), 2)

        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
        self.assertAlmostEqual(self.calculator.sqrt(2.25), 1.5, delta=self.DELTA)

        self.assertError(self.calculator.sqrt, self.singles_invalid_types, TypeError)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(1, 3), 1)
        self.assertEqual(self.calculator.nth_root(1, 2), 1)
        self.assertEqual(self.calculator.nth_root(8, 3), 2)

        self.assertEqual(self.calculator.nth_root(0, math.inf), 1)
        self.assertEqual(self.calculator.nth_root(math.inf, math.inf), 1)
        self.assertEqual(self.calculator.nth_root(math.inf, 1), math.inf)

        self.assertError(self.calculator.nth_root, self.double_invalid_types, TypeError)


if __name__ == "__main__":
    unittest.main()

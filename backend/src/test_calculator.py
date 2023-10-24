import unittest
from src.calculator import Calculator
import math
from dataclasses import dataclass


@dataclass
class TestCase:
    msg: str
    args: tuple[float]
    res: float
    delta: float = 1e-7


@dataclass
class ExceptionTestCase:
    msg: str
    args: tuple[float]
    exception: any


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def run_subtests(self, test_cases, func):
        for test_case in test_cases:
            with self.subTest(msg=test_case.msg):
                self.assertAlmostEqual(
                    func(*test_case.args), test_case.res, delta=test_case.delta)
                
    def run_subtests_error(self, test_cases, func):
        for test_case in test_cases:
            with self.subTest(msg=test_case.msg):
                self.assertRaises(test_case.exception, func, *test_case.args)

    def test_add(self):
        test_cases = (
            TestCase(msg="positive", args=(1.2, 2), res=3.2),
            TestCase(msg="zero", args=(2.3, 0), res=2.3),
            TestCase(msg="negative", args=(3, -2.1), res=0.9),
        )

        self.run_subtests(test_cases, self.calculator.addition)

    def test_sub(self):
        test_cases = (
            TestCase(msg="positive", args=(5.1, 1), res=4.1),
            TestCase(msg="zero", args=(3, 0), res=3),
            TestCase(msg="negative", args=(5, -3.5), res=8.5),
        )

        self.run_subtests(test_cases, self.calculator.subtraction)

    def test_mult(self):
        test_cases = (
            TestCase(msg="positive", args=(5.1, 2), res=10.2),
            TestCase(msg="zero", args=(3, 0), res=0),
            TestCase(msg="negative", args=(5, -3.2), res=-16),
            TestCase(msg="one", args=(6.5, 1), res=6.5),
        )

        self.run_subtests(test_cases, self.calculator.multiplication)

    def test_div(self):
        test_cases = (
            TestCase(msg="positive", args=(6, 4), res=1.5),
            TestCase(msg="negative", args=(5, -2), res=-2.5),
            TestCase(msg="one", args=(6.5, 1), res=6.5),
            TestCase(msg="zero divident", args=(0, 5.1), res=0),
            TestCase(msg="zero divisor", args=(3, 0), res=None),
            TestCase(msg="zero by zero", args=(0, 0), res=None),
        )

        self.run_subtests(test_cases, self.calculator.division)

    def test_abs(self):
        test_cases = (
            TestCase(msg="positive", args=(3.3,), res=3.3),
            TestCase(msg="negative", args=(-5.3,), res=5.3),
            TestCase(msg="zero", args=(0,), res=0),
        )

        self.run_subtests(test_cases, self.calculator.adsolute)

    def test_degree(self):
        test_cases = (
            TestCase(msg="positive", args=(2, 3), res=8),
            TestCase(msg="negative", args=(2, -3), res=0.125),
            TestCase(msg="zero", args=(8.5, 0), res=1),
            TestCase(msg="float", args=(9, 1.5), res=27),
        )

        self.run_subtests(test_cases, self.calculator.degree)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.exp(1.5)), 1.5)

    def test_ln_error(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)

    def test_log_error(self):
        test_cases = (
            ExceptionTestCase(msg="one base", args=(12, 1), exception=ZeroDivisionError),
            ExceptionTestCase(msg="negative base", args=(8, -3), exception=ValueError),
        )
        self.run_subtests_error(test_cases, self.calculator.log)


    def test_sqrt(self):
        test_cases = (
            TestCase(msg="positive", args=(16,), res=4),
            TestCase(msg="negative", args=(-4,), res=2j),
            TestCase(msg="zero", args=(0,), res=0),
        )

        self.run_subtests(test_cases, self.calculator.sqrt)

    def test_nth_root(self):
        test_cases = (
            TestCase(msg="positive", args=(16, 4), res=2),
            TestCase(msg="degree negative", args=(8, -3), res=0.5),
            TestCase(msg="radicand negative", args=(-8, 3), res=1 + 1.73j, delta=0.01),
            TestCase(msg="float", args=(3, 0.5), res=9),
        )

        self.run_subtests(test_cases, self.calculator.nth_root)

    def test_nth_root_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 8, 0)


if __name__ == "__main__":
    unittest.main()

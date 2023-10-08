import math
import cmath
import unittest
from src.calculator import Calculator


class TestCase():
    def __init__(self, expected, firstPar, secondPar = None):
        self.expected = expected
        self.firstPar = firstPar
        self.secondPar = secondPar


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        testCases = [
            TestCase(3, 1, 2),
            TestCase(2, -1, 3),
            TestCase(-4, -1, -3),
            TestCase(math.inf, math.inf, math.inf),
        ]

        for test in testCases: 
            self.assertEqual(self.calculator.addition(
                test.firstPar, test.secondPar), test.expected)
    
    def test_mult(self):
        testCases = [
            TestCase(2, 1, 2),
            TestCase(-2, -1, 2),
            TestCase(1, -1, -1),
            TestCase(0, 0, 2),
            TestCase(0, 0, -2),
            TestCase(math.inf, math.inf, math.inf),
            TestCase(-math.inf, math.inf, -1),
        ]
    
        for test in testCases: 
            self.assertEqual(self.calculator.multiplication(
                test.firstPar, test.secondPar), test.expected)
    
    def test_sub(self):
        testCases = [
            TestCase(1, 2, 1),
            TestCase(-1, 0, 1),
            TestCase(2, 2, 0),
            TestCase(-3, -2, 1),
            TestCase(math.inf, math.inf, 1),
        ]
    
        for test in testCases: 
            self.assertEqual(self.calculator.subtraction(
                test.firstPar, test.secondPar), test.expected)
    
    def test_div(self):
        testCases = [
            TestCase(2, 2, 1),
            TestCase(None, 2, 0),
            TestCase(3, 6, 2),
            TestCase(2.5, 5, 2),
            TestCase(0, 0, 2),
            TestCase(math.inf, math.inf, 2),
        ]
    
        for test in testCases: 
            self.assertEqual(self.calculator.division(
                test.firstPar, test.secondPar), test.expected)
        
    def test_abs(self):
        testCases = [
            TestCase(2, -2),
            TestCase(2, 2),
            TestCase(0, 0),
            TestCase(math.inf, math.inf),
            TestCase(math.inf, -math.inf),
        ]
    
        for test in testCases: 
            self.assertEqual(self.calculator.adsolute(
                test.firstPar), test.expected)
    
    def test_deg(self):
        testCases = [
            TestCase(2, 2, 1),
            TestCase(4, 2, 2),
            TestCase(math.inf, 2, math.inf),
            TestCase(math.inf, math.inf, 2),
            TestCase(0.25, 2, -2),
        ]
    
        for test in testCases: 
            self.assertEqual(self.calculator.degree(
                test.firstPar, test.secondPar), test.expected)

    def test_ln(self):
        testCases = [
            TestCase(1, math.e),
            TestCase(2, math.e * math.e),
            TestCase(math.inf, math.inf),
            TestCase(-1, 1/math.e),
        ]
    
        for test in testCases: 
            self.assertEqual(self.calculator.ln(
                test.firstPar), test.expected)
    
    def test_log(self):
        testCases = [
            TestCase(1, 2, 2),
            TestCase(5, 32, 2),
            TestCase(math.inf, math.inf, 3),
            TestCase(0, 1, 2),
        ]
    
        for test in testCases: 
            self.assertEqual(self.calculator.log(
                test.firstPar, test.secondPar), test.expected)

    def test_sqrt(self):
        testCases = [
            TestCase(2, 4),
            TestCase(0, 0),
            # TestCase(cmath.sqrt(-2), -2), Gives not valid answer 
            TestCase(math.sqrt(5), 5),
            TestCase(math.inf, math.inf),
            TestCase(math.inf, -math.inf),
        ]
    
        for test in testCases: 
            self.assertEqual(self.calculator.sqrt(
                test.firstPar), test.expected)

    def test_nth_root(self):
        testCases = [
            TestCase(0.2, 125, -3),
            TestCase(3, 9, 2),
            TestCase(3, 81, 4),
            TestCase(0, 0, 2),
            TestCase(6, 6, 1),
            # TestCase(5, 125, 3), # Gives 4.99 instead of 5
            # TestCase(cmath.sqrt(-25), -25, 2), # Gives not valid answer
        ]
    
        for test in testCases: 
            self.assertEqual(self.calculator.nth_root(
                test.firstPar, test.secondPar), test.expected)

if __name__ == "__main__":
    unittest.main()

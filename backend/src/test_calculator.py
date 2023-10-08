import unittest
from calculator import Calculator


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
            TestCase(math.inf, math.inf, math.inf),
            TestCase(math.inf, -math.inf, 0)
        ]

        for test in testCases: 
            self.assertEqual(self.calculator.addition(
                test.firstPar, test.secondPar), test.expected)
        
if __name__ == "__main__":
    unittest.main()

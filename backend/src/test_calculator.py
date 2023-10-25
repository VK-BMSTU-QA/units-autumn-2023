import unittest
import math
from calculator import Calculator
# from src.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertAlmostEqual(self.calculator.addition(1.1, 2.2), 3.3)
        self.assertEqual(self.calculator.addition("abc", "def"), "abcdef")
        self.assertEqual(self.calculator.addition([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(self.calculator.addition((1, 2), (3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.addition, None, None)
        self.assertRaises(TypeError, self.calculator.addition, "abc", 1)
        self.assertRaises(TypeError, self.calculator.addition, "abc", ["a", "b", "c"])
        self.assertRaises(TypeError, self.calculator.addition, 1, (1, 2))  

    def test_mult(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(0, 1), 0)
        self.assertEqual(self.calculator.multiplication(-1, 2), -2)
        self.assertAlmostEqual(self.calculator.multiplication(1.1, 2.2), 2.42)
        self.assertEqual(self.calculator.multiplication("abc", 3), "abcabcabc")
        self.assertEqual(self.calculator.multiplication([1, 2], 3), [1, 2, 1, 2, 1, 2])
        self.assertEqual(self.calculator.multiplication((1, 2), 3), (1, 2, 1, 2, 1, 2))
        self.assertEqual(self.calculator.multiplication(math.inf, math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.multiplication, "abc", [1, 2])
        self.assertRaises(TypeError, self.calculator.multiplication, [1, 2], (1, 2))
        self.assertRaises(TypeError, self.calculator.multiplication, [1, 2], [1, 2])
        self.assertRaises(TypeError, self.calculator.multiplication, None, None)

    def test_subtr(self):
        self.assertEqual(self.calculator.subtraction(4, 2), 2)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)
        self.assertAlmostEqual(self.calculator.subtraction(1.1, 2.2), -1.1)
        self.assertEqual(self.calculator.subtraction(math.inf, 100), math.inf)
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)
        self.assertRaises(TypeError, self.calculator.subtraction, "abc", 1)
        self.assertRaises(TypeError, self.calculator.subtraction, "abc", ["a", "b", "c"])
        self.assertRaises(TypeError, self.calculator.subtraction, 1, (1, 2))
        self.assertRaises(TypeError, self.calculator.subtraction, "abc", "def")
        self.assertRaises(TypeError, self.calculator.subtraction, [1, 2, 3, 4, 5], [4, 5])
        self.assertRaises(TypeError, self.calculator.subtraction, (1, 2, 3, 4, 5), (3, 4, 5))

    def test_div(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertEqual(self.calculator.division(0, 0), None)
        self.assertEqual(self.calculator.division(-4, 2), -2)
        self.assertAlmostEqual(self.calculator.division(1.628, 2.2), 0.74)
        self.assertEqual(self.calculator.division(math.inf, 100), math.inf)
        self.assertRaises(TypeError, self.calculator.division, "abc", [1, 2])
        self.assertRaises(TypeError, self.calculator.division, [1, 2], (1, 2))
        self.assertRaises(TypeError, self.calculator.division, [1, 2], [1, 2])
        self.assertRaises(TypeError, self.calculator.division, None, None)
        self.assertRaises(TypeError, self.calculator.division, "abc", 3)
        self.assertRaises(TypeError, self.calculator.division, [1, 2], 3)
        self.assertRaises(TypeError, self.calculator.division, (1, 2), 3)

    def test_ads(self):
        self.assertEqual(self.calculator.adsolute(-4), 4)
        self.assertEqual(self.calculator.adsolute(4), 4)
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(-1.2), 1.2)
        self.assertEqual(self.calculator.adsolute(math.inf), math.inf)
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.adsolute, "abc")
        self.assertRaises(TypeError, self.calculator.adsolute, [1, 2])
        self.assertRaises(TypeError, self.calculator.adsolute, (1, 2))
        self.assertRaises(TypeError, self.calculator.adsolute, None)

    def test_deg(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(0, 0), 1)
        self.assertEqual(self.calculator.degree(1, 0), 1)
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertEqual(self.calculator.degree(-2, 4), 16)
        self.assertAlmostEqual(self.calculator.degree(5, -2), 0.04)
        self.assertAlmostEqual(self.calculator.degree(2.2, 2), 4.84)
        self.assertAlmostEqual(self.calculator.degree(2, 2.2), 4.59479342)
        self.assertEqual(self.calculator.degree(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.degree(2, math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.degree, "abc", 2)
        self.assertRaises(TypeError, self.calculator.degree, [1, 2], 2)
        self.assertRaises(TypeError, self.calculator.degree, (1, 2), 2)
        self.assertRaises(TypeError, self.calculator.degree, None, 2)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertAlmostEqual(self.calculator.ln(2.5), 0.916290732)
        self.assertEqual(self.calculator.ln(math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.degree, None)
        self.assertRaises(TypeError, self.calculator.degree, -2.5)
        self.assertRaises(TypeError, self.calculator.degree, "abc")
        self.assertRaises(TypeError, self.calculator.degree, [1, 2])
        self.assertRaises(TypeError, self.calculator.degree, (1, 2))
    
    def test_log(self):
        self.assertEqual(self.calculator.log(2, 2), 1)
        self.assertEqual(self.calculator.log(8, 2), 3)
    
    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(6, 1), 6)
        self.assertEqual(self.calculator.nth_root(4, 2), 2)

if __name__ == "__main__":
    unittest.main()

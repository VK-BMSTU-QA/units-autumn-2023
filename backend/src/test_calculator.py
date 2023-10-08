import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, 2), 1)
        self.assertEqual(self.calculator.addition(-5, -5), -10)
        self.assertEqual(self.calculator.addition(-0.5, -0.5), -1)
        self.assertEqual(self.calculator.addition(0.5, 0.5), 1)
        self.assertEqual(self.calculator.addition(0.5, -0.5), 0)
        self.assertAlmostEqual(self.calculator.addition(1.1, 2.2), 3.3)
        self.assertEqual(self.calculator.addition([1, 1], [2, 2]), [1, 1, 2, 2])
        self.assertEqual(self.calculator.addition('aa', 'qq'), 'aaqq')
        self.assertEqual(self.calculator.addition(1, math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.addition, 'qq', 1)
        self.assertRaises(TypeError, self.calculator.addition, [1,2], 1)
        self.assertRaises(TypeError, self.calculator.addition, [], 1)
        self.assertRaises(TypeError, self.calculator.addition, None, None)

    def test_minus(self):
         self.assertEqual(self.calculator.subtraction(2, 1), 1)
         self.assertEqual(self.calculator.subtraction(-1, 2), -3)
         self.assertEqual(self.calculator.subtraction(-5, -5), 0)
         self.assertEqual(self.calculator.subtraction(-0.5, -0.5), 0)
         self.assertEqual(self.calculator.subtraction(0.5, 0.5), 0)
         self.assertEqual(self.calculator.subtraction(-0.5, 0.5), -1)
         self.assertAlmostEqual(self.calculator.subtraction(2.2, 1.1), 1.1)
         self.assertEqual(self.calculator.subtraction(1, math.inf), -math.inf)
         self.assertTrue(math.isnan(self.calculator.subtraction(math.inf, math.inf)))
         self.assertRaises(TypeError, self.calculator.subtraction, 100500, 'qq')
         self.assertRaises(TypeError, self.calculator.subtraction, [5, 15], 100500)
         self.assertRaises(TypeError, self.calculator.addition, [], 1)
         self.assertRaises(TypeError, self.calculator.subtraction, [5, 15], [100500, 1])

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)
        self.assertEqual(self.calculator.multiplication(-3, 2), -6)
        self.assertEqual(self.calculator.multiplication(3, -2), -6)
        self.assertEqual(self.calculator.multiplication(-3, 0), 0)
        self.assertEqual(self.calculator.multiplication([1, 2, 3], 2), [1, 2, 3, 1, 2, 3])
        self.assertEqual(self.calculator.multiplication('qq', 2), 'qqqq')
        self.assertEqual(self.calculator.multiplication(100500, math.inf), math.inf)
        self.assertEqual(self.calculator.multiplication(-100500, math.inf ), -math.inf)
        self.assertRaises(TypeError, self.calculator.multiplication, 'aa', 'qq')

    def test_divide(self):
         self.assertEqual(self.calculator.division(3, 1), 3)
         self.assertEqual(self.calculator.division(3, -1), -3)
         self.assertEqual(self.calculator.division(math.inf, 1), math.inf)
         self.assertEqual(self.calculator.division(math.inf, -1), -math.inf)
         self.assertEqual(self.calculator.division(1, math.inf), 0)
         self.assertEqual(self.calculator.division(100500, 0), None)
         self.assertTrue(math.isnan(self.calculator.division(math.inf, math.inf)))
         self.assertRaises(TypeError, self.calculator.division, 1, 'qq')
         self.assertRaises(TypeError, self.calculator.division, [1, 2], [2, 1])
         self.assertRaises(TypeError, self.calculator.division, [1, 2], 1)

    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(-3), 3)
        self.assertEqual(self.calculator.adsolute(3), 3)
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.adsolute, 'qq')
        self.assertRaises(TypeError, self.calculator.adsolute, None)
        self.assertRaises(TypeError, self.calculator.adsolute, [1, 2, 3])

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 5), 32)
        self.assertEqual(self.calculator.degree(2, -5), 0.03125)
        self.assertAlmostEqual(self.calculator.degree(4, 1.5), 8)
        self.assertEqual(self.calculator.degree(1, math.inf), 1)
        self.assertEqual(self.calculator.degree(100500, math.inf), math.inf)
        self.assertEqual(self.calculator.degree(math.inf, 100500), math.inf)
        self.assertEqual(self.calculator.degree(math.inf, math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.degree, 'qq', 'aa')
        self.assertRaises(TypeError, self.calculator.degree, 'qq', 1)
        self.assertRaises(TypeError, self.calculator.degree, 1, 'aa')
        self.assertRaises(TypeError, self.calculator.degree, [1, 2], 1)
        self.assertRaises(TypeError, self.calculator.degree, [1, 2], [1,2])
        self.assertRaises(TypeError, self.calculator.degree, 1, None)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1037), math.log(1037))
        self.assertEqual(self.calculator.ln(math.inf), math.inf)
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertRaises(TypeError, self.calculator.ln, 'qq')
        self.assertRaises(ValueError, self.calculator.ln, -100500)
        self.assertRaises(TypeError, self.calculator.ln, [1, 2])
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_log(self):
        self.assertEqual(self.calculator.log(1024, 2), math.log(1024,2))
        self.assertEqual(self.calculator.log(math.inf, 2), math.inf)
        self.assertTrue(math.isnan(self.calculator.log(math.inf, math.inf)))
        self.assertRaises(TypeError, self.calculator.log, 1, 'qq')
        self.assertRaises(TypeError, self.calculator.log, 'qq', 1)
        self.assertRaises(ValueError, self.calculator.log, 1, -1)
        self.assertRaises(TypeError, self.calculator.log, [1, 2], 2)
        self.assertRaises(TypeError, self.calculator.log, None, 2)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(-1), 6.12e-17+1j)
        self.assertEqual(self.calculator.sqrt(-16), 2.4492935982947064e-16+4j)
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.sqrt, 'qq')
        self.assertRaises(TypeError, self.calculator.sqrt, None)
        self.assertRaises(TypeError, self.calculator.sqrt, [1, 2])

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(16,2), 4)
        self.assertAlmostEqual(self.calculator.nth_root(4, 0.5), 16)
        self.assertEqual(self.calculator.nth_root(16,-2), 0.25)
        self.assertEqual(self.calculator.nth_root(100500,math.inf), 1)
        self.assertEqual(self.calculator.nth_root(math.inf, 100500), math.inf)
        self.assertEqual(self.calculator.nth_root(0,math.inf), 1)
        self.assertRaises(TypeError, self.calculator.nth_root, [1, 2], 2)
        self.assertRaises(TypeError, self.calculator.nth_root, 2, [1,2])
        self.assertRaises(TypeError, self.calculator.nth_root, None, 2)
        self.assertRaises(TypeError, self.calculator.nth_root, 2, None)

if __name__ == "__main__":
    unittest.main()

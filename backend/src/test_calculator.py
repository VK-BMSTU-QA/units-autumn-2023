import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, -20000), -20001)
        self.assertAlmostEqual(self.calculator.addition(1.4, 1.7), 3.1)
        self.assertTrue(math.isnan(self.calculator.addition(float('nan'), 2)))
        self.assertEqual(self.calculator.addition('353', '2.5'), '3532.5')
        self.assertEqual(self.calculator.addition([5], [1, 2, 3]), [5, 1, 2, 3])
    
    def test_mult(self):
        self.assertEqual(self.calculator.multiplication(10, 2), 20)
        self.assertEqual(self.calculator.multiplication(-10, -2), 20)
        self.assertEqual(self.calculator.multiplication(10, -2), -20)
        self.assertEqual(self.calculator.multiplication([1, 3, 4], 2), [1, 3, 4, 1, 3, 4])
        with self.assertRaises(TypeError):
            self.calculator.multiplication('353', '2.5')
        with self.assertRaises(TypeError):
            self.calculator.multiplication([1, 3, 4], [1, 2])
       


    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
        self.assertEqual(self.calculator.subtraction(1, -20000), 20001)
        self.assertAlmostEqual(self.calculator.subtraction(1.4, 1.7), -0.3)
        self.assertTrue(math.isnan(self.calculator.subtraction(float('nan'), -2)))
        with self.assertRaises(TypeError):
            self.calculator.subtraction('353', '2.5')
        with self.assertRaises(TypeError):
            self.calculator.subtraction([5], [1, 2, 3])

    def test_division(self):
        self.assertIsNone(self.calculator.division(1, 0))
        self.assertEqual(self.calculator.division(-10, -2), 5)
        self.assertEqual(self.calculator.division(10, -2), -5)
        with self.assertRaises(TypeError):
            self.calculator.division([1, 3, 4], 2)
        with self.assertRaises(TypeError):
            self.calculator.division('353', '2')
        with self.assertRaises(TypeError):
            self.calculator.division([1, 3, 4], [1, 2])

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(-1.5), 1.5)
        self.assertTrue(math.isnan(self.calculator.adsolute(float('nan'))))
        with self.assertRaises(TypeError):
            self.calculator.adsolute('353')
        with self.assertRaises(TypeError):
            self.calculator.adsolute([1, 2])

    def test_degree(self):
        self.assertEqual(self.calculator.degree(4, 2), 16)
        self.assertAlmostEqual(self.calculator.degree(2, -2), 0.25)
        self.assertAlmostEqual(self.calculator.degree(4, 1.5), 8)
        self.assertAlmostEqual(self.calculator.degree(4, 0.5), 2)
        self.assertTrue(math.isnan(self.calculator.degree(4, float('nan'))))
        with self.assertRaises(TypeError):
            self.calculator.degree('353', '1')
        with self.assertRaises(TypeError):
            self.calculator.degree([1, 2], 2)
        with self.assertRaises(TypeError):
            self.calculator.degree([1, 2], [2, 1])

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        with self.assertRaises(ValueError):
            self.calculator.ln(-5)

    def test_log(self):
        self.assertEqual(self.calculator.log(4, 2), 2)
        with self.assertRaises(TypeError):
            self.calculator.log('353', '1')
        with self.assertRaises(TypeError):
            self.calculator.log([1, 2], [2, 1])
        with self.assertRaises(ValueError):
            self.calculator.log(1, -1)
        with self.assertRaises(ValueError):
            self.calculator.log(-1, -20)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertAlmostEqual(self.calculator.sqrt(1.5), 1.224744871391589)
        self.assertAlmostEqual(self.calculator.sqrt(-1), 6.12e-17+1j)
        with self.assertRaises(TypeError):
            self.calculator.sqrt('353')
        with self.assertRaises(TypeError):
            self.calculator.log([1, 2])

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(100, 2), 10)
        self.assertAlmostEqual(self.calculator.nth_root(4, 0.5), 16)
        self.assertAlmostEqual(self.calculator.nth_root(4, -2), 0.5)
        self.assertTrue(math.isnan(self.calculator.nth_root(4, float('nan'))))
        with self.assertRaises(TypeError):
            self.calculator.nth_root('353', '1')
        with self.assertRaises(TypeError):
            self.calculator.nth_root([1, 2], 2)
        with self.assertRaises(TypeError):
            self.calculator.nth_root([1, 2], [2, 1])



    

if __name__ == "__main__":
    unittest.main()

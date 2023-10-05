import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    def test_mult(self):
        self.assertEqual(self.calculator.multiplication(10, 2), 20)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_division(self):
        self.assertIsNone(self.calculator.division(1, 0))

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(-1.5), 1.5)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(4, 2), 16)

    def test_ln(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-5)

    def test_log(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1, -20)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(-1), 6.123233995736766e-17+1j)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(100, 2), 10)

    

if __name__ == "__main__":
    unittest.main()

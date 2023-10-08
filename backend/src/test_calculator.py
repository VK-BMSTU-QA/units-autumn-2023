import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # addition
    def test_add__positive(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add__negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add__float(self):
        self.assertAlmostEqual(self.calculator.addition(1.3, 2.1), 3.4)

    def test_add__string(self):
        self.assertEqual(self.calculator.addition('asd', 'zxc'), 'asdzxc')

    def test_add__array(self):
        self.assertEqual(self.calculator.addition([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_add__inf(self):
        self.assertEqual(self.calculator.addition(math.inf, 4), math.inf)

    def test_add__string_num(self):
        self.assertRaises(TypeError, self.calculator.addition, 'asd', 1)

    def test_add__none_num(self):
        self.assertRaises(TypeError, self.calculator.addition, None, 1)

    def test_add__array_num(self):
        self.assertRaises(TypeError, self.calculator.addition, [1, 2], 1)


    # multiplication
    def test_mult__positive(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)

    def test_mult__negative(self):
        self.assertEqual(self.calculator.multiplication(-3, 2), -6)

    def test_mult__float(self):
        self.assertAlmostEqual(self.calculator.multiplication(1.3, 2.1), 2.73)

    def test_mult__string(self):
        self.assertEqual(self.calculator.multiplication('asd', 2), 'asdasd')

    def test_mult__array(self):
        self.assertEqual(self.calculator.multiplication([1, 2], 2), [1, 2, 1, 2])

    def test_mult__inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 4), math.inf)

    def test_mult__none_num(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, 1)


    # subtraction
    def test_sub__positive(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 1)

    def test_sub__negative(self):
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)

    def test_sub__float(self):
        self.assertAlmostEqual(self.calculator.subtraction(1.3, 2.1), -0.8)

    def test_sub__string(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'asdzxc', 'zxc')

    def test_sub__array(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [1, 2], [3, 4])

    def test_sub__inf(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 4), math.inf)

    def test_sub__string_num(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'asd', 1)

    def test_sub__none_num(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, 1)

    def test_sub__array_num(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [1, 2], 1)


    # division
    def test_div__positive(self):
        self.assertEqual(self.calculator.division(6, 2), 3)

    def test_div__negative(self):
        self.assertEqual(self.calculator.division(-6, 2), -3)

    def test_div__float(self):
        self.assertAlmostEqual(self.calculator.division(6.3, 2.1), 3.0)

    def test_div__string(self):
        self.assertRaises(TypeError, self.calculator.division, 'asdzxc', 'zxc')

    def test_div__array(self):
        self.assertRaises(TypeError, self.calculator.division, [1, 2], [3, 4])

    def test_div__inf(self):
        self.assertEqual(self.calculator.division(math.inf, 4), math.inf)

    def test_div__string_num(self):
        self.assertRaises(TypeError, self.calculator.division, 'asd', 1)

    def test_div__none_num(self):
        self.assertRaises(TypeError, self.calculator.division, None, 1)

    def test_div__array_num(self):
        self.assertRaises(TypeError, self.calculator.division, [1, 2], 1)

    def test_div__by_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_div__by_inf(self):
        self.assertEqual(self.calculator.division(1, math.inf), 0)


    # adsolute
    def test_abs__positive(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_abs__negative(self):
        self.assertEqual(self.calculator.absolute(-5), 5)

    def test_abs__string(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'asd')

    def test_abs__array(self):
        self.assertRaises(TypeError, self.calculator.absolute, [1, 2, 3])

    def test_abs__none(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)

    def test_abs__inf_positive(self):
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)

    def test_abs__inf_negative(self):
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)


    # degree
    def test_deg__pos_pos(self):
        self.assertEqual(self.calculator.degree(3, 3), 27)

    def test_deg__pos_neg(self):
        self.assertEqual(self.calculator.degree(2, -2), 0.25)

    def test_deg__neg_pos(self):
        self.assertEqual(self.calculator.degree(-2, 2), 4)

    def test_deg__float_deg(self):
        self.assertEqual(self.calculator.degree(3, 3.5), 46.76537180435969)

    def test_deg__string(self):
        self.assertRaises(TypeError, self.calculator.degree, 'asd', 3.3)

    def test_deg__array(self):
        self.assertRaises(TypeError, self.calculator.degree, [1, 2], 3.3)

    def test_deg__none(self):
        self.assertRaises(TypeError, self.calculator.degree, 1, None)


    # ln
    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln__reverse(self):
        self.assertEqual(self.calculator.ln(1 / math.e), -1)

    def test_ln__neg(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln__string(self):
        self.assertRaises(TypeError, self.calculator.ln, 'asd')

    def test_ln__array(self):
        self.assertRaises(TypeError, self.calculator.ln, [1, 2])

    def test_ln__none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)


    # log
    def test_ln(self):
        self.assertEqual(self.calculator.log(8, 2), 3)

    def test_ln__reverse(self):
        self.assertAlmostEqual(self.calculator.log(2, 8), 1/3)

    def test_ln__neg(self):
        self.assertRaises(ValueError, self.calculator.log, -1, 2)

    def test_ln__string(self):
        self.assertRaises(TypeError, self.calculator.log, 'asd', 2)

    def test_ln__array(self):
        self.assertRaises(TypeError, self.calculator.log, [1, 2], 2)

    def test_ln__none(self):
        self.assertRaises(TypeError, self.calculator.log, None, 2)


    # sqrt
    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_sqrt__neg(self):
        self.assertEqual(self.calculator.sqrt(-16), 2.4492935982947064e-16+4j)

    def test_sqrt__string(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'asd')

    def test_sqrt__none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_sqrt__array(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [1, 2])



    # sqrt
    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(16, 4), 2)

    def test_nth_root__neg(self):
        self.assertEqual(self.calculator.nth_root(16, -4), 0.5)

    def test_nth_root__complex(self):
        self.assertEqual(self.calculator.nth_root(-16, 4), (1.4142135623730951+1.414213562373095j))
#
    def test_nth_root__string(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'asd', 2)

    def test_nth_root__none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, 2)

    def test_nth_root__array(self):
        self.assertRaises(TypeError, self.calculator.nth_root, [1, 2], 2)


if __name__ == "__main__":
    unittest.main()

import unittest
import math_lib as ml

class TestMathLib(unittest.TestCase):
    def test_add(self):
        self.assertEqual(ml.add(2, 3), 5)
        self.assertEqual(ml.add(-1, 1), 0)
        self.assertEqual(ml.add(0, 0), 0)
        self.assertEqual(ml.add(-5, -5), -10)
    def test_subtract(self):
        self.assertEqual(ml.sub(5, 3), 2)
        self.assertEqual(ml.sub(0, 1), -1)
        self.assertEqual(ml.sub(-1, -1), 0)
        self.assertEqual(ml.sub(-5, 5), -10)
    def test_multiply(self):
        self.assertEqual(ml.mul(2, 3), 6)
        self.assertEqual(ml.mul(-1, 1), -1)
        self.assertEqual(ml.mul(0, 5), 0)
        self.assertEqual(ml.mul(-5, -5), 25)
    def test_divide(self):
        self.assertEqual(ml.div(6, 3), 2)
        self.assertEqual(ml.div(-1, 1), -1)
        self.assertEqual(ml.div(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            ml.div(5, 0)
    def test_power(self):
        self.assertEqual(ml.pow(2, 3), 8)
        self.assertEqual(ml.pow(-1, 2), 1)
        self.assertEqual(ml.pow(5, 0), 1)
        self.assertEqual(ml.pow(-5, 3), -125)
    def test_sqrt(self):
        self.assertEqual(ml.sqrt(4), 2)
        self.assertEqual(ml.sqrt(0), 0)
        self.assertEqual(ml.sqrt(1), 1)
        with self.assertRaises(ValueError):
            ml.sqrt(-1)
    def test_root(self):
        self.assertEqual(ml.root(27, 3), 3)
        self.assertEqual(ml.root(16, 4), 2)
        self.assertEqual(ml.root(1, 5), 1)
        with self.assertRaises(ValueError):
            ml.root(-1, 2)

if __name__ == '__main__':
    unittest.main()
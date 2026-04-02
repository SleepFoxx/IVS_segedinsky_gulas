import unittest
import math_lib as ml

class TestMathLib(unittest.TestCase):
    def test_add(self):
        self.assertEqual(ml.add(2, 3), 5)
        self.assertEqual(ml.add(-1, 1), 0)
        self.assertEqual(ml.add(0, 0), 0)
        self.assertEqual(ml.add(-5, -5), -10)
        self.assertAlmostEqual(ml.add(1.5, 2.5), 4.0, places=9)
        
    def test_add_list(self):
        self.assertEqual(ml.add_list([1, 2, 3]), 6)
        self.assertEqual(ml.add_list([-1, 1, 0]), 0)
        self.assertEqual(ml.add_list([0, 0, 0]), 0)
        with self.assertRaises(ValueError):
            ml.add_list([])
        with self.assertRaises(ValueError):
            ml.add_list([1, 'a', 3])
        
    def test_subtract(self):
        self.assertEqual(ml.sub(5, 3), 2)
        self.assertEqual(ml.sub(0, 1), -1)
        self.assertEqual(ml.sub(-1, -1), 0)
        self.assertEqual(ml.sub(-5, 5), -10)
        self.assertAlmostEqual(ml.sub(2.5, 1.5), 1.0, places=9)
    
    def test_sub_list(self):
        self.assertEqual(ml.sub_list([10, 2, 3]), 5)
        self.assertEqual(ml.sub_list([-1, 1, 0]), -2)
        self.assertEqual(ml.sub_list([0, 0, 0]), 0)
        with self.assertRaises(ValueError):
            ml.sub_list([])
        with self.assertRaises(ValueError):
            ml.sub_list([1, 'a', 3])
        
    def test_multiply(self):
        self.assertEqual(ml.mul(2, 3), 6)
        self.assertEqual(ml.mul(-1, 1), -1)
        self.assertEqual(ml.mul(0, 5), 0)
        self.assertEqual(ml.mul(-5, -5), 25)
        self.assertAlmostEqual(ml.mul(1.5, 2.5), 3.75 , places=9)

    def test_mul_list(self):
        self.assertEqual(ml.mul_list([1, 2, 3]), 6)
        self.assertEqual(ml.mul_list([-1, 1, 0]), 0)
        self.assertEqual(ml.mul_list([1, 1, 1]), 1)
        with self.assertRaises(ValueError):
            ml.mul_list([])
        with self.assertRaises(ValueError):
            ml.mul_list([1, 'a', 3])
    
    def test_divide(self):
        self.assertEqual(ml.div(6, 3), 2)
        self.assertEqual(ml.div(-1, 1), -1)
        self.assertEqual(ml.div(5, 2), 2.5)
        self.assertEqual(ml.div(0, 5), 0)
        self.assertEqual(ml.div(-5, -5), 1)
        self.assertAlmostEqual(ml.div(1,3), 0.333333333, places=9)
        with self.assertRaises(ZeroDivisionError):
            ml.div(5, 0)
            
    def test_power(self):
        self.assertEqual(ml.pow(2, 3), 8)
        self.assertEqual(ml.pow(-1, 2), 1)
        self.assertEqual(ml.pow(5, 0), 1)
        self.assertEqual(ml.pow(400, 0), 1)
        self.assertEqual(ml.pow(0, 5), 0)
        self.assertEqual(ml.pow(-2, 3), -8)
        self.assertEqual(ml.pow(-5, 3), -125)
        self.assertAlmostEqual(ml.pow(2, -1), 0.5, places=9)
        self.assertAlmostEqual(ml.pow(4, 0.5), 2.0, places=9)
        
    def test_sqrt(self):
        self.assertEqual(ml.sqrt(4), 2)
        self.assertEqual(ml.sqrt(0), 0)
        self.assertEqual(ml.sqrt(1), 1)
        self.assertAlmostEqual(ml.sqrt(2), 1.414213562, places=9)
        with self.assertRaises(ValueError):
            ml.sqrt(-1)
        with self.assertRaises(ValueError):
            ml.sqrt(-0.5)
            
    def test_root(self):
        self.assertEqual(ml.root(27, 3), 3)
        self.assertEqual(ml.root(16, 4), 2)
        self.assertEqual(ml.root(1, 5), 1)
        self.assertAlmostEqual(ml.root(2, 2), 1.414213562, places=9)
        with self.assertRaises(ValueError):
            ml.root(-1, 2)
        with self.assertRaises(ValueError):
            ml.root(8, 0)
            
    def test_factorial(self):
        self.assertEqual(ml.factorial(0), 1)
        self.assertEqual(ml.factorial(1), 1)
        self.assertEqual(ml.factorial(5), 120)
        self.assertEqual(ml.factorial(10), 3628800)
        with self.assertRaises(ValueError):
            ml.factorial(-1)
        with self.assertRaises(ValueError):
            ml.factorial(3.5)
            
    def test_abs(self):
        self.assertEqual(ml.abs(-5), 5)
        self.assertEqual(ml.abs(5), 5)
        self.assertEqual(ml.abs(0), 0)
        self.assertEqual(ml.abs(-3.5), 3.5)
        self.assertEqual(ml.abs(2.5), 2.5)
        
    def test_percent(self):
        self.assertEqual(ml.percent(50, 200), 25)
        self.assertEqual(ml.percent(25, 100), 25)
        self.assertEqual(ml.percent(0, 100), 0)
        self.assertEqual(ml.percent(100, 100), 100)
        with self.assertRaises(ValueError):
            ml.percent(50, 0)
            
    def test_negate(self):
        self.assertEqual(ml.negate(5), -5)
        self.assertEqual(ml.negate(-5), 5)
        self.assertEqual(ml.negate(0), 0)
        self.assertEqual(ml.negate(3.5), -3.5)
        self.assertEqual(ml.negate(-2.5), 2.5)

if __name__ == '__main__':
    unittest.main()
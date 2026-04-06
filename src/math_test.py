"""
@file test_math_lib.py
@author Ronnie Rybarik (xrybarr00)
@brief Unit tests for the math_lib library.
@details This file contains unit tests for all functions in math_lib.py. Tests cover standard inputs, edge cases (zero, negative numbers, floats), invalid value inputs (ValueError, ZeroDivisionError) and invalid type inputs (TypeError). All trigonometric functions expect and return values in degrees.
@version 0.3
@date 2026-04-03
 
@section LICENSE
This software is licensed under the GNU GPL v3 license.
"""






import unittest
import math_lib as ml

class TestMathLib(unittest.TestCase):
    """
    @brief Test class for math_lib.py.
 
    Contains unit tests for all functions defined in math_lib. Each function
    has a corresponding test method for standard behavior and a separate test
    method for invalid type inputs.
    """
    
    def test_add(self):
        """
        @brief Tests the add function.
 
        Verifies correct addition of positive, negative, zero and float values.
        Also checks that passing a non-numeric argument raises TypeError.
        """
        self.assertEqual(ml.add(2, 3), 5)
        self.assertEqual(ml.add(-1, 1), 0)
        self.assertEqual(ml.add(0, 0), 0)
        self.assertEqual(ml.add(-5, -5), -10)
        self.assertAlmostEqual(ml.add(1.5, 2.5), 4.0, places=9)
        with self.assertRaises(TypeError):
            ml.add(1, 'a')
        with self.assertRaises(TypeError):
            ml.add('b', 1)
        with self.assertRaises(TypeError):
            ml.add('a', 'b')
        
    def test_add_list(self):
        """
        @brief Tests the add_list function.
 
        Verifies correct summation of a list of numbers including floats.
        Also checks that an empty list raises ValueError and a non-numeric
        element raises TypeError.
        """
        self.assertEqual(ml.add_list([1, 2, 3]), 6)
        self.assertEqual(ml.add_list([-1, 1, 0]), 0)
        self.assertEqual(ml.add_list([0, 0, 0]), 0)
        self.assertAlmostEqual(ml.add_list([1.5, 2.5, 0.5]), 4.5, places=9)
        with self.assertRaises(ValueError):
            ml.add_list([])
        with self.assertRaises(TypeError):
            ml.add_list([1, 'a', 3])
        
    def test_subtract(self):
        """
        @brief Tests the sub function.
 
        Verifies correct subtraction of positive, negative, zero and float values.
        Also checks that passing a non-numeric argument raises TypeError.
        """
        self.assertEqual(ml.sub(5, 3), 2)
        self.assertEqual(ml.sub(0, 1), -1)
        self.assertEqual(ml.sub(-1, -1), 0)
        self.assertEqual(ml.sub(-5, 5), -10)
        self.assertAlmostEqual(ml.sub(2.5, 1.5), 1.0, places=9)
        with self.assertRaises(TypeError):
            ml.sub(1, 'a')
        with self.assertRaises(TypeError):
            ml.sub('b', 1)
        with self.assertRaises(TypeError):
            ml.sub('a', 'b')
    
    def test_sub_list(self):
        """
        @brief Tests the sub_list function.
 
        Verifies correct sequential subtraction of a list of numbers including floats.
        Also checks that an empty list raises ValueError and a non-numeric
        element raises TypeError.
        """
        self.assertEqual(ml.sub_list([10, 2, 3]), 5)
        self.assertEqual(ml.sub_list([-1, 1, 0]), -2)
        self.assertEqual(ml.sub_list([0, 0, 0]), 0)
        self.assertAlmostEqual(ml.sub_list([2.5, 1.5, 0.5]), 0.5, places=9)
        with self.assertRaises(ValueError):
            ml.sub_list([])
        with self.assertRaises(TypeError):
            ml.sub_list([1, 'a', 3])
        
    def test_multiply(self):
        """
        @brief Tests the mul function.
 
        Verifies correct multiplication of positive, negative, zero and float values.
        Also checks that passing a non-numeric argument raises TypeError.
        """
        self.assertEqual(ml.mul(2, 3), 6)
        self.assertEqual(ml.mul(-1, 1), -1)
        self.assertEqual(ml.mul(0, 5), 0)
        self.assertEqual(ml.mul(-5, -5), 25)
        self.assertAlmostEqual(ml.mul(1.5, 2.5), 3.75 , places=9)
        with self.assertRaises(TypeError):
            ml.mul(1, 'a')
        with self.assertRaises(TypeError):
            ml.mul('b', 1)
        with self.assertRaises(TypeError):
            ml.mul('a', 'b')

    def test_mul_list(self):
        """
        @brief Tests the mul_list function.
 
        Verifies correct sequential multiplication of a list of numbers including floats
        and sign combinations. Also checks that an empty list raises ValueError and
        a non-numeric element raises TypeError.
        """
        self.assertEqual(ml.mul_list([1, 2, 3]), 6)
        self.assertEqual(ml.mul_list([-1, 1, 0]), 0)
        self.assertEqual(ml.mul_list([1, 1, 1]), 1)
        self.assertEqual(ml.mul_list([-1, -1, -1]), -1)
        self.assertAlmostEqual(ml.mul_list([1.5, 2.5, 0.5]), 1.875, places=9)
        with self.assertRaises(ValueError):
            ml.mul_list([])
        with self.assertRaises(TypeError):
            ml.mul_list([1, 'a', 3])
    
    def test_divide(self):
        """
        @brief Tests the div function.
 
        Verifies correct division of positive, negative, zero and float values.
        Also checks that dividing by zero raises ZeroDivisionError and that
        passing a non-numeric argument raises TypeError.
        """
        self.assertEqual(ml.div(6, 3), 2)
        self.assertEqual(ml.div(-1, 1), -1)
        self.assertEqual(ml.div(5, 2), 2.5)
        self.assertEqual(ml.div(0, 5), 0)
        self.assertEqual(ml.div(-5, -5), 1)
        self.assertAlmostEqual(ml.div(1,3), 0.333333333, places=9)
        with self.assertRaises(ZeroDivisionError):
            ml.div(5, 0)
        with self.assertRaises(TypeError):
            ml.div(1, 'a')
        with self.assertRaises(TypeError):
            ml.div('b', 1)
        with self.assertRaises(TypeError):
            ml.div('a', 'b')
            
    def test_power(self):
        """
        @brief Tests the pow function.
 
        Verifies correct exponentiation where the exponent is a natural number
        (0, 1, 2, ...) as specified by the assignment. Checks that negative or
        non-integer exponents raise ValueError and that passing a non-numeric
        argument raises TypeError.
        """
        self.assertEqual(ml.pow(2, 3), 8)
        self.assertEqual(ml.pow(-1, 2), 1)
        #self.assertEqual(ml.pow(5, 0), 1)
        #self.assertEqual(ml.pow(400, 0), 1)
        self.assertEqual(ml.pow(0, 5), 0)
        self.assertEqual(ml.pow(-2, 3), -8)
        self.assertEqual(ml.pow(-5, 3), -125)
        with self.assertRaises(ValueError):
            ml.pow(2, -1)
        with self.assertRaises(ValueError):
            ml.pow(2, -0.5)
        with self.assertRaises(ValueError):
            ml.pow(4, 0.5)
        with self.assertRaises(TypeError):
            ml.pow(1, 'a')
        with self.assertRaises(TypeError):
            ml.pow('b', 1)
        with self.assertRaises(TypeError):
            ml.pow('a', 'b')
        
        
    def test_sqrt(self):
        """
        @brief Tests the sqrt function.
 
        Verifies correct square root computation including irrational results.
        Also checks that a negative input raises ValueError and that passing
        a non-numeric argument raises TypeError.
        """
        self.assertEqual(ml.sqrt(4), 2)
        self.assertEqual(ml.sqrt(0), 0)
        self.assertEqual(ml.sqrt(1), 1)
        self.assertAlmostEqual(ml.sqrt(2), 1.414213562, places=9)
        with self.assertRaises(ValueError):
            ml.sqrt(-1)
        with self.assertRaises(ValueError):
            ml.sqrt(-0.5)
        with self.assertRaises(TypeError):
            ml.sqrt('a')
            
    def test_root(self):
        """
        @brief Tests the root function.
 
        Verifies correct nth root computation. Also checks that taking an even
        root of a negative number raises ValueError, that a zero degree raises
        ValueError as it is undefined, and that passing a non-numeric argument
        raises TypeError.
        """
        self.assertAlmostEqual(ml.root(27, 3), 3, places=9)
        self.assertAlmostEqual(ml.root(16, 4), 2, places=9)
        self.assertAlmostEqual(ml.root(1, 5), 1, places=9)
        self.assertAlmostEqual(ml.root(2, 2), 1.414213562, places=9)
        with self.assertRaises(ValueError):
            ml.root(-1, 2)
        with self.assertRaises(ValueError):
            ml.root(8, 0)
        with self.assertRaises(TypeError):
            ml.root(1, 'a')
        with self.assertRaises(TypeError):
            ml.root('b', 1)
        with self.assertRaises(TypeError):
            ml.root('a', 'b')
            
    def test_factorial(self):
        """
        @brief Tests the factorial function.
 
        Verifies correct factorial computation for standard values including 0! = 1.
        Also checks that a negative integer raises ValueError, a float raises
        ValueError, and that passing a non-numeric argument raises TypeError.
        """
        self.assertEqual(ml.factorial(0), 1)
        self.assertEqual(ml.factorial(1), 1)
        self.assertEqual(ml.factorial(5), 120)
        self.assertEqual(ml.factorial(10), 3628800)
        with self.assertRaises(ValueError):
            ml.factorial(-1)
        with self.assertRaises(ValueError):
            ml.factorial(3.5)
        with self.assertRaises(TypeError):
            ml.factorial('a')
        
            
    def test_abs(self):
        """
        @brief Tests the abs function.
 
        Verifies correct absolute value computation for positive, negative, zero
        and float values. Also checks that passing a non-numeric argument raises TypeError.
        """
        self.assertEqual(ml.abs(-5), 5)
        self.assertEqual(ml.abs(5), 5)
        self.assertEqual(ml.abs(0), 0)
        self.assertEqual(ml.abs(-3.5), 3.5)
        self.assertEqual(ml.abs(2.5), 2.5)
        with self.assertRaises(TypeError):
            ml.abs('a')
        
        
    def test_percent(self):
        """
        @brief Tests the percent function.
 
        Verifies correct percentage computation using the formula x * p / 100,
        where x is the base number and p is the percentage value. Also checks
        that passing a non-numeric argument raises TypeError.
        """
        self.assertEqual(ml.percent(50, 200), 100)
        self.assertEqual(ml.percent(25, 100), 25)
        self.assertEqual(ml.percent(0, 100), 0)
        self.assertEqual(ml.percent(100, 100), 100)
        self.assertAlmostEqual(ml.percent(33.3333, 100), 33.3333, places=9)
        self.assertAlmostEqual(ml.percent(33,200), 66.0, places=9)
        #with self.assertRaises(ValueError):
            #ml.percent(50, 0)
        with self.assertRaises(TypeError):
            ml.percent('a', 100)
        with self.assertRaises(TypeError):
            ml.percent(50, 'b')
        with self.assertRaises(TypeError):
            ml.percent('a', 'b')
            
    def test_negate(self):
        """
        @brief Tests the negate function.
 
        Verifies correct sign toggling for positive, negative, zero and float values.
        Also checks that passing a non-numeric argument raises TypeError.
        """
        self.assertEqual(ml.negate(5), -5)
        self.assertEqual(ml.negate(-5), 5)
        self.assertEqual(ml.negate(0), 0)
        self.assertEqual(ml.negate(3.5), -3.5)
        self.assertEqual(ml.negate(-2.5), 2.5)
        with self.assertRaises(TypeError):
            ml.negate('a')
        
            
    def test_sin(self):
        """
        @brief Tests the sin function.
 
        Verifies correct sine computation for standard angles in degrees including
        quadrant boundaries and a negative angle. Also checks that passing a
        non-numeric argument raises TypeError.
        """
        self.assertAlmostEqual(ml.sin(0), 0.0, places=9)
        self.assertAlmostEqual(ml.sin(30), 0.5, places=9)
        self.assertAlmostEqual(ml.sin(45), 0.707106781, places=9)
        self.assertAlmostEqual(ml.sin(60), 0.86602540378, places=9)
        self.assertAlmostEqual(ml.sin(90), 1.0, places=9)
        self.assertAlmostEqual(ml.sin(180), 0.0, places=9)
        self.assertAlmostEqual(ml.sin(270), -1.0, places=9)
        self.assertAlmostEqual(ml.sin(360), 0.0, places=9)
        self.assertAlmostEqual(ml.sin(-30), -0.5, places=9)
        with self.assertRaises(TypeError):
            ml.sin('a')
        
            
    def test_cos(self):
        """
        @brief Tests the cos function.
 
        Verifies correct cosine computation for standard angles in degrees including
        quadrant boundaries and a negative angle. Also checks that passing a
        non-numeric argument raises TypeError.
        """
        self.assertAlmostEqual(ml.cos(0), 1.0, places=9)
        self.assertAlmostEqual(ml.cos(30), 0.86602540378, places=9)
        self.assertAlmostEqual(ml.cos(45), 0.707106781, places=9)
        self.assertAlmostEqual(ml.cos(60), 0.5, places=9)
        self.assertAlmostEqual(ml.cos(90), 0.0, places=9)
        self.assertAlmostEqual(ml.cos(180), -1.0, places=9)
        self.assertAlmostEqual(ml.cos(270), 0.0, places=9)
        self.assertAlmostEqual(ml.cos(360), 1.0, places=9)
        self.assertAlmostEqual(ml.cos(-30), 0.866025404, places=9)
        with self.assertRaises(TypeError):
            ml.cos('a')
        
            
    def test_tg(self):
        """
        @brief Tests the tg function.
 
        Verifies correct tangent computation for standard angles in degrees.
        Also checks that undefined values at 90° and 270° raise ValueError
        and that passing a non-numeric argument raises TypeError.
        """
        self.assertAlmostEqual(ml.tg(0), 0.0, places=9)
        self.assertAlmostEqual(ml.tg(30), 0.577350269, places=9)
        self.assertAlmostEqual(ml.tg(45), 1.0, places=9)
        self.assertAlmostEqual(ml.tg(60), 1.732050808, places=9)
        self.assertAlmostEqual(ml.tg(180), 0.0, places=5)
        self.assertAlmostEqual(ml.tg(360), 0.0, places=5)
        self.assertAlmostEqual(ml.tg(-30), -0.577350269, places=9)
        with self.assertRaises(ValueError):
            ml.tg(90)
        with self.assertRaises(ValueError):
            ml.tg(270)
        with self.assertRaises(TypeError):
            ml.tg('a')
        
            
    def test_arcsin(self):
        """
        @brief Tests the arcsin function.
 
        Verifies correct arcsine computation with output in degrees in the range
        [-90, 90]. Also checks that inputs outside the domain [-1, 1] raise
        ValueError and that passing a non-numeric argument raises TypeError.
        """
        self.assertAlmostEqual(ml.arcsin(0), 0.0, places=9)
        self.assertAlmostEqual(ml.arcsin(0.5), 30.0, places=9)
        self.assertAlmostEqual(ml.arcsin(0.707106781), 45.0, places=9)
        self.assertAlmostEqual(ml.arcsin(0.866025403), 60.0, places=9)
        self.assertAlmostEqual(ml.arcsin(1), 90.0, places=9)
        self.assertAlmostEqual(ml.arcsin(-0.5), -30.0, places=9)
        with self.assertRaises(ValueError):
            ml.arcsin(2)
        with self.assertRaises(ValueError):
            ml.arcsin(-2)
        with self.assertRaises(TypeError):
            ml.arcsin('a')
        
            
    def test_arccos(self):
        """
        @brief Tests the arccos function.
 
        Verifies correct arccosine computation with output in degrees in the range
        [0, 180]. Also checks that inputs outside the domain [-1, 1] raise
        ValueError and that passing a non-numeric argument raises TypeError.
        """
        self.assertAlmostEqual(ml.arccos(1), 0.0, places=9)
        self.assertAlmostEqual(ml.arccos(0.866025403), 30.0, places=9)
        self.assertAlmostEqual(ml.arccos(0.707106781), 45.0, places=9)
        self.assertAlmostEqual(ml.arccos(0.5), 60.0, places=9)
        self.assertAlmostEqual(ml.arccos(0), 90.0, places=9)
        self.assertAlmostEqual(ml.arccos(-1), 180.0, places=9)
        with self.assertRaises(ValueError):
            ml.arccos(2)
        with self.assertRaises(ValueError):
            ml.arccos(-2)
        with self.assertRaises(TypeError):
            ml.arccos('a')
        
            
    def test_arctg(self):
        """
        @brief Tests the arctg function.
 
        Verifies correct arctangent computation with output in degrees in the range
        (-90, 90). The domain is all real numbers so no ValueError is expected.
        Also checks that passing a non-numeric argument raises TypeError.
        """
        self.assertAlmostEqual(ml.arctg(0), 0.0, places=9)
        self.assertAlmostEqual(ml.arctg(0.577350269), 30.0, places=9)
        self.assertAlmostEqual(ml.arctg(1), 45.0, places=9)
        self.assertAlmostEqual(ml.arctg(1.732050808), 60.0, places=9)
        self.assertAlmostEqual(ml.arctg(-0.577350269), -30.0, places=9)
        with self.assertRaises(TypeError):
            ml.arctg('a')
        

if __name__ == '__main__':
    unittest.main()

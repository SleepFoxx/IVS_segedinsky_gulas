"""
@file math_lib.py
@author Jakub Hulín (xhulinj00)
@brief A simple math library that provides basic arithmetic operations.
@details This library includes functions for addition, subtraction, multiplication, division, exponentiation, square root and nth root. It can handle integers, floats, negative numbers... The functions are designed to be simple and easy to use, with error handling for invalid inputs.
@version 0.5
@date 2026-04-09

@section LICENSE
This software is licensed under the GNU GPL v3 license.
"""

pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679



def add(a: int | float, b: int | float) -> int | float:
    """
    @brief Adds two numbers together.

    This function takes two numbers, no matter their type and returns their sum. It can handle integers, floats, negative numbers...

    @param a First number
    @param b Second number
    @return The sum of a and b
    """
    if not type(a) in (int, float) or not type(b) in (int, float):
        raise TypeError("Both a and b must be numbers")
    return a + b


def add_list(numbers: list[int | float]) -> int | float:
    """
    @brief Adds a list of numbers together

    This function takes a list of numbers and returns their sum. It can handle integers, floats, negative numbers... The list cannot be empty and all elements must be numbers.
    @param numbers List of numbers to add
    @return The sum of all numbers in the list
    """
    total = 0
    if not numbers:
        raise ValueError("The list cannot be empty")
    for num in numbers:
        if not type(num) in (int, float):
            raise TypeError("All elements must be numbers")
        total += num
    return total
def sub(a: int | float, b: int | float) -> int | float:
    """
    @brief Subtracts two numbers.
    This function takes two numbers, no matter their type and returns their difference. It can handle integers, floats, negative numbers...
    @param a First number
    @param b Second number
    @return The difference of a and b
    """
    if not type(a) in (int, float) or not type(b) in (int, float):
        raise TypeError("Both a and b must be numbers")
    return a - b
    
    
def sub_list(numbers: list[int | float]) -> int | float:
    """
    @brief Subtracts a list of numbers together
    This function takes a list of numbers and returns their difference. It can handle integers, floats, negative numbers... The list cannot be empty and all elements must be numbers.
    @param numbers List of numbers to subtract
    @return The difference of all numbers in the list
    """
    if not numbers:
        raise ValueError("The list cannot be empty")
    total = numbers[0]
    for num in numbers[1:]:
        if not type(num) in (int, float):
            raise TypeError("All elements must be numbers")
        total -= num
    return total

def mul(a: int | float, b: int | float) -> int | float:
    """
    @brief Multiplies two numbers together.
    This function takes two numbers, no matter their type and returns their product. It can handle integers, floats, negative numbers...
    @param a First number
    @param b Second number
    @return The product of a and b
    """
    if not type(a) in (int, float) or not type(b) in (int, float):
        raise TypeError("Both a and b must be numbers")
    return a * b
    

def mul_list(numbers: list[int | float]) -> int | float:
    """
    @brief Multiplies a list of numbers together
    This function takes a list of numbers and returns their product. It can handle integers, floats, negative numbers... The list cannot be empty and all elements must be numbers.
    @param numbers List of numbers to multiply
    @return The product of all numbers in the list
    """
    if not numbers:
        raise ValueError("The list cannot be empty")
    total = numbers[0]
    for num in numbers[1:]:
        if not type(num) in (int, float):
            raise TypeError("All elements must be numbers")
        total *= num
    return total

def div(a: int | float, b: int | float) -> int | float:
    """
    @brief Divides two numbers.
    This function takes two numbers, no matter their type and returns their quotient. It can handle integers, floats, negative numbers... The second number cannot be zero.
    @param a First number
    @param b Second number, cannot be zero
    @return The quotient of a and b
    """
    if not type(a) in (int, float) or not type(b) in (int, float):
        raise TypeError("Both a and b must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
    




def pow(a: int | float, b: int) -> int:
    """
    @brief Raises a number to a power.
    This function takes a number and an integer exponent and returns the result of raising the number to that exponent. It can handle integers, floats, negative numbers... The exponent must be an integer.
    @param a The base number
    @param b The exponent, must be a positive integer
    @return The result of a raised to the power of b
    """

    if type(b) is not int or type(a) not in (int, float):
        raise TypeError("a must be a number and b must be an integer")

    if(b <= 0):
        if b < 0:
            raise ValueError("b must be a positive integer")
        raise ValueError("b must not be zero")
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result
    

def sqrt(a: int | float) -> int | float:
    """
    @brief Takes the square root of a number.
    This function takes a number and returns its square root. It can handle integers, floats... The number must be non-negative.
    @param a The number to take the square root of, must be non-negative
    @return The square root of a
    """
    if not type(a) in (int, float):
        raise TypeError("a must be a number")
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    if a == 0 or a == 1:
        return a
    
    guess = a / 2 if a > 1.0 else 1.0

    while True:
        next_guess = 0.5 * (guess + a / guess)
        diff = guess - next_guess
        if(diff if diff > 0 else -diff) < 1e-10:
            return next_guess
        guess = next_guess
    
def root(a: int | float, n: int) -> int | float:
    """
    @brief Takes the nth root of a number with Newton's approximation method.
    This function takes a number and an integer n and returns the nth root of that number. It can handle integers, floats... The number must be non-negative if n is even.
    @param a The number to take the nth root of, must be non-negative if n is even
    @param n The degree of the root, must be a positive integer
    @return The nth root of a
    """
    if not type(n) is int or type(a) not in (int, float):
        raise TypeError("a must be a number and n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if a < 0 and n % 2 == 0:
        raise ValueError("Cannot take even root of a negative number")
    if a == 0:
        return 0
    if a == 1:
        return 1
    
    is_negative = False
    if a < 0:
        is_negative = True
        a = -a
    guess = a / n if a > 1.0 else 1.0

    while True:
        guess_pow_minus_1 = pow(guess, n-1)
        next_guess = ((n-1) * guess + a / guess_pow_minus_1) / n
        diff = guess - next_guess
        if(diff if diff > 0 else -diff) < 1e-10:
            break
        guess = next_guess
    return -guess if is_negative else guess

        

def factorial(a: int) -> int:
    """
    @brief Takes the factorial of a number.
    This function takes a non-negative integer and returns its factorial. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It can handle integers... The number must be a non-negative integer.
    @param a The number to take the factorial of, must be a non-negative integer
    @return The factorial of a
    """
    if type(a) is float:
        raise ValueError("a must be an integer")
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if a < 0:
        raise ValueError("Cannot take factorial of a negative number")
    if a == 0 or a == 1:
        return 1
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result

def abs(a: int | float) -> int | float:
    """
    @brief Takes the absolute value of a number.
    This function takes a number and returns its absolute value. It can handle integers, floats... The absolute value of a number is the non-negative value of that number without regard to its sign.
    @param a The number to take the absolute value of
    @return The absolute value of a
    """
    if not type(a) in (int, float):
        raise TypeError("a must be a number")
    return a if a >= 0 else -a

def negate(a: int | float) -> int | float:
    """
    @brief Negates a number.
    This function takes a number and returns its negation. It can handle integers, floats... The negation of a number is the number with the opposite sign.
    @param a The number to negate
    @return The negation of a
    """
    if not type(a) in (int, float):
        raise TypeError("a must be a number")
    return -a


def percent(a: int | float, b: int | float) -> int | float:
    """
    @brief Calculates the percentage of a number.
    This function takes two numbers and returns the percentage of the first number that the second number represents. It can handle integers, floats... The second number cannot be zero.
    @param a Percentage to calculate
    @param b The number to calculate the percentage of
    @return The percentage of b that a represents
    """
    
    if not type(a) in (int, float) or not type(b) in (int, float):
        raise TypeError("Both a and b must be numbers")
    return (b / 100) * a

def sin(a: int | float) -> float:
    """
    @brief Calculates the sine of an angle in degrees.
    This function takes an angle in degrees and returns its sine. It can handle integers, floats... The sine of an angle is a trigonometric function that gives the ratio of the length of the side opposite the angle to the length of the hypotenuse in a right triangle.
    @param a The angle in degrees to calculate the sine of
    @return The sine of the angle
    """

    a_rad = mul(a, div(pi, 180))
    
    if not type(a) in (int, float):
        raise TypeError("a must be a number")
    a_rad = a_rad % (mul(2, pi))

    term = a_rad
    sin_a = a_rad
    for i in range(1, 15):
        term *= div(mul(-1, mul(a_rad, a_rad)), mul(mul(2, i), add(mul(2, i), 1)))
        sin_a += term
    return float(sin_a)


def cos(a: int | float) -> float:
    """
    @brief Calculates the cosine of an angle in degrees.
    This function takes an angle in degrees and returns its cosine. It can handle integers, floats... The cosine of an angle is a trigonometric function that gives the ratio of the length of the adjacent side to the length of the hypotenuse in a right triangle.
    @param a The angle in degrees to calculate the cosine of
    @return The cosine of the angle
    """

    if not type(a) in (int, float):
        raise TypeError("a must be a number")
        
    a_rad = mul(a, div(pi, 180))
    a_rad = a_rad % (mul(2, pi))

    term = 1
    cos_a = 1
    for i in range(1, 15):
        numer = mul(-1, mul(a_rad, a_rad))
        denom = mul(sub(mul(2, i), 1), mul(2, i))
        term *= div(numer, denom)

        cos_a += term
    return float(cos_a)


def tg(a: int | float) -> float:
    """
    @brief Calculates the tangent of an angle in degrees.
    This function takes an angle in degrees and returns its tangent. It can handle integers, floats... The tangent of an angle is a trigonometric function that gives the ratio of the sine of the angle to the cosine of the angle.
    @param a The angle in degrees to calculate the tangent of
    @return The tangent of the angle
    """

    if not type(a) in (int, float):
        raise TypeError("a must be a number")
    epsilon = 1e-10
    cos_a = cos(a)
    if abs(cos_a) < epsilon:
        raise ValueError("Tangent is undefined for this angle")
    return div(sin(a), cos_a)

def arctg(a: int | float, is_recursive = False) -> float:
    """
    @brief Calculates the arctangent of a number in degrees using the Taylor series expansion.
    This function takes a number and returns its arctangent in degrees. It can handle integers, floats... The arctangent of a number is the angle whose tangent is that number. The range of the arctangent function is from -90 to 90 degrees.
    @param a The number to calculate the arctangent of
    @return The arctangent of the number in degrees
    """
    if not type(a) in (int, float):
        raise TypeError("a must be a number")
    
    if a == 0:
        return 0.0
        
    if abs(a - 1.0) < 1e-12:
        return 45.0 if not is_recursive else div(pi, 4)

    if abs(a + 1.0) < 1e-12:
        return -45.0 if not is_recursive else div(-pi, 4)
    

    if(abs(a) > 0.5):
        new_a = div(a, add(1, sqrt(add(1, mul(a, a)))))
        res_rad = mul(2, arctg(new_a, is_recursive = True))
    else:
        result = a
        term = a
        a_squared = mul(a, a)

        for i in range(1, 500):
            term *= a_squared
            denom = add(1, mul(2, i))
            current_term = div(term, denom)

            if i % 2 == 1:
                result -= current_term
            else:
                result += current_term
        res_rad = result

    if(is_recursive):
        return res_rad
    else:
        return(mul(res_rad, div(180, pi)))

def arcsin(a: int | float) -> float:
    """
    @brief Calculates the arcsine of a number in degrees.
    This function takes a number and returns its arcsine in degrees. It can handle integers, floats... The arcsine of a number is the angle whose sine is that number. The range of the arcsine function is from -90 to 90 degrees. The input must be in the range from -1 to 1, inclusive.
    Using Taylor series expansion for arcsin is not efficient for values close to 1 or -1, so we will use the identity arcsin(x) = arctg(x / sqrt(1 - x^2)) to calculate the arcsine for those values.
    @param a The number to calculate the arcsine of, must be in the range from -1 to 1, inclusive
    @return The arcsine of the number in degrees
    """
    if not type(a) in (int, float):
        raise TypeError("a must be a number")

    if a < -1 or a > 1:
        raise ValueError("arcsin is undefined for this value")

    if a == 0:
        return 0.0

    if a == 1:
        return 90.0

    if a == -1:
        return -90.0

    numerator = a
    denominator = sqrt(sub(1, pow(a, 2)))
    ratio = div(numerator, denominator)

    if abs(ratio-1.0) < 1e-12:
        ratio = 1.0

    if abs(ratio+1.0) < 1e-12:
        ratio = -1.0

    return arctg(ratio)


def arccos(a: int | float) -> float:
    """
    @brief Calculates the arccosine of a number in degrees.
    This function takes a number and returns its arccosine in degrees. It can handle integers, floats... The arccosine of a number is the angle whose cosine is that number. The range of the arccosine function is from 0 to 180 degrees. The input must be in the range from -1 to 1, inclusive. We will use the identity arccos(x) = 90 - arcsin(x) to calculate the arccosine.
    From the identity arccos(x) = 90 - arcsin(x) we can see that arccos(0) = 90, arccos(1) = 0 and arccos(-1) = 180, so we can handle those cases separately to avoid unnecessary calculations.
    @param a The number to calculate the arccosine of, must be in the range from -1 to 1, inclusive
    @return The arccosine of the number in degrees
    """
    if not type(a) in (int, float):
        raise TypeError("a must be a number")

    if a < -1 or a > 1:
        raise ValueError("arccos is undefined for this value")

    if a == 0:
        return 90.0

    if a == 1:
        return 0.0

    if a == -1:
        return 180.0
    
    return sub(90.0, arcsin(a))

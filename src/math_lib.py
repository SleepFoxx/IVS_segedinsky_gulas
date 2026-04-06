"""
@file math_lib.py
@author Jakub Hulín (xhulinj00)
@brief A simple math library that provides basic arithmetic operations.
@details This library includes functions for addition, subtraction, multiplication, division, exponentiation, square root and nth root. It can handle integers, floats, negative numbers... The functions are designed to be simple and easy to use, with error handling for invalid inputs.
@version 0.4
@date 2026-04-03

@section LICENSE
This software is licensed under the GNU GPL v3 license.
"""






def add(a: int | float, b: int | float) -> int | float:
    """
    @brief Adds two numbers together.

    This function takes two numbers, no matter their type and returns their sum. It can handle integers, floats, negative numbers...

    @param a First number
    @param b Second number
    @return The sum of a and b
    """
    try:
        a = float(a)
        b = float(b)
        return a + b
    except (TypeError, ValueError):
        raise TypeError("Both a and b must be numbers")


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
        #if not isinstance(num, (int, float)):
            #raise TypeError("All elements must be numbers")
        try:
            num = float(num)
        except (TypeError, ValueError):
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
    try:
        a = float(a)
        b = float(b)
        return a - b
    except (TypeError, ValueError):
        raise TypeError("Both a and b must be numbers")
    
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
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be a number")
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
    try:
        a = float(a)
        b = float(b)
        return a * b
    except (TypeError, ValueError):
        raise TypeError("Both a and b must be numbers")

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
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be a number")
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
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    except (TypeError, ValueError):
        raise TypeError("Both a and b must be numbers")




def pow(a: int | float, b: int) -> int:
    """
    @brief Raises a number to a power.
    This function takes a number and an integer exponent and returns the result of raising the number to that exponent. It can handle integers, floats, negative numbers... The exponent must be an integer.
    @param a The base number
    @param b The exponent, must be a positive integer
    @return The result of a raised to the power of b
    """
    if not isinstance(b, int | float):
        raise TypeError("b must be numeric")
    if isinstance(b, float):
        raise ValueError("b must be an integer")
    try:
        a = float(a)
        b = int(b)
    except (TypeError, ValueError):
        raise TypeError("a must be a number and b must be an integer")
    if(b < 0):
        raise ValueError("Exponent must be a positive integer")
    if (b == 0):
        return 1
    result = a
    for i in range(1, b):
        result *= a
    return result
    

def sqrt(a: int | float) -> int | float:
    """
    @brief Takes the square root of a number.
    This function takes a number and returns its square root. It can handle integers, floats... The number must be non-negative.
    @param a The number to take the square root of, must be non-negative
    @return The square root of a
    """
    if not isinstance(a, (int, float)):
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
    @brief Takes the nth root of a number.
    This function takes a number and an integer n and returns the nth root of that number. It can handle integers, floats... The number must be non-negative if n is even.
    @param a The number to take the nth root of, must be non-negative if n is even
    @param n The degree of the root, must be a positive integer
    @return The nth root of a
    """
    if not isinstance(n, int) or not isinstance(a, (int, float)):
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
    if isinstance(a, float):
        raise ValueError("a must be an integer")
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if a < 0:
        raise ValueError("Cannot take factorial of a negative number")
    if a == 0 or a == 1:
        return 1
    return a * factorial(a - 1)

def abs(a: int | float) -> int | float:
    """
    @brief Takes the absolute value of a number.
    This function takes a number and returns its absolute value. It can handle integers, floats... The absolute value of a number is the non-negative value of that number without regard to its sign.
    @param a The number to take the absolute value of
    @return The absolute value of a
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be a number")
    return a if a >= 0 else -a

def negate(a: int | float) -> int | float:
    """
    @brief Negates a number.
    This function takes a number and returns its negation. It can handle integers, floats... The negation of a number is the number with the opposite sign.
    @param a The number to negate
    @return The negation of a
    """
    if not isinstance(a, (int, float)):
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
    
    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        raise TypeError("Both a and b must be numbers")
    return (b / 100) * a

def sin(a: int | float) -> float:
    


    
def add(a, b):
    return a + b
def add_list(numbers):
    total = 0
    if not numbers:
        raise ValueError("The list cannot be empty")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numbers")
        total += num
    return total
def sub(a, b):
    return a - b

def sub_list(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    total = numbers[0]
    for num in numbers[1:]:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be a number")
        total -= num
    return total

def mul(a, b):
    return a * b

def mul_list(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    total = numbers[0]
    for num in numbers[1:]:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be a number")
        total *= num
    return total

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
def pow(a, b):
    return a ** b
def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return a ** 0.5
def root(a, n):
    if a < 0 and n % 2 == 0:
        raise ValueError("Cannot take even root of a negative number")
    return a ** (1/n)

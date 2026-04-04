import sys
import math_lib as ml

def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return
    
    numbers = [float(num) for num in input_data]
    n = len(numbers)

    if n <= 1:
        print("At least two numbers are required to calculate standard deviation.")
        return
    
    sum = ml.add_list(numbers)
    avg = ml.div(sum, n)

    variance_sum = 0.0
    for num in numbers:
        variance_sum = ml.add(variance_sum, ml.pow(num - avg, 2))
    deviation = ml.sqrt(ml.div(variance_sum, n - 1))


    print(deviation)

if __name__ == "__main__":
    main()
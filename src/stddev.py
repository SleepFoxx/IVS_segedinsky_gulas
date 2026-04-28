"""
@file stddev.py
@author Jakub Hulín (xhulinj00)
@brief Calculating standard deviation of a list of numbers.
@details The program reads a list of numbers from standard input, calculates the mean, and then computes the standard deviation using the sample standard deviation formula. The result is printed to standard output.
@version 0.4
@date 2026-04-27

@section LICENSE
This software is licensed under the GNU GPL v3 license.
"""


import sys
import math_lib as ml

##
# @brief Main function to calculate the standard deviation of a list of numbers.
# @details The function reads numbers from standard input, calculates the mean, and then computes the sample standard deviation using the math_lib library. It handles cases where there are not enough numbers to calculate the standard deviation and prints an appropriate message.
# The standard deviation is calculated using the formula:
# \f[
# s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
# \f]
#
# @return None
# @raises ValueError If any element in input_data cannot be converted to float.
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
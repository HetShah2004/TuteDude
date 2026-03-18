# importing math modeule to use its functions
"""
A simple arithmetic module to perfrom square, logarithm and sine operations on a given number.
"""

import math 

# created a function to perfom operations
def math_functions(n):
    """calculating the square, logarithm and sine of the number
        n is the input number for which we want to perform the operations.

        Returns: sqr: the square of the number
                 log: the logarithm of the number
                 sin: the sine of the number
    """
    sqr = math.sqrt(n)
    log = math.log(n)
    sin = math.sin(n)
    # returning the values of the three operations
    return sqr, log, sin



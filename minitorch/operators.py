"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a: float, b: float):
    # Multiplies a and b
    return a * b


def id(input: float):
    # Returns the input unchanged
    return input


def add(a: float, b: float):
    # Adds a and b
    return a + b


def neg(input: float):
    # Negates a number
    return -input


def lt(a: float, b: float):
    # Returns true if a is less than b
    return a < b


def eq(a: float, b: float):
    # Returns true if a and b are equal
    return a == b


def max(a: float, b: float):
    # Returns the larger of two numbers
    return a if a > b else b


def is_close(a: float, b: float):
    # Returns true if the difference between a and b is less than 1e-2
    return abs(a - b) < 1e-2


def sigmoid(input: float):
    """
    Calculates the sigmoud function.
    We use this piecewise definition of the sigmoid function to prevent overflow and underflow issues.
    """
    if input < 0:
        exp = math.exp(input)
        return exp / (1 + exp)

    return 1.0 / (1.0 + math.exp(-input))


def relu(input: float):
    """
    Applies the ReLu activation function
    """
    return max(0, input)


def log(input: float):
    # Calculates the exponential function
    return math.log(input)


def exp(input: float):
    # Calculates the exponential function
    return math.exp(input)


def inv(input: float):
    # Calculates the reciprocal
    return 1 / input


def log_back(a: float, b: float):
    # Multiples the derivative of log(a) by b.
    return inv(a) * b


def inv_back(a: float, b: float):
    # Multiplies the derivative of inv(a) by b
    return pow(-a, -2) * b


def relu_back(a: float, b: float):
    # Multiplies the derivative of relu(a) by b
    relu_val = relu(a)
    return (0 if relu_val == 0 else 1) * b


def negList():
    pass


def addLists():
    pass


def sum():
    pass


def prod():
    pass


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

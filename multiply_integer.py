#!/usr/bin/python3
"""defines multiplication"""


def multiply(self, num1, num2):
    """gives the product of two integer numbers
    Args:
    num1(int): the first number
    num2(int): the second number
    Raises:
        TypeError: num1 and num2 must be integers
    return:
    product
    """
    if type(num1) is not int:
        raise TypeError('num1 must be integer')
    if type(num2) is not int:
        raise TypeError('num2 must be integer')

    return num1 * num2

#!/usr/bin/env python3
"""
prints even and odd for the numbers given
"""


def even_odd(num):
    if (type(num) is not int):
        raise TypeError(f"{num} is not an int")
    if (num % 2 == 0):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

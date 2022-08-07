#!/usr/bin/python3
"""defines unittest for the module multiply_integer.py"""
import unittest
from multiply_integer import multiply
"""module = __import__('multiply_integer').multiply"""


class Test_multiply_integer(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            multiply("string", 'string')
            multiply(3.4, 2)

    def test_mult(self):
        self.assertEqual(multiply(self, 2, 2), 4)
        self.assertEqual(multiply(self, 3, 5), 15)
        self.assertEqual(multiply(self, 2, -10), -20)

    def test_nan(self):
        with self.assertRaises(TypeError):
            multiply(None, 2)
            multiply(2, None)


if __name__ == "__main__":
    unittest.main()

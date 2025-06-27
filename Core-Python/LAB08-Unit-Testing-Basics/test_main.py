#!/usr/bin/env python3
"""
LAB08 - Unit Testing Basics in Python

This module contains unit tests for the functions in main.py.
It demonstrates how to structure test cases, use assertions,
and test different aspects of your code.
"""

import unittest
# TODO: Import the functions you'll be testing from main.py


class TestMain(unittest.TestCase):
    """Test case for the functions in main.py."""
    
    # TODO: Write a test method for the add function
    # The method should:
    # - Be named test_add
    # - Test multiple scenarios (positive numbers, negative numbers, zeros)
    # - Use assertEqual to verify that the function returns the expected sum
    #

    
    # TODO: Write a test method for the is_even function
    # The method should:
    # - Be named test_is_even
    # - Test both even and odd numbers
    # - Use assertTrue for even numbers and assertFalse for odd numbers
    # - Include edge cases like zero and negative numbers
    #

    
    # TODO: Write a test method for the get_largest function
    # The method should:
    # - Be named test_get_largest
    # - Test with various list inputs
    # - Use assertEqual to verify the function returns the largest number
    # - Include tests for negative numbers, duplicates, and single-element lists
    #

    
    # TODO: Write a test method for the get_largest function with empty list
    # The method should:
    # - Be named test_get_largest_empty_list
    # - Use assertRaises to verify that an empty list raises ValueError
    #

    
    # TODO: Write a test method for the reverse_string function
    # The method should:
    # - Be named test_reverse_string
    # - Test with various string inputs
    # - Use assertEqual to verify the function returns the reversed string
    # - Include tests for empty strings, single characters, and palindromes
    #

    
    # BONUS: Explore other assertion methods
    # Try using different assertion methods like:
    # - assertIn: Check if an item is in a container
    # - assertIsNone: Check if something is None
    # - assertAlmostEqual: Compare floats with tolerance
    # - assertGreater: Check if a value is greater than another
    #


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Run tests with detailed output 
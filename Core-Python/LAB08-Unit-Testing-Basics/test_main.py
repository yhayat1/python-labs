#!/usr/bin/env python3
"""
LAB08 - Unit Testing Basics in Python

This module contains unit tests for the functions in main.py.
"""

import unittest
# TODO: Import the functions you'll be testing from main.py
# from main import add, is_even, get_largest, reverse_string


class TestMain(unittest.TestCase):
    """Test case for the functions in main.py."""
    
    # TODO: Write a test method for the add function
    # The method should be named test_add
    # Use assertEqual to verify that the function returns the expected sum
    # Example: self.assertEqual(add(2, 3), 5)
    
    
    # TODO: Write a test method for the is_even function
    # The method should be named test_is_even
    # Use assertTrue and assertFalse to verify the function's return values
    # Example: self.assertTrue(is_even(2))
    
    
    # TODO: Write a test method for the get_largest function
    # The method should be named test_get_largest
    # Use assertEqual to verify that the function returns the largest number
    # Include tests for negative numbers, duplicates, and single-element lists
    
    
    # TODO: Write a test method for the reverse_string function
    # The method should be named test_reverse_string
    # Use assertEqual to verify the function's return values
    # Test with various strings including empty strings and palindromes
    
    
    # BONUS: Write a test that should fail
    # Uncomment this to see how failing tests are reported
    # def test_should_fail(self):
    #     self.assertEqual(1, 2, "This test should fail")
    
    
    # BONUS: Explore other assertion methods in unittest
    # Try using assertIn, assertRaises, assertAlmostEqual, etc.


if __name__ == '__main__':
    unittest.main() 
# LAB08 - Unit Testing Basics in Python (Solutions)

This document provides the reference solutions for the Unit Testing Basics lab. Please attempt to solve the lab on your own before consulting these solutions.

## Solution for `main.py`

```python
#!/usr/bin/env python3
"""
LAB08 - Unit Testing Basics in Python

This module contains functions that will be tested in test_main.py.
"""

def add(a, b):
    """
    Add two numbers together and return the result.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number: The number to check
        
    Returns:
        True if the number is even, False otherwise
    """
    return number % 2 == 0


def get_largest(numbers):
    """
    Find the largest number in a list.
    
    Args:
        numbers: A list of numbers
        
    Returns:
        The largest number in the list
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot find largest in an empty list")
    return max(numbers)


def reverse_string(text):
    """
    Reverse a string.
    
    Args:
        text: The string to reverse
        
    Returns:
        The reversed string
    """
    return text[::-1]


if __name__ == "__main__":
    # This code runs only if the script is executed directly
    print("Testing functions manually:")
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"is_even(4) = {is_even(4)}")
    print(f"get_largest([1, 5, 3]) = {get_largest([1, 5, 3])}")
    print(f"reverse_string('hello') = {reverse_string('hello')}")
```

## Solution for `test_main.py`

```python
#!/usr/bin/env python3
"""
LAB08 - Unit Testing Basics in Python

This module contains unit tests for the functions in main.py.
"""

import unittest
from main import add, is_even, get_largest, reverse_string


class TestMain(unittest.TestCase):
    """Test case for the functions in main.py."""
    
    def test_add(self):
        """Test the add function with various inputs."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -7), -12)
    
    def test_is_even(self):
        """Test the is_even function with even and odd numbers."""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))
    
    def test_get_largest(self):
        """Test the get_largest function with various inputs."""
        self.assertEqual(get_largest([1, 5, 3]), 5)
        self.assertEqual(get_largest([-1, -5, -3]), -1)
        self.assertEqual(get_largest([7]), 7)
        self.assertEqual(get_largest([1, 1, 1]), 1)
        
    def test_get_largest_empty_list(self):
        """Test that get_largest raises ValueError with an empty list."""
        with self.assertRaises(ValueError):
            get_largest([])
    
    def test_reverse_string(self):
        """Test the reverse_string function with various inputs."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("Python"), "nohtyP")
    
    # Example of additional test methods using other assertions
    
    def test_list_contents(self):
        """Example test demonstrating assertIn."""
        fruits = ["apple", "banana", "orange"]
        self.assertIn("banana", fruits)
        self.assertNotIn("grape", fruits)
    
    def test_almost_equal(self):
        """Example test demonstrating assertAlmostEqual for floating-point."""
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=15)


if __name__ == '__main__':
    unittest.main()
```

## Running the Tests

To run the tests, use the following command:

```bash
python -m unittest test_main.py
```

Alternatively, you can run:

```bash
python test_main.py
```

## Key Learning Points

1. **Basic Test Structure**:
   - Tests are organized in classes that inherit from `unittest.TestCase`
   - Test methods must start with `test_`
   - Each test method tests a specific functionality

2. **Common Assertions**:
   - `assertEqual(a, b)`: Verify that a equals b
   - `assertTrue(x)`: Verify that x is True
   - `assertFalse(x)`: Verify that x is False
   - `assertRaises(exception, callable, *args, **kwargs)`: Verify that calling the function raises the expected exception
   - `assertIn(a, b)`: Verify that a is in b
   - `assertAlmostEqual(a, b, places=7)`: Verify that a and b are equal to a specified precision

3. **Test Isolation**:
   - Each test should be independent of others
   - Tests should not depend on the order of execution

4. **Error Testing**:
   - It's important to test error cases, like empty lists or invalid inputs
   - Use `assertRaises` to verify that functions raise appropriate exceptions

5. **Test Coverage**:
   - Try to test all code paths and edge cases
   - Test with both valid and invalid inputs

## Common Issues and Troubleshooting

1. **Tests Not Being Found**:
   - Ensure test methods start with `test_`
   - Make sure the test class inherits from `unittest.TestCase`

2. **Import Errors**:
   - Ensure the module being tested is in the Python path
   - Check for typos in import statements

3. **Assertion Errors**:
   - Review the error message to understand why the test failed
   - Check the values being tested and the expected results

4. **Floating-Point Comparisons**:
   - Use `assertAlmostEqual` instead of `assertEqual` for floating-point numbers due to floating-point precision issues
   - Example: `0.1 + 0.2` doesn't exactly equal `0.3` in floating-point arithmetic

5. **False Positives/Negatives**:
   - Make sure tests actually verify the functionality they're supposed to test
   - Avoid tests that would pass even if the code is broken

## DevOps Application

In DevOps contexts, unit testing is crucial for:

1. **Automation Scripts**: Ensure your deployment and infrastructure scripts work correctly before execution
2. **Configuration Management**: Validate that configuration templates produce expected results
3. **CI/CD Pipelines**: Automatically detect issues before code reaches production
4. **API Testing**: Verify integrations with external services work as expected
5. **Infrastructure as Code**: Test that your infrastructure definitions produce expected resources

Remember that testing is an investment that pays off by reducing debugging time and preventing production issues! 
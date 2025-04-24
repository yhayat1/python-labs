#!/usr/bin/env python3
"""
LAB01 - Simple CLI Calculator Tool

This script demonstrates how to build a command-line interface (CLI) tool using argparse.
The tool performs basic arithmetic operations based on user input.

Usage:
    python cli_tool.py 10 5 --op add     # Result: 15
    python cli_tool.py 10 5 --op sub     # Result: 5
"""

# TODO: Import the argparse module


# TODO: Create an argument parser
# Create an ArgumentParser object with a description


# TODO: Add arguments to the parser
# 1. Add a positional argument 'x' (first number)
# 2. Add a positional argument 'y' (second number)
# 3. Add an optional argument '--op' with choices and a default value


# TODO: Parse the arguments


# TODO: Implement the calculator logic
# Perform different operations based on the --op argument
# For example, add or subtract the numbers


# TODO: BONUS - Extend the calculator
# Add support for additional operations like:
# - mul (multiplication)
# - div (division)
# - pow (power/exponentiation)
# - mod (modulo)
# Add error handling for division by zero


if __name__ == "__main__":
    # This ensures the code only runs when the script is executed directly
    # Uncomment after implementing the code:
    
    # Execute your calculator logic here
    
    # Print a helpful message showing the available commands
    print("\nTry these commands:")
    print("  python cli_tool.py 10 5 --op add")
    print("  python cli_tool.py 10 5 --op sub") 
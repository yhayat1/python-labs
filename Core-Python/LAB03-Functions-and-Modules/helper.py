#!/usr/bin/env python3
"""
Helper Module for LAB03

This module contains utility functions that will be imported and used in main.py.
"""

# TODO: Define a function called greet
# This function should:
# - Accept a parameter called 'name'
# - Return a greeting string like "Hello, {name}!"

def greet(name):
    #name = input("Enter your name: ")
    print(f"Hello, {name}!")

greet("Yossi")

# TODO: Define a function called add
# This function should:
# - Accept two parameters, 'x' and 'y'
# - Return the sum of x and y

def add(x, y):
    return x + y

result = add(5, 3)
print(result)

# TODO: Bonus - Define a function called max_of_three
# This function should:
# - Accept three parameters: 'a', 'b', and 'c'
# - Return the maximum value of the three
# Hint: You can use the built-in max() function

def max_of_three(a, b, c):
    return max(a, b, c)

result = max_of_three(1, 9, 5)
print(result)

# TODO: Extra Challenge - Create your own function
# Define a new function that does something useful (e.g., calculate area, multiply numbers, etc.)
# Make sure to include docstrings explaining what the function does!

# The below function multiples 3 given strings by order
# For example, parameter "3, 3, 3" will multiple 3 by 3 (9) and then multiple 9 by 3 (27)
def multiple(a, b, c):
    return (a * b * c)

result = multiple(3, 3, 3)
print(result)

if __name__ == "__main__":
    # This code only runs when helper.py is executed directly (not when imported)
    print("This is the helper module containing utility functions.")
    print("Import these functions in main.py to use them!")
    
    # You can also add test calls here to verify your functions work correctly
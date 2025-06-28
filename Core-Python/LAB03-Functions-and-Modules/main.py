#!/usr/bin/env python3
"""
LAB03 - Functions and Modules in Python

Instructions:
1. Complete both this file and helper.py
2. Import and use the functions from helper.py in this file
3. Run the script to test your implementations
"""

# TODO: Import functions from helper.py
# Add your import statement here to bring in the functions you'll create
import helper

# TODO: Call the greet() function
# Call the greet() function with your name or "DevOps Learner"
helper.greet("Yossi Hayat")

# TODO: Call the add() function
# Call the add() function with two numbers and print the result
result = helper.add(3, 5)
print(result)


# TODO: Bonus - Call the max_of_three() function
# Call the max_of_three() function with three different numbers
# Print the result
result = helper.max_of_three(3, 9, 6)
print(result)


# TODO: Extra Challenge - Create and call a new function
# First, add a new function to helper.py (e.g., multiply, calculate_area, etc.)
# Then import and use it here
result = helper.multiple(3, 3, 3)
print(result)


print("\nGreat job! You've successfully worked with functions and modules.")
print("Run this script with: python main.py")
print("Check your implementation against the validation checklist in the README.md") 
#!/usr/bin/env python3
"""
LAB02 - Python Basics: Loops and Conditional Logic

Instructions:
1. Complete each of the exercises below
2. Add your own code where indicated by the TODO comments
3. Run the script to test your implementations
"""

# TODO: 1. Conditional Statements
# Create a variable 'age' and write conditional logic to print 
# different messages based on the age value
# - If age is 18 or older: "You are an adult."
# - If age is between 13-17: "You are a teenager."
# - Otherwise: "You are a child."
age = 12

if age > 18:
    print("You're an adult")
elif age >= 13 and age <= 17:
    print("You're a teenager")
else:
    print("You are a child")


# TODO: 2. Loop Over a List
# Create a list called 'skills' with at least 3 technology skills
# Use a for loop to iterate over the list and print each skill
# Example output: "Learning: Python"

skills = ["python", "bash", "powershell"]
for skill in skills:
    print("Learning:", skill)



# TODO: 3. Use a While Loop
# Create a counter variable
# Write a while loop that prints the counter value until it reaches 3
# Don't forget to increment the counter inside the loop!

counter = 0
while counter <= 3:
    print("Count:", counter)
    counter += 1


# TODO: 4. Bonus: Loop with Conditional Logic
# Create a list of 'users' including at least "admin", "guest", and one other username
# Loop through the users and print a different greeting message for "admin" vs other users

users = ["admin", "guest", "bob", "alice"]
for user in users:
    print("User currently being iterated is:", user)
    if user == "admin":        
        print("Currently iterated user is admin!")
    else:
        print("Currently iterated user is not admin.")



# TODO: 5. Extra Challenge: Nested Loops
# Create a small 2D structure (e.g., a 3x3 grid using a list of lists)
# Use nested loops to iterate through each element and print its position and value



print("\nGreat job! You've successfully worked with loops and conditionals.")
print("Run this script with: python main.py")
print("Check your implementation against the validation checklist in the README.md") 
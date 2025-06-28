#!/usr/bin/env python3
"""
LAB01 - Python Basics: Variables and Data Types

Instructions:
1. Follow the comments below to create variables and print them
2. Run the script to see your results
3. Try experimenting with different values
"""

# TODO: 1. Create variables of different types

# Create a string variable called 'name'
# Example: name = "Your Name"
name = "Yossi Hayat"

# Create an integer variable called 'age'
age = 32

# Create a float variable called 'height'
height = 1.76

# Create a boolean variable called 'is_hungry'
is_hungry = True

# Create a list variable called 'skills' with at least 3 skills
skills = ["bash", "python", "powershell"]


# Create a dictionary variable called 'profile' that includes name, age, and skills
profile  = {"name": "Yossi Hayat", "age": 32, "skills": skills}

# TODO: 2. Print the variables using print()

# Print each variable with a descriptive label
# Example: print("Name:", name)
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Hungry?:", is_hungry)
print("Skills:", skills)
print("Profile:", profile)

# TODO: 3. Try basic operations
# Print your age in 5 years
print("Age in 5 years:", age + 5)

# Print the number of skills you have
print(len(skills))

# Print your first skill from the list
print(skills[0])


# BONUS: Try additional operations if you finish early
# Try string methods like .upper() or .lower()

sentence_up_letters = "THIS SENTENCE CONTAINS ONLY UPPERCASE LETTERS"
sentence_low_letters = "this sentence contains only lowercase letters"

# .lower() function
print('Printing "sentence_up_letters" variable without .lower() function:', sentence_up_letters)
print('Printing "sentence_up_letters" variable with .lower() function:', sentence_up_letters.lower())

# .upper() function
print('\nPrinting "sentence_low_letters" variable without .upper() function:', sentence_low_letters)
print('Printing "sentence_low_letters" variable with .upper() function:', sentence_low_letters.upper())


# Try adding a new skill to your list with .append()
skills.append("json")
print(skills)

# Try adding a new key-value pair to your dictionary
profile["Height"] = 1.76
print(profile)


print("\nOnce you're done, run this file with: python main.py")
print("Check your output against the validation checklist in the README.md")
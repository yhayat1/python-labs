#!/usr/bin/env python3
"""
LAB06 - Object-Oriented Programming (OOP) in Python

Instructions:
1. Complete the code blocks below to implement classes and objects
2. Run the script to see how objects interact
3. Add your own methods and attributes to extend functionality
"""

# TODO: 1. Create a Server class
# Define a class called 'Server' with:
# - An __init__ method that takes 'name' and 'ip' parameters
# - A 'ping' method that prints a message showing the server is being pinged


# TODO: 2. Instantiate a Server object
# Create an instance of your Server class with a name and IP address
# Call the ping method on your server instance


# TODO: 3. Create a DatabaseServer class that inherits from Server
# Define a class that extends Server with:
# - An __init__ method that takes 'name', 'ip', and 'engine' parameters
# - A call to the parent class's __init__ method
# - A 'backup' method that prints a message about backing up the database


# TODO: 4. Instantiate a DatabaseServer object
# Create an instance of your DatabaseServer class
# Call both the ping and backup methods


# TODO: 5. Add more advanced OOP concepts (Bonus)
# Try implementing some of these advanced concepts:
# - Add a class variable (shared across all instances)
# - Create a static method
# - Implement property getters and setters
# - Override a method from the parent class


# TODO: 6. Extra Challenge: Create another derived class
# Create a WebServer class that also inherits from Server
# Add methods specific to web servers (deploy, restart, etc.)
# Demonstrate polymorphism by creating a list of different server types
# and calling common methods on them


print("\nGreat job! You've successfully worked with OOP concepts in Python.")
print("You've created classes, instantiated objects, and implemented inheritance.")
print("Run this script with: python main.py") 
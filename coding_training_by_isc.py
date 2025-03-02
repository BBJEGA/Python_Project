# Coding and Research Training Organized by ISC UM6P.
# Week 1 Assignment 1

# Question 1: Write a Python program that takes two numbers as input and prints their sum, difference, product, and quotient.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2
print('Sum', sum_result, '| Product', product_result, '|Difference', difference_result, '|Quotient', quotient_result)

# Question 2: Convert a user-input temperature from Celsius to Fahrenheit. Formula: F=(Cx9/5)+32"""

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Question 3: Ask the user for their name, age, and favorite color, then print a personalized message"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
favorite_color = input("Enter your favorite color: ")
print(f"Hello, {name}! you are {age} years old, and your favorite color is {favorite_color}. That's is awesome!")

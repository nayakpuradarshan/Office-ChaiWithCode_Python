
# 8. Prime Number Checker
"""
Problem: Check if a number is prime.
"""

number = int(input("Enter any number:"))

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False

print(is_prime)
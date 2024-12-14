
# 6. Factorial Calculator
"""
Problem: Compute the factorial of a number using a while loop.
For example: what is the factorial of 5 or how to find factorial of 5?
Ans: 5*4*3*2*1 = 120

"""

number = 5
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1

print("factorial for number 5 is", factorial)


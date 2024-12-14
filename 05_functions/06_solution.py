
# 6. Lambda Function
"""
Problem: Create a lambda function to compute the cube of a number.
"""

# with normal function
def cube(number):
    return number ** 3

# with lambda function
cube = lambda x: x ** 3
print(cube(3))

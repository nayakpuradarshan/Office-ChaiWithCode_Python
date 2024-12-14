
# 1. Counting Positive Numbers
"""
Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
"""
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_in_numbers = 0

for num in numbers:
    if num > 0:
        positive_number_in_numbers = positive_number_in_numbers + 1
print("Final positive number in numbers is:", positive_number_in_numbers)






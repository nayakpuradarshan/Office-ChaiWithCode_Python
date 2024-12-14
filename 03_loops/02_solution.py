
# 2. Sum of Even Numbers
"""
Problem: Calculate the sum of even numbers up to a given number n.
"""

n = 20
even_number = 0

for i in range(2, n+1, 2):
    even_number = even_number + i

print("sum of even number of ", n, "is :", even_number)


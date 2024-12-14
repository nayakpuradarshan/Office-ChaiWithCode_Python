
# 1. Age Group Categorization
""" Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
"""

age = int(input("Enter your age: "))

if age < 13:
    print("You're child")
elif age < 19:
    print("You're teenager")
elif age < 59:
    print("You're adult")
else:
    print("You're senior")




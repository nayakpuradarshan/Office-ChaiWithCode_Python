# 3. Grade Calculator
""" Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79),
D (60-69), F (below 60).
"""

score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("You got A grade")
elif score >= 80 and score <= 89:
    print("You got B grade")
elif score >= 70 and score <= 79:
    print("You got C grade")
elif score >= 60 and score <= 69:
    print("You got D grade")
else:
    print("You got F grade")

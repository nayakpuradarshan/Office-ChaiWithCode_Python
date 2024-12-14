
# 8. Password Strength Checker
"""
Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak),
6-10 chars (Medium), >10 chars (Strong).
"""

password = str(input("Enter password char here: "))


if len(password) < 6:
    password_type = "Weak"
elif len(password) < 10:
    password_type = "Medium"
else:
    password_type = "strong"

print(password_type)


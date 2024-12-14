
# 7. Validate Input
"""
Problem: Keep asking the user for input until they enter a number between 1 and 10.
"""

while True:
    number = int(input("enter number b/w 1 to 10: "))

    if 1 <= number <= 10:
        print("you guess right number! Thanks")
        break
    else:
        print("Wrong number, Try again!")



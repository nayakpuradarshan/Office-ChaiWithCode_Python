
# 5. Weather Activity Suggestion
"""
Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
"""

weather = str(input("How's weather today: "))

if weather == "sunny":
    print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")
else:
    print("see weather carefully!")


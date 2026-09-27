# 1
import math

number = 5

print("Square root:", math.sqrt(number))
print("Factorial:", math.factorial(number))
print("Value of Pi:", math.pi)

# 2
import os

files = os.listdir()

for file in files:
    if file.lower().endswith((".jpg", ".png")):
        print(file)

# 3

from datetime import datetime

date_input = input("Enter date (YYYY-MM-DD): ")

date = datetime.strptime(date_input, "%Y-%m-%d")

print("Day:", date.strftime("%A"))

# 4
def format_follower_count(n):
    if n >= 1000000:
        return f"{n / 1000000:.1f}M"
    elif n >= 1000:
        return f"{n / 1000:.1f}K"
    else:
        return str(n)

# 5

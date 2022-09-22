#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    L_digit = number % -10
else:
    L_digit = number % 10
if (L_digit > 5):
    print(f"Last digit of {number:d} is {L_digit:d} and is greater than 5")
elif (L_digit < 6) and (L_digit != 0):
    print(f"Last digit of {number:d} is {L_digit:d}"
          f" and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {L_digit:d} and is 0")

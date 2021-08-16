"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A value error will occur when a user enters an invalid numbers.txt.
2. When will a ZeroDivisionError occur?
A Zero Division Error occurs when a user tries to divide a numbers.txt by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You could change the code so that the program had error checking and would ask
you to enter another numbers.txt other than zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers.txt!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
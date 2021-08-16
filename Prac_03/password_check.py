"""Rhys Sheehan CP1404 Prac 03 password_check"""

"""On paper, write a program that asks the user for a password, with error-checking to repeat if the password doesn't 
meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters "Pythonista" (10 characters), the program should print "**********"."""

minimum_length = 4


def main():
    password = input("What is your password? ")
    if len(password) == minimum_length:
        print("*" * len(password))
    else: password = input("What is your password? ")


main()

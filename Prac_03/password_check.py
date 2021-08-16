"""Rhys Sheehan CP1404 Prac 03 password_check"""

"""On paper, write a program that asks the user for a password, with error-checking to repeat if the password doesn't 
meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters "Pythonista" (10 characters), the program should print "**********"."""

minimum_length = 4


def main():
    password = get_password(minimum_length)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("What is your password? ")
    while len(password) > minimum_length:
        password = input("What is your password? ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()

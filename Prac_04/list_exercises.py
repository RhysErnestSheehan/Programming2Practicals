"""Rhys Sheehan CP1404 Prac 04 list exercises"""

# basic list operations
numbers = []
for i in range(5):
    number = int(input("Pick a number: "))
    numbers.append(number)

print("The first number is", numbers[0])
print("The last number is", numbers[4])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average number is",)

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter a username: ")
if username in usernames:
    print("Access Granted")
Else: print("Access Denied")

"""
CP1404/CP5632 - Practical
"""

# Program 1
# output_file = open("name.txt", 'w')
# name = input("What is your name? ")
# print(name, file=output_file)
# output_file.close()

# Program 2
# input_file = open("name.txt", "r")
# name = input_file.read()
# input_file.close()
# print("Your name is", name)

# Program 3
input_file = open("numbers.txt", "r")
line1 = int(input_file.readline())
line2 = int(input_file.readline())
input_file.close()
print(line1 + line2)


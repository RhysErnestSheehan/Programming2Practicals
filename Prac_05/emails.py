"""Rhys Sheehan CP1404 Practical 05 emails"""

emails = {}


def main():
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        is_name_correct = input("Is your name {}? (Y/n) ".format(name))
        if is_name_correct.upper() != "Y":
            name = input("Name: ")
        emails[email] = name
        email = input("Email: ")
    print(name, email)


def get_name(email):
    split_name_from_email = email.split('@')[0]
    parts = split_name_from_email.split('.')
    name = " ".join(parts).title()
    return name


main()
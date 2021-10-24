"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():


        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name

# main()

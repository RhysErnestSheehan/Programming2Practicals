"""CP1404 sort files 1"""
import os
import shutil


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        file_extension = filename.split('.')
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        directory = file_extension
        shutil.move(directory)
        print(file_extension, filename)


main()
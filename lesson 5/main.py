from random import choice
import os
from pathlib import Path

def menu():
    print('main menu:')
    print('1. create a directory')
    print('2. delete a directory')
    print('3. create a new file in a directory')
    print('4. write to file')
    print('5. delete a file')
    print('6. get a list of all the files in the directory')
    print('7. show the full path af this directory')
    print('8. exit')
    choice=input()
    if choice==1:
        createDirectory()
    elif choice==2:


def create_directory():
    path=Path(input('enter path:'))
    try:
        path.mkdir()
        print("Directory created successfully.")

    except FileExistsError:
        print("The specified path already exists.")

    except FileNotFoundError:
        print("The parent directory does not exist.")

    except PermissionError:
        print("Permission denied.")

    except OSError as error:
        print("Directory creation failed:", error)

def delete_empty_directory():

def create_new_file_in_directory():
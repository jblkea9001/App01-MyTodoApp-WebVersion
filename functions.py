import os
import sys


FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return
    this list of to-do items. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(tds_local, filepath=FILEPATH):
    """ Write a list of to-do items into a text file. """
    with open(filepath, 'w') as file:
        file.writelines(tds_local)


def CheckFileExists(filepath=FILEPATH):
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, "w") as file:
            pass


def rp(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        return "images/" + relative_path


""" This __name__ is to allow us to test this functions.py
It allow us to test the function without
execute the below line if called from another method.
basically it means try execute the code functions.py and 
Cmd_Line_Interface.py. You will see a difference in this __name__ string
This is useful if you build web apps.
"""

print(__name__)
if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())

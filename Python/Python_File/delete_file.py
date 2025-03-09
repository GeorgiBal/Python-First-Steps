import os

path = "delete.txt"
try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")

import os

location = "C:\\Users\\БАЛДЖИЕВ\\Desktop\\test.txt"

if os.path.exists(location):
    print("This location exists!!!")
    if os.path.isfile(location):
        print("This is file!!!")
    elif os.path.isdir(location):
        print("That is a directory!!!")
else:
    print("This location doesn't exists")

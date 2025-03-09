from tkinter import *


def create_window():
    # new_window = Toplevel() # Linked windows(if you close the first one
                              # you close all of them)
    new_window = Tk()  # creates independent windows
    old_window.destroy()  # closes the previous window


old_window = Tk()

Button(old_window, text="Create new window", command=create_window).pack()

old_window.mainloop()

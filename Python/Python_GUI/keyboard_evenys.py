from tkinter import *


def do_something(event):
    label.config(text=event.keysym)


window = Tk()

label = Label(window, font=("Helvetica", 100))
label.pack()

window.bind("<Key>", do_something)

window.mainloop()

from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    print(color)
    color_hex = color[1]
    window.config(bg=color_hex)


window = Tk()
window.geometry("420x420")

button = Button(window,
                text="CLICK ME!",
                command=click)
button.pack()

window.mainloop()

from tkinter import *
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\БАЛДЖИЕВ\\Documents\\Python\\Python_GUI",
                                          title="Open file",
                                          filetypes=[("Text files", "*.txt"),
                                                     ("All files", ".*")])
    file = open(filepath, "r")
    print(file.read())
    file.close()


window = Tk()

button = Button(window,
                text="OPEN",
                command=open_file)
button.pack()

window.mainloop()

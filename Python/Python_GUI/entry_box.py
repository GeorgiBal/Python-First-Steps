from tkinter import *


def submit():
    username = entry.get()
    print("Hello ", username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()

entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              show="*")
# entry.insert(0, "Text")
entry.pack(side=LEFT)

submit = Button(window,
                text="SUBMIT",
                command=submit)
submit.pack(side=RIGHT)

delete = Button(window,
                text="DELETE",
                command=delete)
delete.pack(side=RIGHT)

backspace = Button(window,
                   text="BACKSPACE",
                   command=backspace)
backspace.pack(side=RIGHT)

window.mainloop()

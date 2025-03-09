from tkinter import *


def submit():
    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))

    print("You ordered:")

    for i in food:
        print(i)


def add():
    listbox.insert(listbox.size(), entry.get())
    listbox.config(height=listbox.size())


def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Bread")
listbox.insert(4,  "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size(), width=listbox.size())

entry = Entry(window)
entry.pack()

submit = Button(window,
                text="SUBMIT",
                command=submit,)
submit.pack()

add = Button(window,
             text="ADD",
             command=add)
add.pack()

delete = Button(window,
                text="DELETE",
                command=delete)
delete.pack()

window.mainloop()

from tkinter import *


def open_file():
    print("You opened file")


def save_file():
    print("You saved file")


def cut():
    print("You cut some text")


def copy():
    print("You copy some text")


def paste():
    print("You paste some text")


window = Tk()

open_image = PhotoImage(file="open_file.png")
save_image = PhotoImage(file="save.png")
exit_image = PhotoImage(file="exit.png")

cut_image = PhotoImage(file="scissors.png")
copy_image = PhotoImage(file="copy.png")
paste_image = PhotoImage(file="paste.png")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0, font=("MV Boli", 15))
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open",
                      command=open_file,
                      image=open_image,
                      compound="left")
file_menu.add_separator()
file_menu.add_command(label="Save",
                      command=save_file,
                      image=save_image,
                      compound="left")
file_menu.add_separator()
file_menu.add_command(label="Exit",
                      command=quit,
                      image=exit_image,
                      compound="left")

edit_menu = Menu(menu_bar, tearoff=0, font=("MV Boli", 15))
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut",
                      command=cut,
                      image=cut_image,
                      compound="left")
edit_menu.add_separator()
edit_menu.add_command(label="Copy",
                      command=copy,
                      image=copy_image,
                      compound="left")
edit_menu.add_separator()
edit_menu.add_command(label="Paste",
                      command=paste,
                      image=paste_image,
                      compound="left")

window.mainloop()

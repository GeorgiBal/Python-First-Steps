from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="Info message box", message="You are a programmer")
    # messagebox.showwarning(title="WARNING!", message="You have a VIRUS!")
    # messagebox.showerror(title="ERROR!", message="Something went wrong")
    """
    if messagebox.askokcancel(title="Question?", message="Do you want to continue?"):
        print("You want to continue")
    else:
        print("You don't want to continue")
    """
    """
    if messagebox.askretrycancel(title="Question?", message="Do you want to retry?"):
        print("You want to retry")
    else:
        print("You don't want to retry")
    """
    """
    if messagebox.askyesno(title="Question?", message="Do you want to continue?"):
        print("You want to continue")
    else:
        print("You don't want to continue")
    """
    """
    answer = messagebox.askquestion(title="Question?", message="Do you want to continue?")
    if answer == "yes":
        print("You want to continue")
    else:
        print("You don't want to continue")
    """
    answer = messagebox.askyesnocancel(title="Question?", message="Do you want to continue?", icon="warning")
    if answer:
        print("You want to continue")
    elif answer is False:
        print("You don't want to continue")
    else:
        print("You closed the old_window")


window = Tk()

button = Button(window,
                text="CLICK ME!",
                command=click)
button.pack()

window.mainloop()

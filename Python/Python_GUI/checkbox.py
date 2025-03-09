from tkinter import *


def display():
    if x.get() == 1:
        print("You agree")
    else:
        print("You disagree")


window = Tk()

photo = PhotoImage(file="uktc.png")

x = IntVar()

check = Checkbutton(window,
                    text="I agree!",
                    variable=x,
                    onvalue=1,
                    offvalue=0,
                    command=display,
                    font=("Arial", 20),
                    fg="#00FF00",
                    bg="black",
                    activeforeground="#00FF00",
                    activebackground="black",
                    padx=25,
                    pady=10,
                    image=photo,
                    compound="right")
check.pack()

window.mainloop()

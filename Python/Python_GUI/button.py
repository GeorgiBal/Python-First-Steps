from tkinter import *

count = 0


def click():
    global count
    count += 1
    print("I clicked the button!")


window = Tk()

photo = PhotoImage(file="uktc.png")

button = Button(window,
                text="Go To UKTC",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="blue",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()

print("You clicked the button", count, "times")

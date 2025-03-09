from tkinter import *

window = Tk()

title = Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

first_name = Label(window, text="First name", width=20, bg="red").grid(row=1, column=0)
first_name_entry = Entry(window).grid(row=1, column=1)

last_name = Label(window, text="Last name", bg="blue").grid(row=2, column=0)
last_name_entry = Entry(window).grid(row=2, column=1)

email = Label(window, text="Email", bg="green", width=30).grid(row=3, column=0)
email_entry = Entry(window).grid(row=3, column=1)

submit = Button(window, text="SUBMIT").grid(row=4, column=0, columnspan=2)

window.mainloop()

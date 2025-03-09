from tkinter import *

window = Tk()
# old_window.geometry("420x420")

photo = PhotoImage(file="uktc.png")

label = Label(window,
              text="PYTHON COURSE",
              font=("Arial", 40, "bold"),
              fg="#00FF00",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom")

# label.place(x=100, y=100)
label.pack()

window.mainloop()

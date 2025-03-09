from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("My First GUI")

icon = PhotoImage(file="uktc.png")
window.iconphoto(True, icon)

window.config(background="#5ce9ff")

window.mainloop()

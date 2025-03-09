from tkinter import *

food = ["pizza", "burger", "hotdog"]


def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered burger!")
    elif x.get() == 2:
        print("You ordered hotdog!")
    else:
        print("Huh?")


window = Tk()

x = IntVar()

pizza = PhotoImage(file="pizza.png")
burger = PhotoImage(file="hamburger.png")
hotdog = PhotoImage(file="hotdog.png")
food_images = [pizza, burger, hotdog]


for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[i],
                              variable=x,
                              value=i,
                              padx=25,
                              font=("Impact", 50),
                              image=food_images[i],
                              compound="left",
                              indicatoron=0,
                              width=350,
                              command=order)
    radiobutton.pack(anchor=W)

window.mainloop()

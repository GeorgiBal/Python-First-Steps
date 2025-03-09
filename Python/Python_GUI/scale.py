from tkinter import *


def submit():
    print("The temperature is:", scale.get(), "degrees C")


window = Tk()

hot = PhotoImage(file="fire.png")
hot_label = Label(image=hot)
hot_label.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL,
              font=("Consolas", 20),
              tickinterval=10,
              # showvalue = 0, # hide current value
              resolution=5,
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="black",)
scale.pack()
scale.set(((scale["from"]-scale["to"])/2) + scale["to"])

cold = PhotoImage(file="snowflake.png")
cold_label = Label(image=cold)
cold_label.pack()

button = Button(window,
                text="SUBMIT",
                command=submit)
button.pack()

window.mainloop()

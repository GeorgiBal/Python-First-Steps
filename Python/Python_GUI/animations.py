from tkinter import *
import time

WIDTH = 280
HEIGHT = 180

x_velocity = 3.7
y_velocity = 2.5

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

space = PhotoImage(file="space.png")
background = canvas.create_image(0, 0, image=space, anchor=NW)

ufo = PhotoImage(file="ufo.png")
my_image = canvas.create_image(0, 0, image=ufo, anchor=NW)

image_width = ufo.width()
image_height = ufo.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        x_velocity = -x_velocity
    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        y_velocity = -y_velocity
    canvas.move(my_image, x_velocity, y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()

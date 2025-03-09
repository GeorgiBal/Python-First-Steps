from tkinter import *
from ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 3, 1, "white")
tennis_ball = Ball(canvas, 100, 0, 50, 5, 2, "yellow")
basket_ball = Ball(canvas, 30, 30, 150, 8, 5, "orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500, bg="green")

# canvas.create_line(0, 0, 500, 500, fill="blue", width=5)
# canvas.create_line(0, 500, 500, 0, fill="red", width=5)
# canvas.create_rectangle(50, 50, 250, 250, fill="purple")
# points = [(250, 0), (500, 500), (0, 500)]
# canvas.create_polygon(points, fill="yellow", outline="black", width=5)
# canvas.create_arc(0, 0, 500, 500, style=PIESLICE, start=270, extent=180)
canvas.create_arc(0, 0, 500, 500, style=PIESLICE, start=0, extent=180, fill="red", width=10)
canvas.create_arc(0, 0, 500, 500, style=PIESLICE, start=180, extent=180, fill="white", width=10)
canvas.create_oval(190, 190, 310, 310, fill="white", width=10)
canvas.create_oval(220, 220, 280, 280, fill="white", width=5)

canvas.pack()

window.mainloop()

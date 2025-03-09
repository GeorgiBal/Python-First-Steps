from tkinter import *


def button_press(num):
    global eql_text
    eql_text += str(num)

    eql_label.set(eql_text)


def equals():
    global eql_text

    try:
        total = str(eval(eql_text))
        eql_label.set(total)
        eql_text = total
    except SyntaxError:
        eql_label.set("Syntax error")
        eql_text = ""
    except ZeroDivisionError:
        eql_label.set("Arithmetic error")
        eql_text = ""


def clear():
    global eql_text

    eql_text = ""
    eql_label.set("")


window = Tk()
window.title("Calculator")
window.geometry("470x640")

eql_text = ""
eql_label = StringVar()


label = Label(window,
              textvariable=eql_label,
              font=("consolas", 20),
              bg="white",
              width=31,
              height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,
                 text=1,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)
button2 = Button(frame,
                 text=2,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)
button3 = Button(frame,
                 text=3,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)
button4 = Button(frame,
                 text=4,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)
button5 = Button(frame,
                 text=5,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)
button6 = Button(frame,
                 text=6,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)
button7 = Button(frame,
                 text=7,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)
button8 = Button(frame,
                 text=8,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)
button9 = Button(frame,
                 text=9,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)
button0 = Button(frame,
                 text=0,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=1)
plus = Button(frame,
              text="+",
              height=4,
              width=9,
              font=35,
              command=lambda: button_press("+"))
plus.grid(row=0, column=3)
minus = Button(frame,
               text="-",
               height=4,
               width=9,
               font=35,
               command=lambda: button_press("-"))
minus.grid(row=1, column=3)
multiply = Button(frame,
                  text="*",
                  height=4,
                  width=9,
                  font=35,
                  command=lambda: button_press("*"))
multiply.grid(row=2, column=3)
divide = Button(frame,
                text="/",
                height=4,
                width=9,
                font=35,
                command=lambda: button_press("/"))
divide.grid(row=3, column=3)
equal = Button(frame,
               text="=",
               height=4,
               width=9,
               font=35,
               command=equals)
equal.grid(row=3, column=2)
decimal = Button(frame,
                 text=".",
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press("."))
decimal.grid(row=3, column=0)
clear = Button(window,
               text="Clear",
               height=4,
               width=39,
               font=35,
               command=clear)
clear.pack()
window.mainloop()

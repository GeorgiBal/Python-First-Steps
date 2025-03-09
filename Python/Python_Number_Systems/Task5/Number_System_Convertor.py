from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Number convertor')
root.minsize(980, 520)
root.maxsize(980, 520)

num = StringVar()
num.set("")
result_var = StringVar()


def convert():
    if num.get() == 0:
        messagebox.showerror('Error', ' You must enter a number to convert')
    else:
        try:
            if from_var.get() == "Decimal":
                if to_var.get() == "Decimal":
                    result_var.set(num.get())
                elif to_var.get() == "Binary":
                    res = str(bin(int(num.get())))
                    result_var.set(res[2:])
                elif to_var.get() == "Hex":
                    res = str(hex(int(num.get())))
                    result_var.set(res[2:])
                elif to_var.get() == "Octal":
                    res = str(oct(int(num.get())))
                    result_var.set(res[2:])
            elif from_var.get() == "Binary":
                dec = int(str(int(num.get())), 2)
                if to_var.get() == "Binary":
                    result_var.set(num.get())
                elif to_var.get() == "Decimal":
                    result_var.set(str(dec))
                elif to_var.get() == "Hex":
                    res = str(hex(int(dec)))
                    result_var.set(res[2:])
                elif to_var.get() == "Octal":
                    res = str(oct(int(dec)))
                    result_var.set(res[2:])
            elif from_var.get() == "Hex":
                dec = int(str(num.get()), 16)
                if to_var.get() == "Hex":
                    result_var.set(num.get())
                elif to_var.get() == "Decimal":
                    result_var.set(str(dec))
                elif to_var.get() == "Binary":
                    res = str(bin(dec))
                    result_var.set(res[2:])
                elif to_var.get() == "Octal":
                    res = str(oct(dec))
                    result_var.set(res[2:])
            elif from_var.get() == "Octal":
                dec = int(str(int(num.get())), 8)
                if to_var.get() == "Octal":
                    result_var.set(num.get())
                elif to_var.get() == "Decimal":
                    result_var.set(str(dec))
                elif to_var.get() == "Binary":
                    res = str(bin(int(dec)))
                    result_var.set(res[2:])
                elif to_var.get() == "Hex":
                    res = str(hex(int(dec)))
                    result_var.set(res[2:])
        except ValueError:
            messagebox.showerror('Error', ' You must enter a valid number')


def clear():
    num.set("")
    result_var.set("")


def exit_program():
    if messagebox.askyesno('Exit', ' Do you really want to Exit'):
        root.destroy()


Label(root, text='Coversion System',
      font=('times new rommon', 55, 'bold'),
      bg='lime', fg='black', relief=RIDGE).pack(pady=10)

n = Label(root, text='Enter Number:', font='arial 20 bold')
n.place(x=250, y=150)

n_txt = Entry(root, font=('times new rommon', 20, 'bold'), fg='black', justify=CENTER, relief=GROOVE, textvariable=num)
n_txt.place(x=550, y=160)

options = ["Binary",
           "Decimal",
           "Hex",
           "Octal"]

from_var = StringVar()
from_var.set("Decimal")

f = Label(root, text='From: ', font='arial 15 bold')
f.place(x=150, y=210)

from_menu = OptionMenu(root, from_var, *options)
from_menu.config(width=30, height=1, font=('times new rommon', 10, 'bold'))
from_menu.place(x=230, y=210)

to_var = StringVar()
to_var.set("Decimal")

t = Label(root, text='To: ', font='arial 15 bold')
t.place(x=150, y=260)

to_menu = OptionMenu(root, to_var, *options)
to_menu.config(width=30, height=1, font=('times new rommon', 10, 'bold'))
to_menu.place(x=230, y=260)

result_label = Label(root, text='Result: ', font='arial 20 bold')
result_label.place(x=650, y=210)

result = Label(root, width=18, height=1, font=('times new rommon', 20, 'bold'), fg='black', justify=CENTER, relief=GROOVE, textvariable=result_var)
result.place(x=550, y=260)

btn1 = Button(root, text='Convert', font='arial 20 bold',
              fg='black', bg='lime', width=10, relief=GROOVE,
              bd=10, command=convert)
btn1.place(x=100, y=370)

btn2 = Button(root, text='Clear', font='arial 20 bold',
              fg='black', bg='lime', width=10, relief=GROOVE,
              bd=10, command=clear)
btn2.place(x=400, y=370)

btn3 = Button(root, text='Exit', font='arial 20 bold',
              fg='black', bg='lime', width=10, relief=GROOVE,
              bd=10, command=exit_program)
btn3.place(x=700, y=370)

root.mainloop()

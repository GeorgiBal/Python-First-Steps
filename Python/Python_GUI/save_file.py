from tkinter import *
from tkinter import filedialog


def save():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\БАЛДЖИЕВ\\Documents\\Python\\Python_GUI",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", "*.txt"),
                                        ("HTML file", "*.html"),
                                        ("All files", ".*")
                                    ])

    if file is None:
        return
    file_text = str(text.get(1.0, END))
    # file_text = input("Enter text: ")
    file.write(file_text)
    file.close()


window = Tk()

button = Button(window,
                text="SAVE",
                command=save)
button.pack()

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")
text.pack()

window.mainloop()

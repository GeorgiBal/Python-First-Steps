from tkinter import *
from tkinter.ttk import *
import time


def start():
    bar["value"] = 0
    gb = 100
    download = 0
    speed = 1
    while download < gb:
        time.sleep(0.05)
        bar["value"] += (speed/gb)*100
        download += speed
        percent.set(str(int((download/gb)*100)) + "%")
        text.set(str(download) + "/" + str(gb) + " GB completed")
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=text).pack()

Button(window, text="Download", command=start).pack()

window.mainloop()

# tic tac toe
from tkinter import *

# view
list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
window = Tk()
window.minsize(900, 500)
window.maxsize(900, 500)
window.title('Tic Tac Toe')
canvas = Canvas(window, height=489, width=630, bg='black')
canvas.place(x=5, y=5)
situation = Canvas(window, height=489, width=255, bg='blue')
situation.place(x=640, y=5)
stat = Label(window, text='STATS:', font=("Courier", 25), fg='black', bg='blue')
stat.place(x=710, y=15)
player_start = Label(window, text='Player X', font=("Courier", 25), fg='black', bg='blue')
player_start.place(x=660, y=145)
turn = Label(window, text='Turn to play:', font=("Courier", 20), fg='black', bg='blue')
turn.place(x=650, y=105)

player = 'X'
tie = 0


def switch_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


def button1():
    text = Label(window, text=player, font=("Courier", 95), fg='white', bg='black')
    text.place(x=65, y=16)
    list1[0] = player
    global tie
    tie += 1
    switch_player()
    win()
    place1.configure(state=DISABLED)
    list2.remove(place1)


def button2():
    text = Label(window, text=player, font=("Courier", 95), fg='white', bg='black')
    text.place(x=275, y=16)
    list1[1] = player
    global tie
    tie += 1
    switch_player()
    win()
    place2.configure(state=DISABLED)
    list2.remove(place2)


def button3():
    text = Label(window, text=player, font=("Courier", 95), fg='white', bg='black')
    text.place(x=485, y=16)
    list1[2] = player
    global tie
    tie += 1
    switch_player()
    win()
    place3.configure(state=DISABLED)
    list2.remove(place3)


def button4():
    text = Label(window, text=player, font=("Courier", 95), fg='white', bg='black')
    text.place(x=65, y=181)
    list1[3] = player
    global tie
    tie += 1
    switch_player()
    win()
    place4.configure(state=DISABLED)
    list2.remove(place4)


def button5():
    text = Label(window, text=player, font=("Courier", 95), fg='white', bg='black')
    text.place(x=275, y=181)
    list1[4] = player
    global tie
    tie += 1
    switch_player()
    win()
    place5.configure(state=DISABLED)
    list2.remove(place5)


def button6():
    text = Label(window, text=player, font=("Courier", 95), fg='white', bg='black')
    text.place(x=485, y=181)
    list1[5] = player
    global tie
    tie += 1
    switch_player()
    win()
    place6.configure(state=DISABLED)
    list2.remove(place6)


def button7():
    text = Label(window, text=player, font=("Courier", 95), fg='white', bg='black')
    text.place(x=65, y=346)
    list1[6] = player
    global tie
    tie += 1
    switch_player()
    win()
    place7.configure(state=DISABLED)
    list2.remove(place7)


def button8():
    text = Label(window, text=player, font=("Courier", 95), fg='white', bg='black')
    text.place(x=275, y=346)
    list1[7] = player
    global tie
    tie += 1
    switch_player()
    win()
    place8.configure(state=DISABLED)
    list2.remove(place8)


def button9():
    text = Label(window, text=player, font=("Courier", 95), fg='white', bg='black')
    text.place(x=485, y=346)
    list1[8] = player
    global tie
    tie += 1
    switch_player()
    win()
    place9.configure(state=DISABLED)
    list2.remove(place9)


def lines():
    line1 = Canvas(window, height=488, width=5, bg='white')
    line1.place(x=210, y=6)

    line2 = Canvas(window, height=488, width=5, bg='white')
    line2.place(x=420, y=6)

    line3 = Canvas(window, height=5, width=629, bg='white')
    line3.place(x=6, y=163)

    line4 = Canvas(window, height=5, width=629, bg='white')
    line4.place(x=6, y=326)


def win():

    if list1[0] == list1[1] == list1[2] or \
            list1[3] == list1[4] == list1[5] or \
            list1[6] == list1[7] == list1[8] or \
            list1[0] == list1[3] == list1[6] or \
            list1[1] == list1[4] == list1[7] or \
            list1[2] == list1[5] == list1[8] or \
            list1[0] == list1[4] == list1[8] or \
            list1[2] == list1[4] == list1[6]:
        winning = Label(window,  text='WINS!', font=("Courier", 25), fg='black', bg='blue')
        winning.place(x=700, y=200)
        for i in range(len(list2)):
            list2[i].configure(state=DISABLED)
            i += 1
        turn.config(text='')
    elif tie > 8:
        game_tie = Label(window, text='TIE!', font=("Courier", 25), fg='black', bg='blue')
        game_tie.place(x=700, y=200)
        turn.config(text='')
    else:
        player_stat = Label(window, text='Player ' + player, font=("Courier", 25), fg='black', bg='blue')
        player_stat.place(x=660, y=145)


place1 = Button(canvas, height=10, width=28, fg='black', bg='black', command=button1)
place1.place(x=1, y=1)

place2 = Button(canvas, height=10, width=28, fg='black', bg='black', command=button2)
place2.place(x=213, y=1)

place3 = Button(canvas, height=10, width=28, fg='black', bg='black', command=button3)
place3.place(x=425, y=1)

place4 = Button(canvas, height=10, width=28, fg='black', bg='black', command=button4)
place4.place(x=1, y=165)

place5 = Button(canvas, height=10, width=28, fg='black', bg='black', command=button5)
place5.place(x=213, y=165)

place6 = Button(canvas, height=10, width=28, fg='black', bg='black', command=button6)
place6.place(x=425, y=165)

place7 = Button(canvas, height=10, width=28, fg='black', bg='black', command=button7)
place7.place(x=1, y=330)

place8 = Button(canvas, height=10, width=28, fg='black', bg='black', command=button8)
place8.place(x=213, y=330)

place9 = Button(canvas, height=10, width=28, fg='black', bg='black', command=button9)
place9.place(x=425, y=330)

lines()
list2 = [place1, place2, place3, place4, place5, place6, place7, place8, place9]


window.mainloop()

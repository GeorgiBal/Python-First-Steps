# Import the tools
import random
from tkinter import *

# Create the window
root = Tk()
root.minsize(800, 500)
root.maxsize(800, 500)
root.title('ROCK, PAPER, SCISSORS',)
root.iconbitmap(r"rps.ico")

# Create the game window
canvas2 = Canvas(root, height=472, width=385, bg='black')
canvas2.place(x=405, y=18)

# Create the necessary variables
COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""

# Create the text with the score
your_score = Label(root, text='YOUR SCORE: 0', font=("Courier", 25), fg='white', bg='black')
your_score.place(x=420, y=400)

bot_score = Label(root, text='BOT SCORE: 0', font=("Courier", 25), fg='white', bg='black')
bot_score.place(x=440, y=440)

# Create the text with the choice
your_choice = Label(root, text='YOU: ', font=("Courier", 25), fg='white', bg='black')
your_choice.place(x=440, y=50)

bot_choice = Label(root, text='BOT: ', font=("Courier", 25), fg='white', bg='black')
bot_choice.place(x=440, y=100)

# Create the text with the point
point = Label(root, text='POINT: ', font=("Courier", 25), fg='white', bg='black')
point.place(x=420, y=250)


# Make the choices to numbers to use them later
def choice_to_number(choice):
    return {'rock': 0, 'paper': 1, 'scissors': 2}[choice]


def number_to_choice(number):
    return {0: 'rock', 1: 'paper', 2: 'scissors'}[number]


# Make the choice of the computer
def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


# Sum and visualize the result
def choice_result(computer, human):
    global COMPUTER_SCORE, HUMAN_SCORE
    global your_score, bot_score
    global your_choice, bot_choice

    human_number = choice_to_number(human)
    computer_number = choice_to_number(computer)

    if (human_number - computer_number) % 3 == 1:
        HUMAN_SCORE += 1
        point.config(text='POINT: YOU WIN!')
    elif human_number == computer_number:
        point.config(text='POINT: TIE!')
    else:
        COMPUTER_SCORE += 1
        point.config(text='POINT: BOT WIN!')

    your_score.config(text='YOUR SCORE: ' + str(HUMAN_SCORE))
    bot_score.config(text='BOT SCORE: ' + str(COMPUTER_SCORE))

    your_choice .config(text='YOU: ' + human)
    bot_choice.config(text='BOT: ' + computer)


# Situation when human choose rock
def rock():
    global human_choice, computer_choice

    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)


# Situation when human choose paper
def paper():
    global human_choice, computer_choice

    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)


# Situation when human choose scissors
def scissors():
    global human_choice, computer_choice

    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)


# Create buttons
rock_btn = Button(root, text='ROCK', font=("Courier", 30), padx=127, pady=40, fg='white', bg='blue', command=rock)
rock_btn.place(x=10, y=20)

paper_btn = Button(root, text='PAPER', font=("Courier", 30), padx=115, pady=40, fg='white', bg='blue', command=paper)
paper_btn.place(x=10, y=180)

scissors_btn = Button(root, text='SCISSORS', font=("Courier", 30), padx=80, pady=40, fg='white', bg='blue', command=scissors)
scissors_btn.place(x=10, y=340)

root.mainloop()

import random


def computer_choice(x):
    low = 1
    high = x
    feedback = ''
    print(f'Think about any number between {low} and {high}.')
    while feedback != 'c':
        choice = random.randint(low, high)
        feedback = input(f'Is the number {choice} low(L), high(H) or correct(C): ').lower()
        if feedback == 'l':
            low = choice + 1
        elif feedback == 'h':
            high = choice - 1
    print(f'The computer guessed your number {choice} correctly!')


computer_choice(100)

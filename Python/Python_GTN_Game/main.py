import random
choice = random.choice(range(1, 10))
print('Guess the number from 1 to 9!')
print('You have 3 tries!')
guess = int(input('Guess one: '))
if guess == choice:
    print('Right! Great job!')
else:
    guess = int(input('Wrong! Guess two: '))
    if guess == choice:
        print('Right! Great job!')
    else:
        guess = int(input('Wrong! Guess three: '))
        if guess == choice:
            print('Right! Great job!')
        else:
            print(f'You lose! The number was {choice}!')

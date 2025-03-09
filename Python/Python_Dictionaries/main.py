def choice(name):
    return {'Usain': 1, 'Me': 2, 'Quazy': 3}[name]


print(choice(str(input())))


def number(place):
    return {1: 'Usain', 2: 'Me', 3: 'Quazy'}[place]


print(number(int(input())))

def name(**kwargs):
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(value, end=' ')


name(title='Mr.', first='George', last='Petrov', middle='Ivanov')

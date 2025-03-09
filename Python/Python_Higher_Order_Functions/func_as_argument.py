def up(text):
    return text.upper()


def low(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(up)
hello(low)

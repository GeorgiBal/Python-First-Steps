def add(*args):
    num = 0
    for i in args:
        num += i
    return num


print(add(1, 2, 3, 4, 5))

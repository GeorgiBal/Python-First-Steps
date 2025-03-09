import functools

letters = ["H", "E", "L", "L", "O"]
combine = lambda x, y: x + y
word = functools.reduce(combine, letters)
print(word)

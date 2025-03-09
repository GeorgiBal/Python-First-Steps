import functools

digits = [1, 2, 3, 4, 5]
factorial = lambda x, y: x * y
factorial_digit = functools.reduce(factorial, digits)
print(factorial_digit)

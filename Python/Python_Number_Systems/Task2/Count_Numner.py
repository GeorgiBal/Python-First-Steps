def count_number(number, num):
    counter = 0
    while number > 0:
        digit = int(number) % 10
        if digit == num:
            counter += 1
        number /= 10
    print(counter)


count_number(1111234, 1)

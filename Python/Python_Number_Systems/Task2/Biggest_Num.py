def biggest_num(num):
    big = int(num) % 10
    while num != 0:
        digit = num % 10
        if digit > big:
            big = digit
        num /= 10
    print(int(big))


biggest_num(2691212334)

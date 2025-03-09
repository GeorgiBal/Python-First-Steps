def straight_code(dec):
    binary = ""
    while int(dec) > 0:
        digit = int(dec) % 2
        binary += str(digit)
        dec /= 2

    return binary[::-1]


print(straight_code(58))
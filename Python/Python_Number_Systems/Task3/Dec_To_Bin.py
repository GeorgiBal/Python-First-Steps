def dec_to_bin(dec):
    binary = ""
    while int(dec) > 0:
        digit = int(dec) % 2
        binary += str(digit)
        dec /= 2

    return binary[::-1]


print(dec_to_bin(2))

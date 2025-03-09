def reversed_code(dec):
    binary = ""

    while int(dec) > 0:
        digit = int(dec) % 2
        binary += str(digit)
        dec /= 2

    binary = list(binary[::-1])
    reverse_binary = binary[0]

    for i in range(1, len(binary)):
        if binary[i] == "1":
            reverse_binary += "0"
        elif binary[i] == "0":
            reverse_binary += "1"
    return reverse_binary


print(reversed_code(1258))

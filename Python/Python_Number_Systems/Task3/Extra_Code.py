def extra_code(dec):
    dec = bin(dec)

    dec = dec[2:]
    reverse_binary = dec[0]

    for i in range(1, len(dec)):
        if dec[i] == "1":
            reverse_binary += "0"
        elif dec[i] == "0":
            reverse_binary += "1"

    total = 1
    reverse_binary = reverse_binary[::-1]
    for i in range(len(reverse_binary)):
        total += pow(2, i) * int(reverse_binary[i])
    total = bin(total)
    return total[2:]


print(extra_code(56))

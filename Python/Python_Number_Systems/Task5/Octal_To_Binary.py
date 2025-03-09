def octal_to_binary(num, ns):
    binary = ""
    dec = 0
    num = list(num[::-1])
    if ns == 2:
        for i in range(len(num)):
            dec += pow(8, i) * int(num[i])

        while dec > 0:
            binary += str(dec % 2)
            dec = int(dec/2)

        return binary[::-1]
    elif ns == 8:
        for i in range(len(num)):
            dec += pow(2, i) * int(num[i])

        while dec > 0:
            binary += str(dec % 8)
            dec = int(dec/8)

        return binary[::-1]


print(octal_to_binary("111010", 8))

def ternary_to_dec(num, ns):
    if ns == 3:
        num = int(num)
        ternary = ""
        while num != 0:
            ternary += str(num%3)
            num = int(num/3)
        return ternary[::-1]
    elif ns == 10:
        num = list(num[::-1])
        sum = 0
        for i in range(len(num)):
            sum += pow(3, i) * int(num[i])
        return sum


print(ternary_to_dec("169", 3))

def count_letter_num(num):
    global counter
    num = list(num)
    while num:
        i = len(num) - 1
        if "a" <= num[i] <= "f" or "A" <= num[i] <= "F":
            counter += 1
        num.pop(-1)
        return count_letter_num(num)

    return counter


counter = 0
print(count_letter_num("AcBd2"))

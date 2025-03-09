def find_num(number, num):
    if number == 0:
        return False
    elif number % 10 == num:
        return True
    return find_num(int(number / 10), num)


print(find_num(12345, 6))

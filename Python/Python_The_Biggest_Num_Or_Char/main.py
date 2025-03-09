def the_bigger(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def the_biggest(num1, num2, num3):
    return the_bigger(the_bigger(num1, num2), num3)


print(the_biggest(input(), input(), input()))

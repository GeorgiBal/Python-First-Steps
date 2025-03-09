"""
#Non-Dynamic Way
def successful_div(x, y):
    while x % y == 0:
        x //= y
    return x

def ugly_check(num):
    num = successful_div(num, 2)
    num = successful_div(num, 3)
    num = successful_div(num, 5)

    if num == 1:
        return True
    else:
        return False

def nth_ugly_num(n):
    i = 1
    counter = 1
    while n > counter:
        i += 1
        if ugly_check(i):
            counter += 1

    return i

print(nth_ugly_num(15))
"""

#Dynamic Way

def nth_ugly(n):
    dp_ugly = [0]*n
    dp_ugly[0] = 1

    u2 = u3 = u5 = 0
    multiple_2 = 2
    multiple_3 = 3
    multiple_5 = 5

    for i in range(1, n):
        dp_ugly[i] = min(multiple_2, multiple_3, multiple_5)

        if dp_ugly[i] == multiple_2:
            u2 += 1
            multiple_2 = dp_ugly[u2] * 2

        if dp_ugly[i] == multiple_3:
            u3 += 1
            multiple_3 = dp_ugly[u3] * 3

        if dp_ugly[i] == multiple_5:
            u5 += 1
            multiple_5 = dp_ugly[u5] * 5

    return dp_ugly[n - 1]

print(nth_ugly(15))
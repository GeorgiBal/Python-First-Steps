def even_odd_diff(num):
    global diff
    i = num % 10
    while num > 0:
        if i % 2 == 0:
            diff += 1
        else:
            diff -= 1
        return even_odd_diff(int(num/10))
    return abs(diff)


diff = 0
print(even_odd_diff(99))

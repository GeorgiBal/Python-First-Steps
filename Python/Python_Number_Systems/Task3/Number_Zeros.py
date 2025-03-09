def number_zeros(number):
    counter = 0
    for i in str(number):
        if i == "0":
            counter += 1
    return counter


print(number_zeros(11100000000))

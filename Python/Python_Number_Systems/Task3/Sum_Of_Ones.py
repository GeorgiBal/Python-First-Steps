def sum_of_ones(num):
    counter = 0
    for i in str(num):
        if i == "1":
            counter += 1
    return counter


print(sum_of_ones(10010010))
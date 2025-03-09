def kids_with_candies(candies, extra_candies):
    bulls = []
    max_diff = max(candies)
    for candy in candies:
        if candy + extra_candies >= max_diff:
            bulls.append(True)
        else:
            bulls.append(False)

    return bulls

candies = [2,3,5,1,3]
extra_candies = 3
print(kids_with_candies(candies, extra_candies))
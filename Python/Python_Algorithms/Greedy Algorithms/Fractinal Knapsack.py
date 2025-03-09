weight = [30, 50, 10, 70, 40]
values = [150, 100, 90, 140, 120]
capacity = 150

def fractional_knapsack(weight, values, capacity):
    items = list(range(len(values)))
    ratio = [v//w for v, w in zip(values, weight)]
    items.sort(key=lambda i: ratio[i], reverse=True)

    max_values = 0
    fractions = [0] * len(values)

    for i in items:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_values += values[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity // weight[i]
            max_values += values[i] * capacity // weight[i]

    return max_values

print(fractional_knapsack(weight, values, capacity))
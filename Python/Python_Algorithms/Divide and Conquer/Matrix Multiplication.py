# Could use NumPy library for
def matrix_multiply(x, y):
    result = [([0]* len(x[0])) for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]

    return result

x = [[1, 2],
     [2, 3]]

y = [[2, 3],
     [3, 4]]

result = matrix_multiply(x, y)
for row in result:
    print(row)


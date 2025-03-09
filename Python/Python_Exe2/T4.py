n = input()
l1 = n.split(", ")
l1 = list(map(int, l1))
total = 0
for i in range(len(l1)):
    total += l1[i]


average = total / len(l1)

diff = 0
number = 0
high = 0
for i in range(len(l1)):
    diff = abs(l1[i] - average)
    if high < diff:
        high = diff
        number = l1[i]

print(number)



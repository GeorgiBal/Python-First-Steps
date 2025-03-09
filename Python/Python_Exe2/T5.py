n = input()
l1 = n.split(", ")
l1 = list(map(float, l1))
total = 0
for i in range(len(l1)):
    total += abs(l1[i])
print(total)

n = input()
l1 = n.split(", ")
l1 = list(map(int, l1))
total = 0
for i in range(len(l1)):
    total += l1[i]

print(total / len(l1))

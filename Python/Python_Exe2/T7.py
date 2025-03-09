n = input()
l1 = n.split(", ")
l1 = list(map(int, l1))
num = 0
for i in range(len(l1)):
    if i % 2 == 0:
        num = l1[i]
        l1[i] = l1[i+1]
        l1[i+1] = num


print(*l1, sep=", ")

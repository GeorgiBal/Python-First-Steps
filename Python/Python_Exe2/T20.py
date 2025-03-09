l1 = input().split(" ")
l1 = list(map(float, l1))

for i in range(len(l1)-1):
    if i % 2 != 0:
        l1[i] = (l1[i-1] + l1[i+1])/2

print(*l1, sep=" ")

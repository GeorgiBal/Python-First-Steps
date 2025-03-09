n = int(input())
l1 = input().split(", ")
l2 = input().split(", ")
if len(l1) > n or len(l2) > n:
    print("Not in range")
else:
    l1 = list(map(int, l1))
    l2 = list(map(int, l2))
    l3 = []
    for i in range(n):
        l3.append(l1[i] + l2[i])
    print(*l3, sep=", ")

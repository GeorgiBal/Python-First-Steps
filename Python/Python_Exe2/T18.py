from statistics import mode
n = int(input())
l1 = []
for i in range(n):
    num = input()
    l1.append(num)

print(mode(l1))


n = int(input())
l1 = []
for i in range(n):
    num = int(input())
    l1.append(num)

for i in range(len(l1)):
    if i % 2 == 0:
        print(l1[i] + l1[i+1])
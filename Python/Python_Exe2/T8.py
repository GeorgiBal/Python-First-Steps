n = int(input())
total = 0
l1 = []

for i in range(n):
    num = int(input())
    l1.append(num)
    total += num

average = total/n
high_nums = 0
for i in range(len(l1)):
    if abs(l1[i]) > average:
        high_nums += 1

print(high_nums)

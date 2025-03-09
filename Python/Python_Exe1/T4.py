n = int(input())
m = int(input())

for i in range(m+1):
    if n <= i <= m and i % 2 == 0:
        print(i)

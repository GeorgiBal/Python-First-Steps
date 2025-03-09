n = int(input())
m = int(input())
ln = []
lm = []
for i in range(n):
    num = int(input())
    ln.append(num)
for i in range(m):
    num = int(input())
    lm.append(num)

l3 = ln[::-1] + lm[::-1]
print(*l3, sep=", ")
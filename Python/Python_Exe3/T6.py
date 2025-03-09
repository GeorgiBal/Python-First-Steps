n = input()
l1 = list(n)
char = input()
num = 0
for i in l1:
    if i == char:
        num += 1

print(num)

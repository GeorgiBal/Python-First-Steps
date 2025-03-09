n = input()
l1 = n.split(" ")
for i in l1:
    if len(i) < 3:
        l1.remove(i)

print(*l1, sep=" ")
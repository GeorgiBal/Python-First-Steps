l1 = [0]
l2 = [0]

digit1 = ""
digit2 = ""

for i in l1:
    digit1 += str(i)

for i in l2:
    digit2 += str(i)

rev1 = digit1[::-1]
rev2 = digit2[::-1]

total = int(rev1) + int(rev2)
print(total)

l3 = []
for i in str(total):
    l3.append(int(i))

l3.reverse()
print(l3)


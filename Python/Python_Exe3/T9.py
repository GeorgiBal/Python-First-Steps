n = input()
l1 = []
for i in range(len(n)):
    if n[i].isupper():
        l1.append(n[i].lower())
    elif n[i].islower():
        l1.append(n[i].upper())
    elif n[i] == "?":
        l1.append(".")
    else:
        l1.append(n[i])

print(*l1, sep="")

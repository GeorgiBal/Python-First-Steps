sentence = input()
word = input()
l1 = sentence.split(" ")
for i in l1:
    if word == i.lower():
        l1.remove(i)
l1[0] = l1[0].capitalize()
print(*l1, sep=" ")

l1 = input("мас1 = ").split(" ")
l2 = input("мас2 = ").split(" ")
l3 = input("мас3 = ").split(" ")
dl1 = l1
dl2 = l2
dl3 = l3

l2 = dl1
l3 = dl2
l1 = dl3

print("мас1 =", *l1, sep=" ")
print("мас2 =", *l2, sep=" ")
print("мас1 =", *l3, sep=" ")

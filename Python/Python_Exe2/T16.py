l1 = input().split(" ")
first_element = l1[0]
for i in range(len(l1)-1):
    l1[i] = l1[i+1]

l1[len(l1)-1] = first_element
print(*l1, sep=" ")

n = int(input())
full_list = input().split(", ")
if len(full_list) > n*2:
    print("Not in range")
else:
    l1 = full_list[:n]
    l2 = full_list[n:]
    l3 = l1 + l2[::-1]
    print(*l3, sep=", ")

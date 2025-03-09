def AND(num1, num2):
    print(f"Numbers: {num1}, {num2}")
    print(f"{num1} binary --> {bin(num1)[2:]}")
    print(f"{num2} binary --> {bin(num2)[2:]}")
    list1 = list(str(bin(num1)[2:]))
    list2 = list(str(bin(num2)[2:]))

    list1.reverse()
    list2.reverse()

    size = max(len(list1), len(list2))
    diff = abs(len(list1) - len(list2))

    if len(list1) > len(list2):
        for i in range(diff):
            list2.append("0")
    else:
        for i in range(diff):
            list1.append("0")

    l3 = []
    for i in range(size):
        if list1[i] == "1" and list2[i] == "1":
            l3.append("1")
        else:
            l3.append("0")

    l3.reverse()
    num = ""
    for i in l3:
        num += i

    print("AND operator:")
    print("Binary: " + num)
    num = int(num, 2)
    print("Decimal: " + str(num))
    print()


def NOT(num1):
    print(f"Number: {num1}")
    num = -num1 - 1
    print("NOT operator")
    print("Decimal: " + str(num))
    print()


def OR(num1, num2):
    print(f"Numbers: {num1}, {num2}")
    print(f"{num1} binary --> {bin(num1)[2:]}")
    print(f"{num2} binary --> {bin(num2)[2:]}")
    l1 = list(str(bin(num1)[2:]))
    l2 = list(str(bin(num2)[2:]))

    l1.reverse()
    l2.reverse()

    size = max(len(l1), len(l2))
    diff = abs(len(l1) - len(l2))

    if len(l1) > len(l2):
        for i in range(diff):
            l2.append("0")
    else:
        for i in range(diff):
            l1.append("0")

    l3 = []
    for i in range(size):
        if l1[i] == "1" or l2[i] == "1":
            l3.append("1")
        else:
            l3.append("0")

    l3.reverse()
    num = ""
    for i in l3:
        num += i

    print("OR operator:")
    print("Binary: " + num)
    num = int(num, 2)
    print("Decimal: " + str(num))
    print()


def XOR(num1, num2):
    print(f"Numbers: {num1}, {num2}")
    print(f"{num1} binary --> {bin(num1)[2:]}")
    print(f"{num2} binary --> {bin(num2)[2:]}")
    l1 = list(str(bin(num1)[2:]))
    l2 = list(str(bin(num2)[2:]))

    l1.reverse()
    l2.reverse()

    size = max(len(l1), len(l2))
    diff = abs(len(l1) - len(l2))

    if len(l1) > len(l2):
        for i in range(diff):
            l2.append("0")
    else:
        for i in range(diff):
            l1.append("0")

    l3 = []
    for i in range(size):
        if l1[i] == l2[i]:
            l3.append("0")
        else:
            l3.append("1")

    l3.reverse()
    num = ""
    for i in l3:
        num += i

    print("XOR operator:")
    print("Binary: " + num)
    num = int(num, 2)
    print("Decimal: " + str(num))
    print()


def LEFT_SHIFT(num, shifts):
    print(f"Number: {num}")
    print(f"{num} binary --> {bin(num)[2:]}")
    l1 = list(str(bin(num)[2:]))
    for i in range(shifts):
        l1.insert(len(l1), "0")
    num = ""
    for i in l1:
        num += i

    print("LEFT_SHIFT operator:")
    print("Binary: " + num)
    num = int(num, 2)
    print("Decimal: " + str(num))
    print()


def RIGHT_SHIFT(num, shifts):
    print(f"Number: {num}")
    print(f"{num} binary --> {bin(num)[2:]}")
    l1 = list(str(bin(num)[2:]))
    for i in range(shifts):
        l1.pop()
    num = ""
    for i in l1:
        num += i

    print("RIGHT_SHIFT operator:")
    print("Binary: " + num)
    num = int(num, 2)
    print("Decimal: " + str(num))
    print()


AND(43, 8)
NOT(23)
OR(15, 11)
XOR(5, 3)
LEFT_SHIFT(44, 2)
RIGHT_SHIFT(543, 1)

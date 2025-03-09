n = int(input())
perfect_square = False
for i in range(n):
    if i * i == n:
        perfect_square = True

if perfect_square:
    print("Да")
else:
    print("Не")

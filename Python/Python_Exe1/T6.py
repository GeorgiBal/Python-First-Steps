n = int(input())
even_sum = 0
odd_sum = 0


for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num


print("Сума четни:", even_sum)
print("Сума нечетни:", odd_sum)

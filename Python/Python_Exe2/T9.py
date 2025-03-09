import statistics
n = input()
l1 = n.split(", ")
l1 = list(map(int, l1))
median = statistics.median(l1)
print(median)

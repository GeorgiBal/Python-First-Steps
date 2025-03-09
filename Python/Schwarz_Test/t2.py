import math

r1, h1, r2, h2 = input().split(",")

r1 = float(r1)
h1 = float(h1)
r2 = float(r2)
h2 = float(h2)

vol1 = math.pi * r1**2 * h1 / 1000
vol2 = math.pi * r2**2 * h2 / 1000

result = round(max(vol1, vol2), 2)
print(result)

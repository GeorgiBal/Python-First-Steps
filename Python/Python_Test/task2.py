import math
r1, h1, r2, h2 = input().split(',')
cylinder1 = math.pi*math.pow(int(r1), 2)*int(h1)/1000
cylinder2 = math.pi*math.pow(int(r2), 2)*int(h2)/1000

if cylinder1 > cylinder2:
    print('{:.2f}'.format(cylinder1))
else:
    print('{:.2f}'.format(cylinder2))

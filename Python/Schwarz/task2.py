from datetime import datetime

x = int(input())

while True:
    if 1700 <= x <= 2700:
        break
    else:
        x = int(input("The year must be in the range of 1700-2700: "))

calendar = ""
year = ""
if 1700 <= x <= 1915:
    calendar = "julian"
else:
    calendar = "gregorian"


if calendar == "julian":
    if x % 4 == 0:
        year = "leap"
    else:
        year = "not leap"
else:
    if x % 4 == 0 and x % 100 != 0:
        year = "leap"
    else:
        year = "not leap"

y = int(input())
while True:
    if year == "not leap":
        if 1 <= y <= 365:
            break
        else:
            y = int(input("The day must be in the range of 1-365: "))
    else:
        if 1 <= y <= 366:
            break
        else:
            y = int(input("The day must be in the range of 1-366: "))


day_num = str(y)

day_num.rjust(3 + len(day_num), '0')
year = str(x)

res = datetime.strptime(year + "." + day_num, "%Y.%j").strftime("%d.%m.%Y")

print(str(res))


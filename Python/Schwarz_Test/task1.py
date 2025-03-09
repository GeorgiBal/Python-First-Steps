schedule = input().split(" -> ")
command = input()

while command != "start academy":

    splited_str = command.split(":")
    operation = splited_str[0]
    lesson = splited_str[1]

    if operation == "Add":

        if lesson not in schedule:
            schedule.append(lesson)

    elif operation == "Insert":

        index = int(splited_str[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)

    elif operation == "Remove":

        if lesson in schedule:
            schedule.remove(lesson)

    elif operation == "Swap":

        lesson2 = splited_str[2]
        if lesson in schedule and lesson2 in schedule:
            index1 = schedule.index(lesson)
            index2 = schedule.index(lesson2)
            schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
    command = input()

for i in range(len(schedule)):
    print(f"{i+1}.{schedule[i]}")

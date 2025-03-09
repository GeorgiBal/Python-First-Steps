n = int(input())
students = {}

for i in range(n):
    grades = input().split(', ')
    name = input()

    if name not in students:
        students[name] = {'grades': [], 'average': 0}

    students[name]['grades'].extend(list(map(float, grades)))

sorted_students = []
for name, grade in students.items():
    grades = grade['grades']
    avg_grade = sum(grades) / len(grades)

    if avg_grade >= 4.00:
        grade['average'] = avg_grade
        sorted_students.append((name, avg_grade))

sorted_students.sort(key=lambda x: x[1])

for name, avg_grade in sorted_students:
    print(f"{name} -> {avg_grade:.2f}")

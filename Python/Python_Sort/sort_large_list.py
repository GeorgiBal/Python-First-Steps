students = [("Tim", "F", 12),
            ("John", "A", 15),
            ("Nico", "C", 16),
            ("Alan", "D", 14)]

print("Sorted by students' name")
students.sort()
print(students)

print("Sorted by students' grade")
grade = lambda grades: grades[1]
students.sort(key=grade)
print(students)

print("Sorted by students' age")
age = lambda ages: ages[2]
students.sort(key=age, reverse=True)
print(students)

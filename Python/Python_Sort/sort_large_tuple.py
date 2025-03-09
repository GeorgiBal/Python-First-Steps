students = (("Tim", "F", 12),
            ("John", "A", 15),
            ("Nico", "C", 16),
            ("Alan", "D", 14))

print("Sorted by students' name")
sorted_students = sorted(students)
print(sorted_students)

print("Sorted by students' grade")
grade = lambda grades: grades[1]
sorted_students = sorted(students, key=grade)
print(sorted_students)

print("Sorted by students' age")
age = lambda ages: ages[2]
sorted_students = sorted(students, key=age, reverse=True)
print(sorted_students)

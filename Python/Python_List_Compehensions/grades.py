students = [100, 20, 70, 60, 80, 30, 50]

# to_pass = lambda x: x >= 60
# passed_students = list(filter(to_pass, students))

# passed_students = [i for i in students if i >= 60]

passed_students = [i if i >= 60 else "FAILED" for i in students]

print(passed_students)

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print('Numbers of students: ' + str(len(self.students)))
            return True
        return False

    def get_average_grade(self):
        value = 0
        for person in self.students:
            value += person.get_grade()
        return value/len(self.students)


s1 = Student('Tim', 19, 95)
s2 = Student('Bob', 19, 75)
s3 = Student('Max', 19, 65)

course = Course('Math', 2)

course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())

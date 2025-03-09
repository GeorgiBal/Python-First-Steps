class Room:
    def __init__(self, roomNumber, studentCapacity):
        self.roomNumber = roomNumber
        self.studentCapacity = studentCapacity


class ClassRoom(Room):
    def __init__(self, roomNumber):
        super().__init__(roomNumber, 25)


class PresentationRoom(Room):
    def __init__(self, roomNumber):
        if roomNumber > 10:
            super().__init__(roomNumber, 50)
        else:
            super().__init__(roomNumber, 75)


class Worker:
    def __init__(self, workerId, name):
        self.workerId = workerId
        self.name = name

    def greet(self, student):
        print(f"Good morning{student.name}!")


class Principle(Worker):
    def __init__(self, workerId, name):
        super().__init__(workerId, name)
        self.numOfStudentsYelledAt = 0

    def greet(self, student):
        print(f"Don't run in the hallways, {student.name}")

    def yell(self, student):
        self.numOfStudentsYelledAt += 1
        student.yelledAt = True


class Janitor(Worker):
    def __init__(self, workerId, name):
        super().__init__(workerId, name)
        self.cleanedRooms = []

    def greet(self, student):
        print(f"Don't step on the wet floor, {student.name}")

    def cleanRoom(self, room):
        self.cleanedRooms.append(room)


class Teacher(Worker):
    def __init__(self, workerId, name):
        super().__init__(workerId, name)
        self.roomsTeaching = []

    def greet(self, student):
        print(f"Hello, {student.name}")

    def teach(self, student, room):
        student.room = room
        student.teacher = self
        self.roomsTeaching.append(room)


class Student:
    def __init__(self, name, age, attendsSports=False):
        self.name = name
        self.age = age
        self.room = None
        self.teacher = None
        self.attendsSports = attendsSports
        self.yelledAt = False

    def sport(self):
        if self.attendsSports:
            print("Feels good to be active!")
        else:
            print(":)")

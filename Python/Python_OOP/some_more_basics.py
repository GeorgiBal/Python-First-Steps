class Person:
    number_of_persons = 0

    def __init__(self, name):
        self.name = name
        Person.add_people()

    @classmethod
    def number_of_people(cls):
        return cls.number_of_persons

    @classmethod
    def add_people(cls):
        cls.number_of_persons += 1


p1 = Person('Tim')
p2 = Person('Max')
print(Person.number_of_persons)


class Math:
    @staticmethod
    def add_num(x):
        return x + 5


print(Math.add_num(3))

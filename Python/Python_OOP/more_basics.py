class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    @staticmethod
    def speak():
        print('Meow')

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    @staticmethod
    def speak():
        print('Bark')


p = Pet('Tim', 19)
p.show()

c = Cat('Max', 21, 'blue')
c.show()
c.speak()

d = Dog('Sam', 22)
d.show()
d.speak()

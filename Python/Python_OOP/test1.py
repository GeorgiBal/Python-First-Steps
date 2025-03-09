class Car:

    def turn_on(self):
        print("The car is turned on")
        return self

    def drive(self):
        print("The car is driven")
        return self

    def turn_off(self):
        print("The car is turned off")
        return self


car = Car()
car.turn_on().\
    drive().\
    turn_off()

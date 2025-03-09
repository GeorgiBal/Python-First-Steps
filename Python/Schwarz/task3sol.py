taken_rooms = []
cleaned_rooms = []


class Room:
    def __init__(self, room_number, price_per_night):
        self.room_number = room_number
        self.price_per_night = price_per_night


class Suite(Room):
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)
        self.price_per_night = 50


class Apartment(Room):
    def __init__(self, room_number, price_per_night):
        super(Apartment, self).__init__(room_number, price_per_night)
        if self.room_number > 3:
            self.price_per_night = 150
        else:
            self.price_per_night = 100


class HotelPersonal:
    def __init__(self, workerld, name):
        self.workerld = workerld
        self.name = name

    def greet(self, tourist_name):
        print("Enjoy your stay" + tourist_name)

    def clean(self, room):
        cleaned_rooms.append(room)


class Cleaner(HotelPersonal):

    def __init__(self, workerld, name):
        super().__init__(workerld, name)

    def greet(self, tourist_name):
        print("Enjoy your stay" + tourist_name)


class Receptionist(HotelPersonal):

    def __init__(self, workerld, name):
        super().__init__(workerld, name)

    def greet(self, tourist_name):
        print("Welcome to the hotel" + tourist_name)

    def assign_room(self, tourist, room):
        taken_rooms.append(room)


class Tourist:
    def __init__(self, name, stay_days, is_allinclusive):
        self.name = name
        self.stay_days = stay_days
        self.is_allinclusive = is_allinclusive

    def relax(self):
        if self.is_allinclusive:
            print("Feels good to make fat stacks coding")
        else:
            print(":)")



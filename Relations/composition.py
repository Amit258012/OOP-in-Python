""""
Composition:- one object composed of many instances of other objects

Composition is a design technique in programming that is used to implement has-a relationships.

If House is destroyed then all the room inside it will be destroyed

[House]<0>------>[Rooms] // House consist of Rooms
"""


class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []

    def add_room(self, room_name):
        room = Room(room_name)
        self.rooms.append(room)


house = House("Ram Nivas")
house.add_room("Devr Katti")

print(house.rooms[0].name)  # Output: Devr Katti

from passenger import Passenger


class Hotel:
    def __init__(self):
        self.rooms = dict()

    def __repr__(self):
        return "Hotel rooms: {}".format(self.rooms)

    def reserve_rooms(self, name, room_type, count):
        if room_type in self.rooms:
            if self.rooms[room_type] >= count:
                self.rooms[room_type] -= count
                return Passenger(name, room_type, room_count=count)
            else:
                print(f"Not enough {room_type} rooms available.")
        else:
            print(f"{room_type} rooms are not available in this hotel.")

p = Passenger("aram", 20, 20)
hotel = Hotel()
hotel.rooms = {
    "Single": 5,
    "Double": 10,
    "luxe": 3
}
hotel.reserve_rooms("ara", "Single", 10)
print(hotel)
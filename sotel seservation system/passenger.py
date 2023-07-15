class Passenger:
    def __init__(self, name, room_type, room_count):
        self.name = name
        self.room_type = room_type
        self.room_count = room_count


    def __repr__(self):
        return "Passenger name :{}, room type: {}, room count: {}".format(self.name, self.room_type, self.room_count)





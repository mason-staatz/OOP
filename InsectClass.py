import random


class Insect:
    def __init__(self, w, l):
        self.legs = w
        self.wings = l
        self.miles = 0

    def flight(self):
        self.miles = random.randint(1, 10)

    def get_flight_length(self):
        return self.miles

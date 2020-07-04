from random import randint

class Cube:
    instances = 0
    grains = 0
    def __init__(self, ns=6):
        self.number_of_sides = ns
        self.__class__.instances += 1
        self.__class__.grains += ns

    def roll(self):
        return randint(1, self.number_of_sides)

"""
Pygount
"""


class car:
    def __init__(self, color):
        self.color = color


my_car = car("blue")


def crash(car1, car2):  # pylint: disable=unused-argument
    car1.color = "burnt"


crash(car("red"), my_car)
print("Hello World!")

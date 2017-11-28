from Weel import Weel
from beerbot.Pins import Pins


class BeerBot(object):

    in4 = 15
    in3 = 13
    in2 = 11
    in1 = 7

    in5 = 29
    in6 = 31
    in7 = 33
    in8 = 35

    def __init__(self):
        pins = Pins()
        pins.initBoard()
        self.weel11 = Weel(self.in1, self.in2)
        self.weel12 = Weel(self.in3, self.in4)
        self.weel21 = Weel(self.in5, self.in6)
        self.weel22 = Weel(self.in7, self.in8)


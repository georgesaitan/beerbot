from PrintPins import PrintPins
# from pins.GPIOPins import GPIOPins

from Weel import Weel


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
        self.pins = PrintPins()
        # self.pins = GPIOPins()
        self.pins.initBoard()
        self.weel11 = Weel(self.pins, self.in1, self.in2)
        self.weel12 = Weel(self.pins, self.in3, self.in4)
        self.weel21 = Weel(self.pins, self.in5, self.in6)
        self.weel22 = Weel(self.pins, self.in7, self.in8)

    def forward(self):
        self.weel11.forword()
        self.weel12.forword()
        self.weel21.forword()
        self.weel22.forword()

    def back(self):
        self.weel11.back()
        self.weel12.back()
        self.weel21.back()
        self.weel22.back()

    def right(self):
        self.weel11.back()
        self.weel12.back()
        self.weel21.forword()
        self.weel22.forword()

    def left(self):
        self.weel11.forword()
        self.weel12.forword()
        self.weel21.back()
        self.weel22.back()

    def stop(self):
        self.weel11.stop()
        self.weel12.stop()
        self.weel21.stop()
        self.weel22.stop()


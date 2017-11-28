from beerbot.Pins import Pins


class Weel(object):
    def __init__(self, pin1, pin2):
        pins = Pins()
        self.pin1 = pin1
        self.pin2 = pin2
        pins.initPin(pin1)
        pins.initPin(pin2)

    def forword(self):
        self.pins.setPin(self.pin1,True)
        self.pins.setPin(self.pin2, False)

    def back(self):
        self.pins.setPin(self.pin1, False)
        self.pins.setPin(self.pin2, True)

    def stop(self):
        self.pins.setPin(self.pin1, False)
        self.pins.setPin(self.pin2, False)
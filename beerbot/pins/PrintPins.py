from Pins import Pins

class PrintPins(Pins):

    # _instances = {}
    #
    # def __call__(cls, *args, **kwargs):
    #     if cls not in cls._instances:
    #         cls._instances[cls] = super(Pins, cls).__call__(*args, **kwargs)
    #     return cls._instances[cls]

    def initPin(self, pin):
        print str(pin)

    def setPin(self, pin, value):
        print str(pin) + ':' + str(value)

    def initBoard(self):
        print 'board'

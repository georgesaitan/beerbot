import RPi.GPIO as GPIO
from Pins import Pins


class GPIOPins(Pins):

    # _instances = {}
    #
    # def __call__(cls, *args, **kwargs):
    #     if cls not in cls._instances:
    #         cls._instances[cls] = super(GPIOPins, cls).__call__(*args, **kwargs)
    #     return cls._instances[cls]

    def initPin(self, pin):
        GPIO.setup(pin, GPIO.OUT)

    def setPin(self, pin, value):
        GPIO.output(pin, value)

    def initBoard(self):
        GPIO.setmode(GPIO.BOARD)

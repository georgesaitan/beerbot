import RPi.GPIO as GPIp

class Weel(object):
    def __init__(self, pin1 , pin2):
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        self.pin1 = pin1
        self.pin2 = pin2

    def forword(self):
        GPIO.output(self.pin1, True)
        GPIO.output(self.pin2, False)

    def back(self):
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, True)

    def stop(self):
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, False)
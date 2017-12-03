class GamePad(object):

    def find(self):
        from os import listdir
        from evdev import InputDevice
        # gamepad = InputDevice('/dev/input/event0')
        PATH = '/dev/input/'

        for i in listdir(PATH):
            try:
                gamepad = InputDevice(PATH + i)
                if "Logitech Gamepad F710" in gamepad.name:
                    self.controller = gamepad
            except Exception:
                pass

        # if event.type == 3 and event.code == 16 and event.value == -1:
        #     print "left"
        # elif event.type == 3 and event.code == 16 and event.value == 1:
        #     print "right"
        # elif event.type == 3 and event.code == 17 and event.value == -1:
        #     print "fwd"
        # elif event.type == 3 and event.code == 17 and event.value == 1:
        #     print "back"
        # elif event.type == 3 and event.value == 0:
        #     print "stop"

class Buttons(object):
    def __init__(self, type, code, value):
        self.type = type
        self.code = code
        self.value = value

    def __eq__(self, o):
        return self.type == o.type and self.code == o.code and self.value == o.value

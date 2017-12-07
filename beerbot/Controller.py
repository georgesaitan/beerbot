class GamePad(object):
    PATH = '/dev/input/'


    def find(self):
        from os import listdir
        from evdev import InputDevice

        for i in listdir(GamePad.PATH):
            try:
                gamepad = InputDevice(GamePad.PATH + i)
                if "Logitech Gamepad F710" in gamepad.name:
                    print GamePad.PATH + i
                    self.controller = gamepad
            except Exception:
                pass

    def getButton(self,event):
        button = Button(event.type, event.code, event.value)
        if button == Button.LEFT:
            print "left"
        elif button == Button.RIGHT:
            print "right"
        elif button == Button.FWD:
            print "fwd"
        elif button == Button.BACK:
            print "back"
        elif button == Button.STOP:
            print "stop"

class Button(object):

    def __init__(self, type, code, value):
        self.type = type
        self.code = code
        self.value = value

    def __eq__(self, o):

        return self.type == o.type and self.code == o.code and self.value == o.value
    
class Buttons(object):
    LEFT = Button(3, 16, -1)
    RIGHT = Button(3, 16, 1)
    FWD = Button(3, 17, -1)
    BACK = Button(3, 17, 1)
    STOP = Button(3, None, 0)




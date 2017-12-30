class GamePad(object):
    PATH = '/dev/input/'


    def find(self):
        self.controller = None

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

    @staticmethod
    def getButton(event, bot):
        button = Button(event.type, event.code, event.value)
        if button == Buttons.LEFT:
            print "left"
            bot.left()
        elif button == Buttons.RIGHT:
            print "right"
            bot.right()
        elif button == Buttons.FWD:
            print "fwd"
            bot.forward()
        elif button == Buttons.BACK:
            print "back"
            bot.back()
        elif button in Buttons.STOP:
            print "stop"
            bot.stop()

class Button(object):

    def __init__(self, type, code, value):
        self.type = type
        self.code = code
        self.value = value

    def __eq__(self, o):

        return self.type == o.type and self.code == o.code and self.value == o.value

    def __hash__(self):
        return self.type*100 + self.code*10 + self.code


class Buttons(object):
    LEFT = Button(3, 16, -1)
    RIGHT = Button(3, 16, 1)
    FWD = Button(3, 17, -1)
    BACK = Button(3, 17, 1)
    STOP = {Button(3, 16, 0), Button(3, 17, 0)}




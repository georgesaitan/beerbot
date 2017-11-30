from evdev import InputDevice
from select import select

gamepad = InputDevice('/dev/input/event16')
while True:
    r,w,x = select([gamepad], [], [])
    for event in gamepad.read():
    #     print event
    #     print '\n'
        if event.type == 3 and event.code == 16 and event.value == -1:
            print "left"
        elif event.type == 3 and event.code == 16 and event.value == 1:
            print "right"
        elif event.type == 3 and event.code == 17 and event.value == -1:
            print "fwd"
        elif event.type == 3 and event.code == 17 and event.value == 1:
            print "back"
        elif event.type == 3 and event.value == 0:
            print "stop"


#!/usr/bin/python

from evdev import InputDevice
from select import select
gamepad = InputDevice('/dev/input/event0')


for i in [1,16]:
    print str(i)
    gamepad = InputDevice('/dev/input/event'+str(i))


    print gamepad
    print "\n"
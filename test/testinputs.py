#!/usr/bin/python

from os import listdir
from evdev import InputDevice
PATH = '/dev/input/'

for i in listdir(PATH):
    try:
        gamepad = InputDevice(PATH+i)
        if "Logitech Gamepad F710" in gamepad.name:
            print gamepad.name
    finally:
        pass




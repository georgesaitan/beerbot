#!/usr/bin/python

from os import listdir
from evdev import InputDevice

# from Controller import Button

PATH = '/dev/input/'

for i in listdir(PATH):
    try:
        gamepad = InputDevice(PATH+i)
        if "Logitech Gamepad F710" in gamepad.name:
            print gamepad.name
    except Exception as e:
        pass









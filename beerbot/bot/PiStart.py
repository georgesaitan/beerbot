#!/usr/bin/python
from Controller import GamePad
from Bot import BeerBot

from select import select

#get controller

gamepad = GamePad()
gamepad.find()



#get bot
bot = BeerBot()

#wait for input
if gamepad.controller is not None:
    while True:
        r,w,x = select([gamepad.controller], [], [])
        for event in gamepad.controller.read():
            GamePad.getButton(event, bot)
else:
    print "no controller"

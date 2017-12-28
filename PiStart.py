from Controller import GamePad, Button
from bot.Bot import BeerBot

from select import select

#get controller

controller = GamePad()
controller.find()



#get bot
bot = BeerBot()

#wait for input
while True:
    r,w,x = select([controller.controller], [], [])
    for event in controller.controller.read():
        GamePad.getButton(event, bot)

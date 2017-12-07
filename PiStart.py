from Controller import GamePad
from bot.Bot import BeerBot

#get controller

controller = GamePad()
controller.find()



#get bot
bot = BeerBot()
bot.forword()
bot.left()
# bot.right()
# bot.back()

#wait for input
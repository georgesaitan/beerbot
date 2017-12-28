from bot.Bot import BeerBot
from bot.Controller import GamePad

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
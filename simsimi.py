import telegram
import requests
import logging

from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

TOKEN = "926073780:AAFDut6-uP8tW5yZDrPTE8uYnpN8hHExh2Q"
SimsimiKey = "yHLj8blvWA3IZ3HC15LIvaD+BuBm/GazB5ziRSTI"

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def SimSimi(bot, update):
	message = update.effective_message
	thetext = message.text
	try:
		URL = "http://sandbox.api.simsimi.com/request.p?key={}&lc=id&ft=1.0&text={}".format(SimsimiKey, thetext)
		r = requests.get(url = URL)
		data = r.json()
		if data['result'] == 509:
			text = data['msg']
		else:
			text = data['response']
		update.effective_message.reply_text(text)
	except:
		update.effective_message.reply_text("Error!")

simsimi_handler = MessageHandler(Filters.private, Filters.group, SimSimi)
"""
For only private chat response, use Filters.private
For any text exclude image caption or other, use Filters.text
For only private and text only, use like this (Filters.private | Filters.text)
For more info and any filters, see http://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.filters.html#module-telegram.ext.filters
"""

dispatcher.add_handler(simsimi_handler)

__log__ = logging.getLogger()
__log__.warning("Running bot success!")
updater.start_polling()

from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from config import API_TOKEN
from handlers.commands import start
from handlers.messages import image
from handlers.messages import invalid

updater = Updater(API_TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start.handle)
dispatcher.add_handler(start_handler)

image_handler = MessageHandler(Filters.photo, image.handle)
dispatcher.add_handler(image_handler)

unknown_handler = MessageHandler(Filters.all, invalid.handle)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()

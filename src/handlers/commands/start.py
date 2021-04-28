from telegram import Update
from telegram.ext import CallbackContext

from asset_loader import AssetLoader
from send_action import send_typing_action
from send_action import send_upload_photo_action

loader = AssetLoader()

start_message = loader.load_text('start_message.txt')


@send_typing_action
def send_text(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(start_message)


demo_image_caption = loader.load_text('demo_image_caption.txt')


@send_upload_photo_action
def send_photo(update: Update, context: CallbackContext) -> None:
    photo = loader.load_image('start.jpg')
    update.message.reply_photo(photo, caption=demo_image_caption)


def handle(update: Update, context: CallbackContext) -> None:
    send_text(update, context)
    send_photo(update, context)

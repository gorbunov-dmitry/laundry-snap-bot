from telegram import Update
from telegram.ext import CallbackContext

from asset_loader import AssetLoader
from send_action import send_typing_action

loader = AssetLoader()
invalid_type_message = loader.load_text('invalid_type_message.txt')


@send_typing_action
def handle(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(invalid_type_message)

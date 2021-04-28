import os

from telegram import Update
from telegram.ext import CallbackContext

from send_action import send_typing_action
from labels_recognizer import LabelsRecognizer

recognizer = LabelsRecognizer()


@send_typing_action
def handle(update: Update, context: CallbackContext) -> None:
    # list of photos of different sizes (last is the biggest)
    image = update.message.effective_attachment[-1].get_file()
    path = image.download()
    labels = recognizer.get_labels(path)
    message = '\n'.join(labels)
    update.message.reply_text(message)
    os.remove(path)

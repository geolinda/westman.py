import random

from core import bot
from config import CONFESSION, PERSON, CONTENT


def _video():
    @bot.message_handler(content_types=['video'])
    def __video(message):
        bot.reply_to(message, "<b>Video Received</b>", parse_mode='HTML')
        content = f"<b>{random.choice(PERSON)} {random.choice(CONTENT)}.</b>"
        bot.forward_message(CONFESSION, message.from_user.id, message.message_id)
        reply = "<b>Video has been sent to the confession! Check the channel</b>"
        bot.reply_to(message, reply, parse_mode='HTML')
    pass

import logging
from telegram import Bot


class WelcomeBot(Bot):

    def __init__(self, token):
        super().__init__(token=token)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("Initializing the bot ...")

    def reply(self, update, text, *args, **kwargs):
        self.send_message(chat_id=update.message.chat_id, text=text, *args, **kwargs)

    def action(self, update, action):
        self.send_chat_action(chat_id=update.message.chat_id, action=action)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from bot import WelcomeBot
from commands import *

TOKEN = ""

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
    logging.getLogger(WelcomeBot.__name__).setLevel(logging.DEBUG)

    updater = Updater(bot=WelcomeBot(TOKEN))
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', cmd_start))
    dispatcher.add_handler(CommandHandler('invitelink', invitelink))
    dispatcher.add_handler(CommandHandler('github', github))
    dispatcher.add_handler(CommandHandler('twitter', twitter))
    dispatcher.add_handler(CommandHandler('facebook', facebook))
    dispatcher.add_handler(CommandHandler('youtube', youtube))
    dispatcher.add_handler(CommandHandler('help', cmd_help))
    dispatcher.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome))
    updater.start_polling()

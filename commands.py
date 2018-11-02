from datetime import datetime
import telegram
from telegram import ChatAction
from time import sleep
from emoji import emojize


def cmd_start(bot, update):
    bot.action(update, ChatAction.TYPING)
    sleep(0.2)
    bot.reply(
        update, "I am bot made for Mozilla Delhi Open Community, Please talk to me")


def invitelink(bot, update):
    bot.action(update, ChatAction.TYPING)
    sleep(0.2)
    bot.reply(update, text="[https://t.me/mozilladelhi](https://t.me/mozilladelhi)",
              parse_mode=telegram.ParseMode.MARKDOWN)


def github(bot, update):
    bot.action(update, ChatAction.TYPING)
    sleep(0.2)
    bot.reply(update, text="[https://github.com/MozillaDelhiOpenCommunity](https://github.com/MozillaDelhiOpenCommunity)",
              parse_mode=telegram.ParseMode.MARKDOWN)


def twitter(bot, update):
    bot.action(update, ChatAction.TYPING)
    sleep(0.2)
    bot.reply(update, text="[https://twitter.com/mozilladelhioc](https://twitter.com/mozilladelhioc)",
              parse_mode=telegram.ParseMode.MARKDOWN)


def facebook(bot, update):
    bot.action(update, ChatAction.TYPING)
    sleep(0.2)
    bot.reply(update, text="[https://www.facebook.com/mozilladelhi/](https://www.facebook.com/mozilladelhi/)",
              parse_mode=telegram.ParseMode.MARKDOWN)


def youtube(bot, update):
    bot.action(update, ChatAction.TYPING)
    sleep(0.2)
    bot.reply(update, text="[https://www.youtube.com/channel/UCJoFnsWVHmuppJJBq3b65Eg](https://www.youtube.com/channel/UCJoFnsWVHmuppJJBq3b65Eg)",
              parse_mode=telegram.ParseMode.MARKDOWN)


def welcome(bot, update):
    bot.action(update, ChatAction.TYPING)
    sleep(0.2)
    message = "Welcome "
    for i in update.message.new_chat_members:
        if i.username != None or "":
            message += "@" + i.username
        else:
            message += i.first_name
        message += emojize("! :tada:", use_aliases=True) + ", please introduce yourself. we are very glad to have you with us on this journey into open source!\
         We will also be there for you at all times to help you with actual problems. " + emojize(":grinning:", use_aliases=True)\
            + "\nPlease visit [Mozilla Delhi Official Wiki](http://wiki.mozilla.org/India/Delhi) for more information about us and [Communication Guidelines](https://www.mozilla.org/en-US/about/governance/policies/participation/) in order to maintain group decorum."
        bot.reply(update, message, parse_mode=telegram.ParseMode.MARKDOWN)


def cmd_help(bot, update, chat=None):
    bot.action(update, ChatAction.TYPING)
    sleep(0.2)
    bot.reply(update, """
Hello! This bot welcomes you on the telegram!
Here's the commands:
- /invitelink - to get an invite link for the Mozilla Delhi Open Community
- /github - to get Mozilla Delhi Open Community github link
- /twitter  - to get Mozilla Delhi Open Community twitter link
- /facebook - to get link of Mozilla Delhi Open Community facebook page
- /youtube - to get link of Mozilla Delhi Open Community youtube channel
- /help - view help text
This bot is being worked on, so it may break sometimes. Contact @vaibhavsingh97 \
or open issue [here](https://github.com/MozillaDelhiOpenCommunity/Telegram-bot/issues).
""", parse_mode=telegram.ParseMode.MARKDOWN)

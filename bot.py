import telebot
import config



bot = telebot.TeleBot(config.TOKEN)


# always the last
bot.polling()
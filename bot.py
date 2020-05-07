import telebot
import config
import menu
import money

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    msg = 'Hallo, nice to meet you'
    msg_out = bot.send_message(message.chat.id, msg)
    menu.main_menu(bot, message.chat.id)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text == 'Курсы валют':
        menu.money_menu(bot,message.chat.id)
    elif message.text == 'Доллар':
        usd_in = money.usd_in(bot,message.chat.id)
        usd_out = money.usd_out(bot, message.chat.id)
    elif message.text == 'Евро':
        eur_in = money.eur_in(bot,message.chat.id)
        eur_out = money.eur_out(bot, message.chat.id)
    elif message.text == 'Российский рубль':
        rub_in = money.rub_in(bot,message.chat.id)
        rub_out = money.rub_out(bot,message.chat.id)
    elif message.text == 'Злотый':
        zl_in = money.zl_in(bot, message.chat.id)
        zl_out = money.zl_out(bot,message.chat.id)
    elif message.text == 'Юань':
        un_in = money.un_in(bot, message.chat.id)
        un_out = money.un_out(bot,message.chat.id)

# always the last
bot.polling()
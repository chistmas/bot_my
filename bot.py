import config
import telebot
import menu
import greetings

from datetime import datetime

bot = telebot.TeleBot(config.TOKEN)
message_text=''
recipient_id=''

@bot.message_handler(commands=['start'])
def start_handler(message):
    msg = 'Hallo, nice to meet you'
    msg_out = bot.send_message(message.chat.id, msg)
    menu.main_menu(bot, message.chat.id)
    bot.send_sticker(message.chat.id,
                     'CAACAgIAAxkBAALkol7SyB5mKbDNttoXDpNTD9zihqqaAAK4AAPA-wgAAU2SSZjfsZSOGQQ')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text == 'Hello':
        hello_out=greetings.hello_out(bot, message.chat.id)
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGmdgXD9IAQdmC9xsEuaei6XMWSfbbgAC9QADe04qEEI1AAFASlpvZh4E')
    elif message.text == 'How are you?':
        hello_out = greetings.how_out(bot, message.chat.id)
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGmlgXEARqf8ZbQEBYBYAAcq8u81INxMAAhYCAALSxmEPqfUh5GhpX1EeBA')
    elif message.text == 'You are cute':
        hello_out = greetings.cute_out(bot, message.chat.id)
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGmtgXEDM7Sg3Gu6eN8S0o3SbQ-n1wwACkwADE2MxBzpVc-VYZqd6HgQ')
    elif message.text == 'Lol':
        hello_out = greetings.lol_out(bot, message.chat.id)
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGm9gXEEuEqJMA1HFkynenVnYssS3rgACSgADYmSaJFnWvDC0YiAHHgQ')
    elif message.text == 'Send message':
        msg='Enter message'
        msg_out = bot.send_message(message.chat.id, msg)
        bot.register_next_step_handler(msg_out, ask_who)
    else:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGpFgXFtHscdGzzVeKp7UIh-kVr6aMgACugADwPsIAAGSbw-9i6NJSx4E')

def ask_who(message):
    mes=message.text
    if mes == '/Cancel' or '/cancel':
        msg = 'Sending canceled'
        msg_out = bot.send_message(message.chat.id, msg)
    else:
        message_text=mes
        msg_out = 'Enter recipient'
        bot.register_next_step_handler(msg_out, ask_code)

def ask_code(message):
    mes=message.text
    if mes == '/Cancel' or '/cancel':
        msg = 'Sending canceled'
        msg_out = bot.send_message(message.chat.id, msg)
    else:
        recipient_id=mes
        msg_out = 'Enter code'
        bot.register_next_step_handler(msg_out, send_message)

def send_message(message):
    mes = message.text
    if mes == '/Cancel' or '/cancel':
        msg = 'Sending canceled'
        msg_out = bot.send_message(message.chat.id, msg)
    else:
        msg_out = message.chat.id
        bot.register_next_step_handler(msg_out, send_message)

# always the last
bot.polling()
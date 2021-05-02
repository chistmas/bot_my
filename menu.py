import telebot
import json

def main_menu(bot, chat_id):
    main_menu_buttons = telebot.types.ReplyKeyboardMarkup(row_width=1,
                                                  resize_keyboard=True)

    hello_button = telebot.types.KeyboardButton('Hello')
    how_button = telebot.types.KeyboardButton('How are you?')
    cute_button = telebot.types.KeyboardButton('You are cute')
    lol_button = telebot.types.KeyboardButton('Lol')
    new_button=telebot.types.KeyboardButton('Send message')

    main_menu_buttons.add(hello_button, how_button, cute_button,
                          lol_button, new_button)
    bot.send_message(chat_id, 'XD',
                     reply_markup=main_menu_buttons)


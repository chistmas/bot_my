from telebot import types

def main_menu(bot, chat_id):
    main_menu_buttons = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard = True)

    currency_button = types.KeyboardButton('Курсы валют')
    payments_button = types.KeyboardButton('Платежи')
    cards_button = types.KeyboardButton('Мои карты')
    new_card_button = types.KeyboardButton('Новая карта')

    main_menu_buttons.add(currency_button, payments_button, cards_button, new_card_button)

    bot.send_message(chat_id,'Выберите операцию', reply_markup = main_menu_buttons)

def money_menu(bot, chat_id):
    money_menu_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    usd_button = types.KeyboardButton('Доллар')
    euro_button= types.KeyboardButton('Евро')
    rubl_button = types.KeyboardButton('Российский рубль')
    zloty_button = types.KeyboardButton('Злотый')
    uan_button = types.KeyboardButton('Юань')
    main_menu_button = types.KeyboardButton('Гланое меню')


    money_menu_buttons.add(usd_button,euro_button,rubl_button,zloty_button,uan_button,main_menu_button)

    bot.send_message(chat_id, 'Выберите валюту', reply_markup=money_menu_buttons)
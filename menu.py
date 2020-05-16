from telebot import types
import json


def money_menu(bot, chat_id):
    money_menu_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    usd_button = types.KeyboardButton('Dollar')
    euro_button= types.KeyboardButton('Euro')
    rubl_button = types.KeyboardButton('Russian ruble')
    zloty_button = types.KeyboardButton('Zloty')
    uan_button = types.KeyboardButton('Yuan')
    main_menu_button = types.KeyboardButton('Main menu')


    money_menu_buttons.add(usd_button,euro_button,rubl_button,zloty_button,uan_button,main_menu_button)

    bot.send_message(chat_id, 'Chose curency', reply_markup=money_menu_buttons)

def main_menu(bot, chat_id):
    main_menu_buttons = types.ReplyKeyboardMarkup(row_width=1,
                                                  resize_keyboard=True)
    
    currency_button = types.KeyboardButton('Exchange rates')
    payment_button = types.KeyboardButton('Payments')
    my_cards_button = types.KeyboardButton('My cards')
    new_card_button = types.KeyboardButton('New card')
    
    main_menu_buttons.add(currency_button, payment_button, my_cards_button,
                          new_card_button)
    bot.send_message(chat_id, 'Choose operation', 
                     reply_markup=main_menu_buttons)
    
def payment_menu(bot, chat_id):
    payment_menu_buttons = types.ReplyKeyboardMarkup(row_width=1,
                                                  resize_keyboard=True)
    
    mobile = types.KeyboardButton('Mobile phone')
    internet = types.KeyboardButton('The Internet')
    back = types.KeyboardButton('Main menu')
    
    payment_menu_buttons.add(mobile, internet, back)
    bot.send_message(chat_id, 'Choose a payment', 
                     reply_markup=payment_menu_buttons)

def card_menu(bot, chat_id, card_sum = 0):
    payment_menu_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    file_client = f'.\\storage\\{chat_id}.json'
    with open(file_client, 'r') as file:
        client = json.load(file)
    cards = client['cards']
    for item in cards.items():
        if  int(item[1]['amount'])>=card_sum:
            tmp_card = types.KeyboardButton(f"{item[0]}: {item[1]['amount']} {item[1]['currency']}")
            payment_menu_buttons.add(tmp_card)
    main_menu_button = types.KeyboardButton('Main menu')
    payment_menu_buttons.add(main_menu_button)

    msg_out = bot.send_message(chat_id, 'Сhoose a card with which you will pay', reply_markup=payment_menu_buttons)
    return msg_out

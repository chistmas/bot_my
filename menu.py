from telebot import types
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
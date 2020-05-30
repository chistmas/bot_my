import telebot
import config
import menu
import money
import card
import a
from datetime import datetime

bot = telebot.TeleBot(config.TOKEN)

user_payment = {}


class Payment:
    def __init__(self, telegram_id, payment_type):
        self.telegram_id = telegram_id
        self.payment_type = payment_type
        self.payment_detail = ''
        self.payment_sum = 0.0
        self.payment_card = ''
        self.payment_date = ''


@bot.message_handler(commands=['start'])
def start_handler(message):
    msg = 'Hallo, nice to meet you'
    msg_out = bot.send_message(message.chat.id, msg)
    menu.main_menu(bot, message.chat.id)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text == 'Exchange rates':
        menu.money_menu(bot, message.chat.id)
    elif message.text == 'Dollar':
        usd_in = money.usd_in(bot, message.chat.id)
        usd_out = money.usd_out(bot, message.chat.id)
    elif message.text == 'Euro':
        eur_in = money.eur_in(bot, message.chat.id)
        eur_out = money.eur_out(bot, message.chat.id)
    elif message.text == 'Russian ruble':
        rub_in = money.rub_in(bot, message.chat.id)
        rub_out = money.rub_out(bot, message.chat.id)
    elif message.text == 'Zloty':
        zl_in = money.zl_in(bot, message.chat.id)
        zl_out = money.zl_out(bot, message.chat.id)
    elif message.text == 'Uan':
        un_in = money.un_in(bot, message.chat.id)
        un_out = money.un_out(bot, message.chat.id)

    elif message.text == 'New card':
        new_card = card.new_card(message.chat.id)
        msg = f"Card was successfuly created\n"
        msg += f"Card number is: {new_card['card_num']}"
        msg_out = bot.send_message(message.chat.id, msg)

    elif message.text == 'My cards':
        msg = ''
        cards = card.get_cards(message.chat.id)
        for item in cards.items():
            msg += f"{item[0]} \ Balance is: {item[1]['amount']}"
            msg += f"{item[1]['currency']}\n"
        msg_out = bot.send_message(message.chat.id, msg)

    elif message.text == 'Payments':
        menu.payment_menu(bot, message.chat.id)

    elif message.text == 'My payments':
        msg = ''
        payments = card.get_pay(message.chat.id)
        for item in payments.items():
            msg += f"{item[0]} \nCard: {item[1]['card']}\nAmount: "
            msg += f" {item[1]['amount']}\nType of: {item[1]['type_of']}"
            msg += f"\nAccount number: {item[1]['details']}\n\n"
        msg_out = bot.send_message(message.chat.id, msg)


    elif message.text == 'Mobile phone':
        msg = "Enter your phone number"
        telegram_id = message.chat.id
        payment_type = message.text
        payment = Payment(telegram_id, payment_type)
        user_payment[telegram_id] = payment

        msg_out = bot.send_message(message.chat.id, msg)
        bot.register_next_step_handler(msg_out, ask_phone_number)

    elif message.text == 'The Internet':
        msg = "Enter your payment account number"
        telegram_id = message.chat.id
        payment_type = message.text
        payment = Payment(telegram_id, payment_type)
        user_payment[telegram_id] = payment

        msg_out = bot.send_message(message.chat.id, msg)
        bot.register_next_step_handler(msg_out, ask_internet_number)


    elif message.text == 'Transfer from card to card':
        msg = 'Enter amount you want to transfer'
        telegram_id = message.chat.id
        payment_type = message.text
        payment = Payment(telegram_id, payment_type)
        user_payment[telegram_id] = payment
        msg_out = bot.send_message(message.chat.id, msg)
        bot.register_next_step_handler(msg_out, ask_card_sum)

    elif message.text == 'Main menu':
        menu.main_menu(bot, message.chat.id)

    elif message.text == "Internet history":
        a.ris_in(message.chat.id)
        bot.send_photo(message.chat.id, photo=open('to.png', 'rb'))

    elif message.text == "Phone history":
        a.ris_ph(message.chat.id)
        bot.send_photo(message.chat.id, photo=open('to.png', 'rb'))

    else:
        msg = "This is not one of my functions, do you want try one more time?"
        msg_out = bot.send_message(message.chat.id, msg)


def ask_phone_number(message):
    phone_number = message.text
    if not phone_number.isdigit():
        msg = "Wrong format"
        msg_out = bot.send_message(message.chat.id, msg)
        bot.register_next_step_handler(msg_out, ask_phone_number)
        return

    telegram_id = message.chat.id
    payment = user_payment[telegram_id]
    payment.payment_detail = phone_number

    msg = "Enter amount"
    msg_out = bot.send_message(message.chat.id, msg)
    bot.register_next_step_handler(msg_out, ask_phone_sum)


def ask_phone_sum(message):
    phone_sum = message.text
    if not phone_sum.isdigit():
        msg = "Amount must be a number"
        msg_out = bot.send_message(message.chat.id, msg)
        bot.register_next_step_handler(msg_out, ask_phone_sum)
        return

    telegram_id = message.chat.id
    payment = user_payment[telegram_id]
    payment.payment_sum = phone_sum
    msg_out = menu.card_menu(bot, message.chat.id)
    bot.register_next_step_handler(msg_out, ask_card_num2)


def ask_internet_number(message):
    internet_number = message.text
    if not internet_number.isdigit():
        msg = "Wrong format"
        msg_out = bot.send_message(message.chat.id, msg)
        bot.register_next_step_handler(msg_out, ask_internet_number)
        return

    telegram_id = message.chat.id
    payment = user_payment[telegram_id]
    payment.payment_detail = internet_number

    msg = "Enter amount"
    msg_out = bot.send_message(message.chat.id, msg)
    bot.register_next_step_handler(msg_out, ask_internet_sum)


def ask_internet_sum(message):
    internet_sum = message.text
    if not internet_sum.isdigit():
        msg = "Amount must be a number"
        msg_out = bot.send_message(message.chat.id, msg)
        bot.register_next_step_handler(msg_out, ask_internet_sum)
        return

    telegram_id = message.chat.id
    payment = user_payment[telegram_id]
    payment.payment_sum = internet_sum
    msg_out = menu.card_menu(bot, message.chat.id)
    bot.register_next_step_handler(msg_out, ask_card_num)


def ask_card_num(message):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
    telegram_id = message.chat.id
    payment = user_payment[telegram_id]

    message.text.find(':')
    payment_card = message.text[0: message.text.find(':')]
    payment.payment_card = payment_card
    payment.payment_date = date_time
    card.subtracting_from_card(bot, telegram_id, payment.payment_card, int(payment.payment_sum))
    # funcc that draws money
    card.save(telegram_id, payment.payment_card, int(payment.payment_sum), ['internet', payment.payment_detail])
    msg = f"Thanks!\nUser: {payment.telegram_id}\n{payment.payment_type}:\n"
    msg += f"{payment.payment_detail} \n{payment.payment_sum}\n{payment.payment_date}"
    msg_out = bot.send_message(message.chat.id, msg)


def ask_card_num2(message):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
    telegram_id = message.chat.id
    payment = user_payment[telegram_id]

    message.text.find(':')
    payment_card = message.text[0: message.text.find(':')]
    payment.payment_card = payment_card
    payment.payment_date = date_time
    card.subtracting_from_card(bot, telegram_id, payment.payment_card, int(payment.payment_sum))
    # funcc that draws money
    card.save(telegram_id, payment.payment_card, int(payment.payment_sum), ['phone', payment.payment_detail])
    msg = f"Thanks!\nUser: {payment.telegram_id}\n{payment.payment_type}:\n"
    msg += f"{payment.payment_detail} \n{payment.payment_sum}\n{payment.payment_date}"
    msg_out = bot.send_message(message.chat.id, msg)


def ask_card_sum(message):
    card_sum = message.text
    if not card_sum.isdigit():
        msg = "Amount must be a number"
        msg_out = bot.send_message(message.chat.id, msg)
        bot.register_next_step_handler(msg_out, ask_card_sum)
        return

    telegram_id = message.chat.id
    payment = user_payment[telegram_id]
    payment.payment_amount = card_sum

    msg = 'Сhoose a card from which you want to transfer money'
    bot.send_message(message.chat.id, msg)

    msg_out = menu.card_menu(bot, message.chat.id, int(payment.payment_amount))
    bot.register_next_step_handler(msg_out, ask_card)


def ask_card(message):
    telegram_id = message.chat.id
    payment = user_payment[telegram_id]

    message.text.find(':')
    payment_card = message.text[0: message.text.find(':')]
    payment.payment_card = payment_card

    card.subtracting_from_card(bot, telegram_id, payment_card, int(payment.payment_amount))

    msg = 'Сhoose a card on which you want to transfer money'
    msg_out = bot.send_message(message.chat.id, msg)
    bot.register_next_step_handler(msg_out, ask_card_adding)


def ask_card_adding(message):
    telegram_id = message.chat.id
    payment = user_payment[telegram_id]

    message.text.find(':')
    payment_card = message.text[0: message.text.find(':')]
    payment.payment_card = payment_card
    card.subtracting_from_card(bot, telegram_id, payment_card, -int(payment.payment_amount))

    msg = f"Thanks!\nUser: {payment.telegram_id}\n{payment.payment_type}:\n"
    msg += f"Sum is {payment.payment_amount}"
    msg_out = bot.send_message(message.chat.id, msg)


# always the last
bot.polling()
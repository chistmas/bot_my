
from telebot import types
import json
import requests as res

response = res.get('https://belarusbank.by/api/kursExchange?city=Минск')
curs = json.loads(response.text)


def usd_in(bot, chat_id):
    usd = curs[0]
    usd_in = usd['USD_in']
    msg = f'Bank byes: {usd_in}'
    msg_out = bot.send_message(chat_id, msg)
    return msg_out

def usd_out(bot, chat_id):
    usd = curs[0]
    usd_out = usd['USD_out']
    msg = f'Bank sells: {usd_out}'
    msg_out = bot.send_message(chat_id, msg)
    return msg_out

def eur_in(bot, chat_id):
    eur = curs[0]
    eur_in = eur['EUR_in']
    msg = f'Bank byes: {eur_in}'
    msg_out = bot.send_message(chat_id, msg)
    return msg_out

def eur_out(bot, chat_id):
    eur = curs[0]
    eur_out = eur['EUR_out']
    msg = f'Bank sells: {eur_out}'
    msg_out = bot.send_message(chat_id, msg)
    return msg_out

def rub_in(bot, chat_id):
    rub = curs[0]
    rub_in = rub['RUB_in']
    msg = f'Bank byes: {rub_in}'
    msg_out = bot.send_message(chat_id, msg)
    return msg_out

def rub_out(bot, chat_id):
    rub = curs[0]
    rub_out = rub['RUB_out']
    msg = f'Bank sells: {rub_out}'
    msg_out = bot.send_message(chat_id, msg)
    return msg_out

def zl_in(bot, chat_id):
    zl = curs[0]
    zl_in = zl['PLN_in']
    msg = f'Bank byes: {zl_in}'
    msg_out = bot.send_message(chat_id, msg)
    return msg_out

def zl_out(bot, chat_id):
    zl = curs[0]
    zl_out = zl['PLN_out']
    msg = f'Bank sells: {zl_out}'
    msg_out = bot.send_message(chat_id, msg)
    return msg_out

def un_in(bot, chat_id):
    un = curs[0]
    un_in = un['UAH_in']
    msg = f'Bank byes: {un_in}'
    msg_out = bot.send_message(chat_id, msg)
    return msg_out


def un_out(bot, chat_id):
    un = curs[0]
    un_out = un['UAH_out']
    msg = f'bank sells: {un_out}'
    msg_out = bot.send_message(chat_id, msg)
    return msg_out

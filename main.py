# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 04:17:03 2024

@author: Sherzodbek

Telegrambotni ishga tushurish uchun
pip install pyTelegramBotAPI
"""

from kril_words import to_cyrillic, to_latin
import telebot

TOKEN = '7824751879:AAGuQNuwkugE_ojELbszbC04ryWb9nfOMGc'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "@Krill_laotin_tarjimon_bot ga xush kelibsiz!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    res = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, res(msg))



bot.polling()

    
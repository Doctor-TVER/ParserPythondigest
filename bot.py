import telebot
from telebot import apihelper
import time
import runpy

TOKEN = '5416297795:AAFyTEIdGozxjvaxbNeP_ghj_RQkZmEHpcw'

proxies = {
    'http': 'http://91.249.134.148:80',
    'https': 'http://91.249.134.148:80',
}

apihelper.proxy = proxies

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет!')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Бот умеет получать актуальный список книг о программировании')


@bot.message_handler(commands=['new'])
def new(message):
    bot.reply_to(message, runpy.run_module(mod_name="parser"))


@bot.message_handler(commands=['file'])
def get_file(message):
    print('зашел')
    # Передать файл со списком книг с диска
    with open('result.txt', 'r', encoding='utf-8') as data:
        bot.send_document(message.chat.id, data)

bot.polling()
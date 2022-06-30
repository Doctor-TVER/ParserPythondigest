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


# Обработка команд
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Бот умеет получать актуальный список книг о программировании')


# Команда в параметром
@bot.message_handler(commands=['new'])
def new(message):
    bot.reply_to(message, runpy.run_module(mod_name="parser"))


# Команда администратора
# @bot.message_handler(commands=['admin'], func=lambda message: message.from_user.username == 'DanteOnline')
# def admin(message):
#     print(message)
#     info = os.name
#     bot.reply_to(message, info)
#
#
# @bot.message_handler(commands=['admin2'])
# def admin2(message):
#     if message.from_user.username == 'DanteOnline':
#         info = os.name
#         bot.reply_to(message, info)
#     else:
#         bot.reply_to(message, 'Метод недоступен, нет прав')


# @bot.message_handler(commands=['restart'])
# def restart_server(message):
#     # выполнить команду операционки из python
#     # os.system('notepad')
#     bot.reply_to(message, 'ура!')


@bot.message_handler(commands=['file'])
def get_file(message):
    print('зашел')
    # Передать какой то файл который есть на диске
    with open('result.txt', 'r', encoding='utf-8') as data:
        bot.send_document(message.chat.id, data)



# @bot.message_handler(content_types=['text'])
# def reverse_text(message):
#     if 'плохой' in message.text.lower():
#         bot.reply_to(message, 'В тексте слово плохой')
#         return
#     text = message.text[::-1]
#     bot.reply_to(message, text)
#
#
# @bot.message_handler(content_types=['sticker'])
# def send_sticker(message):
#     FILE_ID = 'CAADAgADPQMAAsSraAsqUO_V6idDdBYE'
#     bot.send_sticker(message.chat.id, FILE_ID)


bot.polling()
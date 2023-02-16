import time
import telebot
from main import news_list
from main import message_form

API_KEY = ''
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Start'])
def send_check(message):
    if message.text == '/Start':
        bot.send_message(message.chat.id, message_form)

        while True:
            post_text = news_list
            iter_ = news_list['news']

            if post_text['news'] != iter_:
                bot.send_message(message.chat.id, message_form)
                time.sleep(1800)
    else:
        bot.send_message(message.chat.id, 'Enter /Start')


bot.polling()

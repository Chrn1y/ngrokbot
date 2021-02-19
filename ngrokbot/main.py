import telebot
from settings import TG_BOT_TOKEN, KILL_CMD
from ngrokfuncs import get_ngrok_url
import subprocess
import os
import signal

bot = telebot.TeleBot(TG_BOT_TOKEN)


@bot.message_handler(commands=['url'])
def url_ngrok(message: telebot.types.Message):
    ngrok_url = get_ngrok_url()
    bot.send_message(message.chat.id, ngrok_url)


# @bot.message_handler(commands=['start'])
# def start_port_ngrok(message: telebot.types.Message):
#     os.system(KILL_CMD)
#     args = message.text.split()[1::]
#     args.insert(0, 'ngrok')
#     print(args)
#     process = subprocess.Popen(args)
#     bot.send_message(message.chat.id, get_ngrok_url())
#     os.system(KILL_CMD)


@bot.message_handler(commands=['start'])
def start_port_ngrok(message: telebot.types.Message):
    os.system(KILL_CMD)
    args = ['ngrok', 'http', '5000']
    process = subprocess.Popen(args)
    bot.send_message(message.chat.id, get_ngrok_url())


@bot.message_handler(commands=['stop'])
def start_port_ngrok(message: telebot.types.Message):
    os.system(KILL_CMD)


if __name__ == '__main__':
    bot.polling()

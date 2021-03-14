import telebot
from settings import TG_BOT_TOKEN, AUTH_TOKEN
from pyngrok import ngrok
import os

bot = telebot.TeleBot(TG_BOT_TOKEN)


def close_all_tunnels():
    tunnels = ngrok.get_tunnels()
    if len(tunnels) > 0:
        for tunnel in tunnels:
            ngrok.disconnect(tunnel.public_url)


@bot.message_handler(commands=['start'])
def start_port_ngrok(message: telebot.types.Message):
    close_all_tunnels()
    ngrok.connect(8000)
    bot.send_message(message.chat.id, ngrok.get_tunnels()[0].public_url)


@bot.message_handler(commands=['stop'])
def start_port_ngrok(message: telebot.types.Message):
    close_all_tunnels()
    bot.send_message(message.chat.id, 'done')


@bot.message_handler(commands=['url'])
def get_url(message: telebot.types.Message):
    bot.send_message(message.chat.id, ngrok.get_tunnels()[0].public_url)


if __name__ == '__main__':
    ngrok.set_auth_token(AUTH_TOKEN)
    bot.polling()

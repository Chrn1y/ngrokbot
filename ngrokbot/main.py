import telebot
from settings import TG_BOT_TOKEN
from ngrokfuncs import get_ngrok_url

bot = telebot.TeleBot(TG_BOT_TOKEN)


@bot.message_handler(commands=['url'])
def start_ngrok(message):
    ngrok_url = get_ngrok_url()
    bot.send_message(message.chat.id, ngrok_url)


if __name__ == '__main__':
    bot.polling()

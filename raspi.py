
import telebot
from config import token
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def funcname(message):
    chat_id=message.chat.id
    bot.send_message(chat_id,"hola "+message.chat.first_name)


if __name__ == "__main__":
    bot.polling()
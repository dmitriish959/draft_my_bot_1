import telebot
# импорт токена
from env import MY_TOKEN
# передача токена
bot = telebot.TeleBot(MY_TOKEN)
#Обработчик отвечающий на команду старт
bot.message_handler(commands=['start'])
#Функция спрашивающая имя
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя завут?')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'. format(name=message.text))


# Функция polling заставляет нашего бота постоянно контачить с ТГ
bot.polling()
import sqlite3

import telebot
# импорт токена
from env import MY_TOKEN

# передача токена
bot = telebot.TeleBot(MY_TOKEN)

# no test
# Обработчик отвечающий на команду старт
@bot.message_handler(commands=['start'])
# Функция спрашивающая имя
def start(message):
    # создание БД
    conn = sqlite3.connect('registr.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    sent = bot.send_message(message.chat.id, 'Как тебя завут?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
    # cur.execute('')
    # sent = bot.send_message(message.chat.id, 'Как тебя завут?')
    # bot.register_next_step_handler(sent, hello)


#def hello(message):
    #bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))


# def cars(message):
#    sent.bot_message(message.chat.id, 'Выберите марку ТС')

# Функция polling заставляет нашего бота постоянно контачить с ТГ
bot.polling()

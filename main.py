import sqlite3

import telebot
# импорт токена
from env import MY_TOKEN

# передача токена
bot = telebot.TeleBot(MY_TOKEN)


# Функция спрашивающая имя
def start(message):
    # создание БД
    conn = sqlite3.connect('registr.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS user(id int auto_increment primory key, name varchar(80)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет')
    bot.register_next_step_handler(message, user_name)
    # cur.execute('')
    # sent = bot.send_message(message.chat.id, 'Как тебя завут?')
    # bot.register_next_step_handler(sent, hello)


@bot.message_handler(commands=['start', 'help'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.chat.username))


# def cars(message):
#    sent.bot_message(message.chat.id, 'Выберите марку ТС')

# Функция polling заставляет нашего бота постоянно контачить с ТГ
bot.polling()

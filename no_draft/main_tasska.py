import telebot
from peewee import DoesNotExist, CharField, Model
# импорт токена
from env import MY_TOKEN
from models import User
from databases import db
from peewee import SqliteDatabase

# Создание таблицы
db = SqliteDatabase('bot.db')

# передача токена
bot = telebot.TeleBot(MY_TOKEN)

db.create_tables([User, ])


# Обработчик отвечающий на команду старт
@bot.message_handler(commands=['start'])
# Функция спрашивающая имя
def start(message):
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


# def hello(message):
# bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))


# def cars(message):
#    sent.bot_message(message.chat.id, 'Выберите марку ТС')


@bot.message_handler(commands=['create'])
def create_user(message):
    db.connect()
    db.create_tables([User, user_name])
    try:
        user_db = User.select().where(User.name == message.chat.username).get()
    except DoesNotExist:
        user_db = None
    if user_db is not None:
        bot.send_message(message.chat.id, 'Ты уже зарегистрирован')
    else:
        user = User()
        user.name = message.chat.username
        user.save()
        bot.send_message(message.chat.id, f'Привет, {user.name}. Ты теперь в Базе Данных')
    db.close()


# Функция polling заставляет нашего бота постоянно контачить с ТГ
bot.polling()

import telebot
from peewee import DoesNotExist, CharField, Model
# импорт токена
from telebot import types
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
    # Эта команда означает, что после отправки сообщения sent бот будет ожидать следующего шага, который будет обработан функцией hello.
    # То есть, когда пользователь отправит сообщение sent, бот перейдет к выполнению функции hello, которая будет обрабатывать следующий шаг в диалоге.
    bot.register_next_step_handler(sent, hello)


def hello(message):
    user = User(name=message.text)
    user.save()
    bot.send_message(message.chat.id, f'Привет, {user.name}!')


# Подключаемся к базе данных
db.connect()

# Создаем таблицу для модели User
db.create_tables([User, ])

# Запускаем бота
bot.polling()


# Отображение кнопок
# reply_markup=mykup
@bot.message_handler(content_types=['cars'])
def cars(message):
    mykup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Марки ТС')
    btn2 = types.KeyboardButton('Объем')
    btn3 = types.KeyboardButton('Help')
    mykup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, f'Привет, {user.name}!', reply_markup=mykup)
#def interesing(message):
    #wen = bot.send_message(message.chat.id, 'Вы хотите выбрать марку машины ?')
    #bot.register_next_step_handler(wen, cars)





# Тут функция просто отвечает что рада видеть не сохраняя в БД
# def hello(message):
# bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
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

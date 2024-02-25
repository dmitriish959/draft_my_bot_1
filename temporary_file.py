from peewee import *

# Определение модели (таблицы) в базе данных
db = SqliteDatabase('bot.db')

class User(Model):
    name = CharField()

    class Meta:
        database = db

# Подключаемся к базе данных
db.connect()

# Создаем новую запись пользователя с именем 'Alice'
user = User(name='Alice')
user.save()

# Закрываем соединение с базой данных
db.close()

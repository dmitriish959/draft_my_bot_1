from peewee import *

# Определение модели (таблицы) в базе данных
db = SqliteDatabase('bot.db')

class User(Model):
    name = CharField()

    class Meta:
        database = db

# Подключаемся к базе данных
db.connect()

# Создаем таблицу для модели User
db.create_tables([User])

# Создаем новую запись пользователя с именем 'Alice'
user = User(name='Alice')
user.save()

# Не закрываем соединение с базой данных, чтобы можно было выполнить операции записи

# Закрываем соединение с базой данных после завершения всех операций
db.close()
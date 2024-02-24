from peewee import CharField, Model, IntegerField

from databases import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(max_length=40)
    telephone = IntegerField()
    city = CharField(max_length=20)

    class Meta:
        db_table = "users"

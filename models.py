from peewee import CharField, Model

from databases import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()

    class Meta:
        db_table = "users"

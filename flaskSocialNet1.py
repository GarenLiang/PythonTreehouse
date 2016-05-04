# PythonTreehouse
import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

database = SqliteDatabase(':memory:')

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')
    
    class Meta:
        database = database
        
    @classmethod
    def new(cls, email, password):
      cls.create(
            email=email,
            password=generate_password_hash(password)
        )

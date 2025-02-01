import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMLY_TRACK_MODIFICATIONS = False

    print(SECRET_KEY)


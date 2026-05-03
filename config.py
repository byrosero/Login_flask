import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "Secret_pss_LXFDKDKD"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'usermodule.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
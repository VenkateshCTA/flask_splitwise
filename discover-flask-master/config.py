import os
import os.path


# default config
class BaseConfig(object):
    DEBUG = False
    # shortened for readability
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'
    SQLALCHEMY_DATABASE_URI = os.path.join(BASE_DIR, "sample.db")
    #SQLALCHEMY_DATABASE_URI = os.environ['sample.db']
    #with sqlite3.connect(db_path) as db:


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.sqlite'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

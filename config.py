import os

import cx_Oracle

# try:
#     cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_9")
# except Exception as err:
#     print("Whoops!")
#     print(err)

cx_Oracle.init_oracle_client(lib_dir="/Users/sarikhin/instantclient_19_8")
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ini sangat rahasia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'oracle://flasky:flasky@127.0.0.1:1521/xe'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
        

config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'default' : ProductionConfig
}
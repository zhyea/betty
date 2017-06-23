import os

import pymysql


class Config(object):
    DEBUG = False
    TESTING = False
    LOGGER_NAME = 'betty'
    TEST_PROP = 'this is a test'
    SECRET_KEY = os.urandom(32)


class ProductionConfig(Config):
    DB_CONFIG = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'betty',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor,
    }


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    DB_CONFIG = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'betty',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor
    }

import pymysql


class Database:
    def __init__(self, config):
        self.config = config
        self.__connect()

    def __connect(self):
        pymysql.connect(**self.config)

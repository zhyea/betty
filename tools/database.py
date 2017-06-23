import pymysql


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class Database(Singleton):
    def __init__(self):
        self.__config = None

    def init(self, config):
        self.__config = config

    def __connect(self):
        return pymysql.connect(**self.__config)

    def find_one(self, sql_query, *args):
        return self.__find(sql_query, True, args)

    def find_all(self, sql_query, *args):
        return self.__find(sql_query, False, args)

    def insert(self, sql_insert, *args):
        return self.__run(sql_insert, args)

    def update(self, sql_update, *args):
        return self.__run(sql_update, args)

    def delete(self, table, primary_key):
        sql = 'delete from ' + table + ' where id=%s'
        return self.__run(sql, primary_key)

    def __find(self, sql_query, is_one, args):
        conn = None
        try:
            conn = self.__connect()
            with conn.cursor() as cursor:
                cursor.execute(sql_query, args)
                if is_one:
                    result = cursor.fetchone()
                else:
                    result = cursor.fetchall()
        finally:
            if conn is not None:
                conn.close()
        return result

    def __run(self, sql, args):
        conn = None
        try:
            conn = self.__connect()
            with conn.cursor() as cursor:
                result = cursor.execute(sql, args)
            conn.commit()
        finally:
            if conn is not None:
                conn.close()
        return result


db = Database()

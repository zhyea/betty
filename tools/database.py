import pymysql


class Database:
    def __init__(self, config):
        self.config = config
        self.__connect()

    def __connect(self):
        return pymysql.connect(**self.config)

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

    def __find(self, sql_query, is_one, *args):
        try:
            conn = self.__connect()
            with conn.cursor() as cursor:
                cursor.execute(sql_query, args)
                if is_one:
                    result = cursor.fetchone()
                else:
                    result = cursor.fetchall()
            return result
        finally:
            conn.close()

    def __run(self, sql, *args):
        try:
            conn = self.__connect()
            with conn.cursor() as cursor:
                result = cursor.execute(sql, args)
            conn.commit()
            return result
        finally:
            conn.close()

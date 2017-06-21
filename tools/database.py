import pymysql


class Database:
    def __init__(self, config):
        self.config = config
        self.__connect()

    def __connect(self):
        return pymysql.connect(**self.config)

    def query(self, sql_query, *args):
        conn = self.__connect()
        with conn.cursor() as cursor:
            cursor.execute(sql_query, args)
            result = cursor.fetchone()
        conn.commit()
        conn.close()
        return result

    def insert(self, sql_delete):
        pass

    def update(self, sql_update):
        pass

    def delete(self, table, primary_key):
        pass

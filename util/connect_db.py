import MySQLdb.cursors
import json

class MysqlMethod:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host ='localhost',
            port = 3306,
            user = 'root',
            passwd = 'root',
            db = 'test_database',
            charset='utf8',
        )
        self.cur = self.conn.cursor()

    def search_one(self,sql):
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def close_mysql(self):
        self.cur.close()


if __name__ == '__main__':
    m = MysqlMethod()
    res = m.search_one("select * from test")
    print(res)
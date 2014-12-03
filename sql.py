import sqlite3
class db:
    conn = None
    def db_connect(self,db_file):
        self.conn = sqlite3.connect(db_file)
        #return conn
    def db_sql(self,sql):
        c = self.conn.cursor()
        row = c.execute(sql)
        #c.execute("create table test (a text ,b text)")
        self.conn.commit()
        return row
    def db_sql(self,sql,*arg):
        c = self.conn.cursor()
        row = c.execute(sql,arg)
        #c.execute("create table test (a text ,b text)")
        self.conn.commit()
        return row

    def db_close(self):
        self.conn.close()

def test():
    foodb = db()
    foodb.db_connect('test.db')
    row = foodb.db_sql('select * from sqlite_master')
    for d in row:
        print d
    foodb.db_close()
if __name__ == "__main__":
    test()


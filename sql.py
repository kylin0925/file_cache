import sqlite3
def db_connect(db_file):
    conn = sqlite3.connect(db_file)
    return conn
def db_sql(conn,sql):
    c = conn.cursor()
    row = c.execute(sql)
    #c.execute("create table test (a text ,b text)")
    conn.commit()
    return row
def db_sql(conn,sql,*arg):
    c = conn.cursor()
    row = c.execute(sql,arg)
    #c.execute("create table test (a text ,b text)")
    conn.commit()
    return row

def db_close(conn):
    conn.close()
'''
conn = db_connect('test.db')
row = db_sql(conn,'select * from test')
for d in row:
    print row
db_close(conn)
'''


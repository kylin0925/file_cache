import os
import sql
cache_db = 'cache.db'
def chk_table(dbfile,table):
    execsql = "select * from sqlite_master where name='%s';" %(table)
    conn = sql.db_connect(dbfile)
    r=sql.db_sql(conn,execsql)
    data = r.fetchall()
    print data
    sql.db_close(conn)
    return len(data)

def create_table(dbfile):
    global cache_db
    conn = sql.db_connect(dbfile)
    r = sql.db_sql(conn,"create table file_list (fullpath text,filename text)")
    sql.db_close(conn)


def chk_db(dbfile):
    if os.access(dbfile,os.R_OK): 
        if chk_table(file_list) == 0:
            create_table(dbfile)
    else:
        create_table(dbfile)
    
def start_cache():
    sdir = '/Users/kylin/Downloads'
    conn = sql.db_connect('f.db')

    for dname,dnames,files in os.walk(sdir):
        for f in files:
            full_path = dname + "/"+ f
            print  full_path
            execsql = 'insert into file_list (fullpath,filename) values ("%s","%s")' % (full_path,f)
            print execsql
            r=sql.db_sql(conn,execsql)


    sql.db_close(conn)

chk_db(cache_db)

import os
import sql
sdir = '/Users/kylin/Downloads'
conn = sql.db_connect('f.db')
#r = sql.db_sql(conn,"create table file_list (fullpath text,filename text)")

for dname,dnames,files in os.walk(sdir):
    for f in files:
        full_path = dname + "/"+ f
        print  full_path
        execsql = 'insert into file_list (fullpath,filename) values ("%s","%s")' % (full_path,f)
        print execsql
        r=sql.db_sql(conn,execsql)


sql.db_close()

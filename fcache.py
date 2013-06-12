import os
import sql
import sys
cache_db = 'cache.db'
def chk_table(dbfile,table):
    execsql = "select * from sqlite_master where name='%s';" %(table)
    conn = sql.db_connect(dbfile)
    r=sql.db_sql(conn,execsql)
    data = r.fetchall()
    #print data
    sql.db_close(conn)
    return len(data)

def is_dup(dbfile,fullpath,filename):
    fullpath = fullpath.replace("'","''")
    filename = filename.replace("'","''")
    execsql = "select * from file_list where fullpath='%s' and filename = '%s';" %(fullpath,filename)
    print execsql
    conn = sql.db_connect(dbfile)
    r=sql.db_sql(conn,execsql)
    data = r.fetchall()
    #print data
    sql.db_close(conn)
    return len(data) > 0

def create_table(dbfile):
    global cache_db
    conn = sql.db_connect(dbfile)
    r = sql.db_sql(conn,"create table file_list (fullpath text,filename text)")
    sql.db_close(conn)


def chk_db(dbfile):
    if os.access(dbfile,os.R_OK): 
        if chk_table(cache_db,'file_list') == 0:
            create_table(dbfile)
    else:
        create_table(dbfile)
    
def start_cache():
    sdir = '/Users/kylin/Downloads'
    conn = sql.db_connect(cache_db)
    cnt =0;
    for dname,dnames,files in os.walk(sdir):
        for f in files:
            full_path = dname + "/"+ f
            if is_dup(cache_db,full_path,f) == False:
                #print  full_path
                execsql = 'insert into file_list (fullpath,filename) values ("%s","%s")' % (full_path,f)
                #print execsql
            
                r=sql.db_sql(conn,execsql)
                cnt+=1
                sys.stdout.write('cached file count :' + str(cnt) + 'file name :' + f + '\r' )
                sys.stdout.flush()
            else:
                sys.stdout.write('cached file count :' + str(cnt) + ' dup skip' + '\r')
                sys.stdout.flush()
    sql.db_close(conn)

chk_db(cache_db)
start_cache()
#print is_dup(cache_db,'test','test')

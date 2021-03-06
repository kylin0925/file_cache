# -*- coding: utf-8 -*-
import os
import sql
import sys
cache_db = 'cache.db'
conn = sql.db_connect(cache_db)

def chk_table(table):
    execsql = "select * from sqlite_master where name=?;"
    r=sql.db_sql(conn,execsql,table)
    data = r.fetchall()
    #print data
    return len(data)

def is_dup(fullpath,filename):
    execsql = "select * from file_list where fullpath=? and filename = ?;"
    #print execsql
    r=sql.db_sql(conn,execsql,fullpath.decode('utf-8'),filename.decode('utf-8'))
    data = r.fetchall()
    #print data
    return len(data) > 0

def create_table(dbfile):
    #global cache_db
    r = sql.db_sql(conn,"create table file_list (fullpath text,filename text)")

def chk_db(dbfile):
    if os.access(dbfile,os.R_OK): 
        if chk_table('file_list') == 0:
            create_table(dbfile)
    else:
        create_table(dbfile)
    
def start_cache():
    sdir = '/Users/kylin/Downloads'
    #conn = sql.db_connect(cache_db)
    cnt =0;
    print "start file cache"
    msg_len = 0
    for dname,dnames,files in os.walk(sdir):
        for f in files:
            full_path = dname + "/"+ f
            msg = ""

            if is_dup(full_path,f) == False:
                #print  full_path
                execsql = 'insert into file_list (fullpath,filename) values (?,?)'
                #print execsql
            
                r=sql.db_sql(conn,execsql,full_path.decode('utf-8'),f.decode('utf-8'))
                cnt+=1
                msg = 'cached file count :' + str(cnt) + ' file name :' + f + '\r'
            else:
                msg = 'cached file count :' + str(cnt) + ' dup skip' + '\r'
            s = ' ' * (msg_len - 1)  + '\r'
            sys.stdout.write(s)
            sys.stdout.flush()

            msg_len = len(msg)
            sys.stdout.write(msg)
            sys.stdout.flush()
    print ""
def query_ext(ext):
    #execsql='''select fullpath,filename from file_list where filename like "%.%s"
    #         group by filename having(COUNT(*)>15);'''
    
    execsql='select fullpath,filename from file_list where filename like "%.%s"'
    r=sql.db_sql(conn,execsql)
    data = r.fetchall()
    #print data
    for f in data:
        print f[0].encode('utf-8'),f[1].encode('utf-8')

chk_db(cache_db)
start_cache()
#print is_dup(cache_db,'test','test')
#query_ext('jpg')

#close    
sql.db_close(conn)

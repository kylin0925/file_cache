# -*- coding: utf-8 -*-
import sqlalchemy
import os
def init(db_name):
    eng = sqlalchemy.create_engine('sqlite:///' + db_name,echo=False)
    metadata = sqlalchemy.MetaData()
    tab = sqlalchemy.Table(
        'file_list',
        metadata,
        sqlalchemy.Column('id',sqlalchemy.Integer,primary_key=True),
        sqlalchemy.Column('file_name',sqlalchemy.String),
        sqlalchemy.Column('full_path',sqlalchemy.String))


    metadata.create_all(eng)
    return eng,tab

def add(eng,tab,file_name,full_path):
    #file_name= 'bbc'
    ins = tab.insert().values(file_name=file_name.decode('utf-8'),full_path=full_path.decode('utf-8'))
    ins.compile().params
    conn = eng.connect()
    r = conn.execute(ins)

def query(eng,tab,full_path):
    s = sqlalchemy.sql.select([tab]).where(tab.c.full_path == full_path.decode('utf-8'))

    conn = eng.connect()
    r = conn.execute(s)
    #for row in r:
    #    print row
    return r.fetchall()

def start_cache(sdir):
    #sdir = '/Users/kylin/Downloads'
    eng,tab = init("foo.db")
    #sdir = '.'
    cnt =0;
    print "start file cache"
    for dname,dnames,files in os.walk(sdir):
        for f in files:
            full_path = dname + "/"+ f
            if full_path.find("/.git/") == -1:
                if len(query(eng,tab,full_path)) == 0:
                    print full_path,f            
                    add(eng,tab,f,full_path)
                    cnt +=1
                else:
                    print full_path,"repeat"
    print "files :",cnt
#eng,tab = init("foo.db")

#add(eng,tab)

#query(tab)

start_cache('/Users/kylin')

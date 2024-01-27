import cx_Oracle
import csv
conn=cx_Oracle.Connection('system/manager@mother')
cur=conn.cursor()

def createtable():
    query='''create table mca12(id number(2) primary key,name varchar(50))'''
    cur.execute(query)

def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    cur.execute("insert into mca12(id,name) values(:id,:name)",record)
    conn.commit()
#insertrecord(2,'srinivas')
#insertrecord(3,'rajanikanth')
#insertrecord(4,'ganesh')
    
def read_records():
    query='select * from mca12'
    cur.execute(query)
    records=cur.fetchall()
    with open('record1.csv','w',newline='') as csvfile:
        data=csv.writer(csvfile)
        data.writerow(['id','name'])
        for row in records:
            data.writerow(row)
read_records()

def fetch_record(sid):
    record={'id':str(sid)}
    query='select * from mca12 where id =:id'
    cur.execute(query,record)
    record =cur.fetchall()
    for row in record:
        print(row)
fetch_record(2)

def update_name(sid):
    fetch_record(sid)
    name=input('enter new name to update:-')
    record={'id':str(sid),'name':name}
    query='update mca12 set name=:name where id=:id'
    cur.execute(query,record)
    conn.commit()
    fetch_record(sid)

def delete_record(sid):
    record={'id':str(sid)}
    query='delete from mca12 where id=:id'
    cur.execute(query,record)
    conn.commit()

def truncate():
    query='reuncate table mca12'
    cur.execute(query)
truncate()
#def insert_from_csv():
#    with open('record1.csv','r') as csvfile:
#        data=csv.reader(csvfile)
#        for row in data:
#            print(row)

def insert_from_csv():
    with open('record1.py','r',)as csvfile:
        data=csv.reader(csvfile)
        data=list(data)
        for row in range(1,len(data)):
            insertrecord(*data[row])

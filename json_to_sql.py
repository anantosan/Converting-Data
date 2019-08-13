import json
import mysql.connector

dbku=mysql.connector.connect(
    host= 'localhost',
    port= 3306,
    user= 'root',
    password= '#####',
    database='doraemon',
    auth_plugin='mysql_native_password'
)

with open('data.json') as x:
    data=json.load(x)

isi=[]
kolom=list(data[0].keys())
for j in data:
    isi.append(tuple(j.values()))


kursor = dbku.cursor()
querydb='''
Create Table testingjson (
{} varchar(100) not null
)
'''.format(kolom[0])
kursor.execute(querydb)
dbku.commit()

for i in kolom[1:]:
    querydb='''
    alter Table testingjson 
    add column
    {} varchar(50) not null
    '''.format(i)
    kursor.execute(querydb)
    dbku.commit()

for k in isi:
    kursor = dbku.cursor()
    querydb='''
    Insert into testingjson values
    {}
    '''.format(k)
    kursor.execute(querydb)
    dbku.commit()

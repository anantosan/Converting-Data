import pymongo
import json
import mysql.connector

dbku=mysql.connector.connect(
    host= 'localhost',
    port= 3306,
    user= 'root',
    password= 'makanayam',
    database='doraemon',
    auth_plugin='mysql_native_password'
)

x= pymongo.MongoClient('mongodb://localhost:27017')

db=x['TestDB']
col=db['Test_Col']

#get all data
data=[]
for i in list(col.find()):
    data.append(i)
print(data)

for i in range(len(data)):
    data[i]['_id']=i+1

isi=[]
kolom=list(data[0].keys())
for j in data:
    isi.append(tuple(j.values()))

kursor = dbku.cursor()
querydb='''
Create Table testingmongo (
{} varchar(100) not null
)
'''.format(kolom[0])
kursor.execute(querydb)
dbku.commit()

for i in kolom[1:]:
    querydb='''
    alter Table testingmongo
    add column
    {} varchar(50) not null
    '''.format(i)
    kursor.execute(querydb)
    dbku.commit()

for k in isi:
    kursor = dbku.cursor()
    querydb='''
    Insert into testingmongo values
    {}
    '''.format(k)
    kursor.execute(querydb)
    dbku.commit()
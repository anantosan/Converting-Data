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

kursor = dbku.cursor()
querydb='''
select * from karakter
'''
kursor.execute(querydb)
data=kursor.fetchall()

querydb='''
describe karakter
'''
kursor.execute(querydb)
# kursor.fetchall()
header=[]
for i in kursor.fetchall():
    header.append(i[0])
# print(header)

datains=[]
for j in data:
    dicti={}
    for k in range (len(j)):
        dicti[header[k]]=j[k]
    datains.append(dicti)

print(datains)

for item in datains:
    col.insert_one(item)
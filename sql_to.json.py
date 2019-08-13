import csv
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

datajson=[]
for j in data:
    dicti={}
    for k in range (len(j)):
        dicti[header[k]]=j[k]
    datajson.append(dicti)

with open('sqltojson.json', 'w') as x:
    json.dump(datajson,x)
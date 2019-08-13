import csv
import mysql.connector

dbku=mysql.connector.connect(
    host= 'localhost',
    port= 3306,
    user= 'root',
    password= 'makanayam',
    database='doraemon',
    auth_plugin='mysql_native_password'
)

data=[]
with open('file_test.csv','r') as x:
    reader=csv.DictReader(x)
    for i in reader:
        data.append(dict(i))

isi=[]
kolom=list(data[0].keys())
for j in data:
    isi.append(tuple(j.values()))


kursor = dbku.cursor()
querydb='''
Create Table testingcsv (
{} varchar(100) not null
)
'''.format(kolom[0])
kursor.execute(querydb)
dbku.commit()

for i in kolom[1:]:
    querydb='''
    alter Table testingcsv 
    add column
    {} varchar(50) not null
    '''.format(i)
    kursor.execute(querydb)
    dbku.commit()

for k in isi:
    kursor = dbku.cursor()
    querydb='''
    Insert into testingcsv values
    {}
    '''.format(k)
    kursor.execute(querydb)
    dbku.commit()
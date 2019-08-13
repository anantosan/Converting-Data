import pymongo
import csv
x= pymongo.MongoClient('mongodb://localhost:27017')

db=x['TestDB']
col=db['Test_Col']

data=[]
with open('file_test.csv','r') as x:
    reader=csv.DictReader(x)
    for i in reader:
        data.append(dict(i))

for i in data:
    col.insert_one(i)
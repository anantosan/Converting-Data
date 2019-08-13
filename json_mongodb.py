import pymongo
import json
x= pymongo.MongoClient('mongodb://localhost:27017')

db=x['TestDB']
col=db['Test_Col']

with open('data.json') as x:
    data=json.load(x)

for i in data:
    col.insert_one(i)
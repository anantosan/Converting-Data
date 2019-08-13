import pymongo
import json
x= pymongo.MongoClient('mongodb://localhost:27017')

db=x['TestDB']
col=db['Test_Col']

#get all data
data=[]
for i in list(col.find()):
    data.append(i)
# print(data)

for i in range(len(data)):
    data[i]['_id']=i+1
# print(data)
# print(list(col.find()))

with open('mongo_to_json.json', 'w') as x:
    json.dump(data,x)
import pymongo
import csv
x= pymongo.MongoClient('mongodb://localhost:27017')

db=x['TestDB']
col=db['Test_Col']

#get all data
data=[]
for i in list(col.find()):
    data.append(i)
print(data)
# print(list(col.find()))

with open('mongotocsv.csv','w',newline='') as y:
    kolom = list(data[0].keys())
    tulis= csv.DictWriter(y,kolom)
    tulis.writeheader()
    tulis.writerows(data)
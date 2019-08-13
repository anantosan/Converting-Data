import csv
import json

data=[]
with open('x.csv','r') as x:
    reader=csv.DictReader(x)
    for i in reader:
        data.append(dict(i))

with open('file_test.json', 'w') as x:
    json.dump(data,x)
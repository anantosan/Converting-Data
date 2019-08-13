import csv
import json

with open('data.json') as x:
    data=json.load(x)

with open('file_test.csv','w',newline='') as y:
    kolom = list(data[0].keys())
    tulis= csv.DictWriter(y,kolom)
    tulis.writeheader()
    tulis.writerows(data)

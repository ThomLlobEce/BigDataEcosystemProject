import json, sys
from elasticsearch import Elasticsearch
from datetime import date

def connect_data():
    es = None
    es = Elasticsearch([{'host':'localhost','port':9200}])
    if es.ping():
        print("Connected to Elasticsearch ....")
    else:
        print("There is a problem. Make sure your server is ON")
    return es
    

if len(sys.argv) > 1:
    date = sys.argv[1]
else:
    date = date.today()

    date = str(date.year) + "-" + str(date.month) + "-" + str(date.day-1)

data = {}

with open(f"{date}.json") as json_file:
    data = json.loads(json_file.read())

es = connect_data()

res = es.indices.get_alias("*")
for name in res:
    print(name)

if 'covid_test' in res:
    print('The index already exist no need to create it again ....')
else:
    es.indices.create(index="covid_test", ignore = 400)
    print('Creating index : covid_test')

for el in data:
    resp = es.index(index='covid_test',doc_type='country',body = el)

query = {
    "query":{
        "match_all":{}
    }
}

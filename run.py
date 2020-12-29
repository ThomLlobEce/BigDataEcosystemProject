import os
import sys
import pandas as pd
import elasticsearch
from elasticsearch import Elasticsearch

def connect_data():
    es = None
    es = Elasticsearch([{'host':'localhost','port':9200}])
    if es.ping():
        print("Connected to Elasticsearch ....")
    else:
        print("There is a problem. Make sure your server is ON")
    return es


if __name__ == "__main__":

    os.system('spark-submit .\get_and_prepare_data.py')
    os.system('python merge.py')

    es = connect_data()

    res = es.indices.get_alias("*")
    for name in res:
        print(name)

    if 'covid_test' in res:
        print('The index already exist no need to create it again ....')
    else:
        es.indices.create(index="covid_test", ignore = 400)
        print('Creating index : covid_test')

    e1 = {"continent":"Europe","location":"Russia","date":"2020-12-26","total_cases":2992123.0,"new_cases":28833.0,"total_deaths":53539.0,"new_deaths":554.0,"total_cases_per_million":20503.197,"new_cases_per_million":197.575,"total_deaths_per_million":366.87,"new_deaths_per_million":3.796,"new_tests":494071.0,"total_tests":8.9099604E7,"total_tests_per_thousand":610.545,"new_tests_per_thousand":3.386,"positive_rate":0.063,"tests_per_case":15.8,"tests_units":"tests performed","population":1.4593446E8,"population_density":8.823,"median_age":39.6,"aged_65_older":14.178,"aged_70_older":9.393,"hospital_beds_per_thousand":8.05,"human_development_index":0.816}
    e2 = {"continent":"Europe","location":"Albania","date":"2020-12-26","total_cases":55755.0,"new_cases":375.0,"total_deaths":1143.0,"new_deaths":9.0,"total_cases_per_million":19374.175,"new_cases_per_million":130.308,"total_deaths_per_million":397.178,"new_deaths_per_million":3.127,"population":2877800.0,"population_density":104.871,"median_age":38.0,"aged_65_older":13.188,"aged_70_older":8.643,"hospital_beds_per_thousand":2.89,"human_development_index":0.785}
    e3 = {"continent":"Africa","location":"Algeria","date":"2020-12-26","total_cases":97857.0,"new_cases":416.0,"total_deaths":2722.0,"new_deaths":6.0,"total_cases_per_million":2231.577,"new_cases_per_million":9.487,"total_deaths_per_million":62.074,"new_deaths_per_million":0.137,"population":4.3851043E7,"population_density":17.348,"median_age":29.1,"aged_65_older":6.211,"aged_70_older":3.857,"handwashing_facilities":83.741,"hospital_beds_per_thousand":1.9,"human_development_index":0.754}
    e4 = {"continent":"Asia","location":"Japan","date":"2020-12-26","total_cases":218467.0,"new_cases":3892.0,"total_deaths":3062.0,"new_deaths":46.0,"total_cases_per_million":1727.333,"new_cases_per_million":30.773,"total_deaths_per_million":24.21,"new_deaths_per_million":0.364,"new_tests":32677.0,"total_tests":4314877.0,"total_tests_per_thousand":34.116,"new_tests_per_thousand":0.258,"positive_rate":0.066,"tests_per_case":15.1,"tests_units":"people tested","population":1.26476458E8,"population_density":347.778,"median_age":48.2,"aged_65_older":27.049,"aged_70_older":18.493,"hospital_beds_per_thousand":13.05,"human_development_index":0.909}
    e5 = {"continent":"Africa","location":"South Africa","date":"2020-12-26","total_cases":994911.0,"new_cases":11552.0,"total_deaths":26521.0,"new_deaths":245.0,"total_cases_per_million":16775.13,"new_cases_per_million":194.778,"total_deaths_per_million":447.169,"new_deaths_per_million":4.131,"new_tests":37817.0,"total_tests":6415824.0,"total_tests_per_thousand":108.177,"new_tests_per_thousand":0.638,"positive_rate":0.261,"tests_per_case":3.8,"tests_units":"people tested","population":5.930869E7,"population_density":46.754,"median_age":27.3,"aged_65_older":5.344,"aged_70_older":3.053,"handwashing_facilities":43.993,"hospital_beds_per_thousand":2.32,"human_development_index":0.699}
    e6 = {"continent":"Oceania","location":"Australia","date":"2020-12-26","total_cases":28308.0,"new_cases":11.0,"total_deaths":908.0,"new_deaths":0.0,"total_cases_per_million":1110.123,"new_cases_per_million":0.431,"total_deaths_per_million":35.608,"new_deaths_per_million":0.0,"positive_rate":0.0,"tests_per_case":3421.1,"tests_units":"tests performed","population":2.5499881E7,"population_density":3.202,"median_age":37.9,"aged_65_older":15.504,"aged_70_older":10.129,"hospital_beds_per_thousand":3.84,"human_development_index":0.939}
    e7 = {"continent":"Asia","location":"Azerbaijan","date":"2020-12-26","total_cases":213192.0,"new_cases":1428.0,"total_deaths":2454.0,"new_deaths":38.0,"total_cases_per_million":21026.563,"new_cases_per_million":140.84,"total_deaths_per_million":242.032,"new_deaths_per_million":3.748,"population":1.0139175E7,"population_density":119.309,"median_age":32.4,"aged_65_older":6.018,"aged_70_older":3.871,"handwashing_facilities":83.241,"hospital_beds_per_thousand":4.7,"human_development_index":0.757}
    e8 = {"continent":"North America","location":"Mexico","date":"2020-12-26","total_cases":1377217.0,"new_cases":4974.0,"total_deaths":122026.0,"new_deaths":189.0,"total_cases_per_million":10681.669,"new_cases_per_million":38.578,"total_deaths_per_million":946.431,"new_deaths_per_million":1.466,"new_tests":3411.0,"total_tests":3123617.0,"total_tests_per_thousand":24.227,"new_tests_per_thousand":0.026,"positive_rate":0.406,"tests_per_case":2.5,"tests_units":"people tested","population":1.28932753E8,"population_density":66.444,"median_age":29.3,"aged_65_older":6.857,"aged_70_older":4.321,"handwashing_facilities":87.847,"hospital_beds_per_thousand":1.38,"human_development_index":0.774}
    e9 = {"continent":"Oceania","location":"New Zealand","date":"2020-12-26","total_cases":2144.0,"new_cases":16.0,"total_deaths":25.0,"new_deaths":0.0,"total_cases_per_million":444.607,"new_cases_per_million":3.318,"total_deaths_per_million":5.184,"new_deaths_per_million":0.0,"positive_rate":0.001,"tests_per_case":856.8,"tests_units":"tests performed","population":4822233.0,"population_density":18.206,"median_age":37.9,"aged_65_older":15.322,"aged_70_older":9.72,"hospital_beds_per_thousand":2.61,"human_development_index":0.917}

    resp = es.index(index='covid_test',doc_type='country',body = e8)

    query = {
        "query":{
            "match_all":{}
        }
    }

    res = es.search(index='covid_test',body=query)

    es.delete(index="covid_test",doc_type="country",id='vndwq3YBF9Skf3w2uitj')

    es.indices.delete(index="cov",ignore=[400,404])


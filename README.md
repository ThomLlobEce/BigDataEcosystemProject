# BigDataEcosystemProject

The projects aims to retrieve and update information about the coronavirus pandemic, in order to have a daily-updated vision on what's going on all over the world.

The data comes from [Our World in Data](https://ourworldindata.org/), which is open access licensed under the Creative Common BY Licence.

### Authors
* Pablo Antoniadis (pablo.antoniadis@edu.ece.fr)
* Thomas Llobregat (thomas.llobregat@edu.ece.fr)
* Sébastien Ye (sebastien.ye@edu.ece.fr)

# Get this project running on your machine

## Create a python virtual environement

If you haven't installed virtualenv yet :
```
pip install virtualenv
```

Create and activate a virtual environnement (replace myenv by the name of your choice)

```
python -m venv myenv
myenv\Scripts\activate
```

## Install dependencies

### Python packages

```
pip install -r requirements.txt
```

### Sparks

* Windows 

To get sparks on windows, you can follow this tutorial (You can skip Step 1 & 2 if you already have both java and python running on your machine) :
https://phoenixnap.com/kb/install-spark-on-windows-10

* Mac OS

To get sparks on mac OS, you can follow this tutorial :
https://medium.com/beeranddiapers/installing-apache-spark-on-mac-os-ce416007d79f

* Linux

To get sparks on ubuntu, you can follow this tutorial :
https://phoenixnap.com/kb/install-spark-on-ubuntu

### ElasticSearch

You can get elastic search running on your computer by following the next tutorial :

https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html#run-elasticsearch-local


### Kibana

You can get kibana running on your computer by following the next tutorial :

* Mac OS X :
https://www.elastic.co/guide/en/kibana/current/targz.html#install-darwin64

* Linux :
https://www.elastic.co/guide/en/kibana/current/targz.html#install-linux64

* Windows :
https://www.elastic.co/guide/en/kibana/current/windows.html#install-windows


# Run the project

Once you have gathered all the dependencies, follow the next steps (depending on your OS):

* Windows : 
1. Start Elasticsearch 
```
.\elasticsearch.bat
```
Elasticsearch should be accessible from https://localhost:9200
2. Start Kibana 
```
.\bin\kibana.bat
```
Kibana should be accessible from https://localhost:5601
3. Run the project 
```
python scheduler.py
```
4. You can run the project in test mode (simulate the last 10 days in ~ 20 minutes instead of 10 days)
```
python scheduler.py --test
```

* Linux / Mac OS :
1. Start Elasticsearch 
```
./elasticsearch
```
Elasticsearch should be accessible from https://localhost:9200
2. Start Kibana
```
./bin/kibana
```
Kibana should be accessible from https://localhost:5601
3. Run the project 
```
python scheduler.py
```
4. You can run the project in test mode (simulate the last 10 days in ~ 20 minutes instead of 10 days)
```
python scheduler.py --test
```

This will automatically, each day :
* Fetch data from https://ourworldindata.org/
* Pre process the previous day data using sparks
* Save the pre process data into a {date}.json file
* Push the new data to elasticsearch and update all visualisations

Each day, you can now see new visualisations from the previous in kibana at : 

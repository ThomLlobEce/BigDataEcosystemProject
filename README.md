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

## Install dependancies

### Python packages

```
pip install -r requirements.txt
```

### Sparks

* Windows 

To get sparks on windows, you can follow this tutorial (You can skip Step 1 & 2 if you already have both java and python running on your machine) :
https://phoenixnap.com/kb/install-spark-on-windows-10

* Mac OS

* Linux

### ElasticSearch

* Windows

* Mac OS

* Linux

### Kibana

* Windows

* Mac OS

* Linux


# Run the project

Once you have gathered all the dependencies, you can simply run the next command line (depending on your OS).
* Windows : 
```
watch python run.py
```

* Linux :

* Mac OS :

This will automatically, each day :
* Fetch data from https://ourworldindata.org/
* Pre process the previous day data using sparks
* Save the pre process data into a {date}.json file
* Push the new data to elasticsearch and update all visualisations

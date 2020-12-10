# BigDataEcosystemProject

## To get this project running

We recommend you to use a docker to get sparks running on your computer.

```console
docker run -d -p 8888:8888 jupyter/pyspark-notebook
```

Then, you need to connect to the bash of your container.

To connect to the bash of your container you will need to run the following command : 

```console
docker ps -a
----------------------------
Container ID | Image | ...
<container_id> | jupyter/pyspark-notebook | ....
----------------------------

docker exec -it <container_id> /bin/bash
```

You are now in the bash of your jupyter/pyspark-notebook. You will need then to fetch the code from this github repository.

```console
mkdir project/
cd project/
git init
git pull https://github.com/ThomLlobEce/BigDataEcosystemProject.git
```

To know where you can run your notebook, you can execute the following command : 

```
jupyter notebook list
```

You will get the currently running jupyter notebook session's url.
Copy and paste it into your favourite browser.

If you get trouble accessing the provided IP address, replace 0.0.0.0 with localhost.

You can now run the notebook PullAndProcessing.ipynb.

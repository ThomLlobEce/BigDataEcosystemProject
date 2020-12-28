import os

os.system('spark-submit .\get_and_prepare_data.py')
os.system('python merge.py')
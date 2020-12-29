from pyspark.sql import SparkSession
from pyspark.sql.functions import ceil
from pyspark import SparkFiles
from time import sleep
from datetime import date
import sys

if len(sys.argv) > 1:
    date = sys.argv[1]
else:
    date = date.today()

    date = str(date.year) + "-" + str(date.month) + "-" + str(date.day-1)

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()


print("------------------------------------------------------Job Starting------------------------------------------------------")

spark.sparkContext.addFile("https://covid.ourworldindata.org/data/owid-covid-data.csv")

print(f"------------------------------------------------------Filtering for {date}------------------------------------------------------")

df = spark.read.csv(SparkFiles.get("owid-covid-data.csv"), header=True, inferSchema= True)

today_df = df.filter(df['date'] == date)

today_df = today_df.filter(df['location'] != "World")

columns_to_delete = ["iso_code", "new_cases_smoothed", "new_deaths_smoothed", "new_cases_smoothed_per_million", "new_deaths_smoothed_per_million", "icu_patients_per_million", "hosp_patients_per_million", "weekly_icu_admissions" "weekly_icu_admissions_per_million", "weekly_hosp_admissions", "weekly_hosp_admissions_per_million", "new_tests_smoothed", "new_tests_smoothed_per_thousand", "total_vaccinations_per_hundred", "stringency_index", "gdp_per_capita", "extreme_poverty", "cardiovasc_death_rate", "diabetes_prevalence", "female_smokers", "male_smokers", "life_expectancy"]

today_df = today_df.drop(*columns_to_delete)

today_df = today_df.withColumn('vaccination_percentage', (today_df.total_vaccinations / today_df.population)*100)

print(f"------------------------------------------------------Saving to data-{date}------------------------------------------------------")

today_df.write.format("json").save(f"data-{date}")

spark.stop()

print("------------------------------------------------------Job finished------------------------------------------------------")
import os, time as t, datetime, sys

def job(next_start, shift=None):
    next_start = datetime.datetime.strptime(next_start, "%m/%d/%Y, %H:%M:%S")
    if datetime.datetime.now() >= next_start:
        if shift is not None :
            date = datetime.date.today()
            date = str(date.year) + "-" + str(date.month) + "-" + str(date.day-shift)
            print(f"Running for date : {date}")

        print("--- STARTING JOB")
        print("--- SUBMITTING PYSPARK APP TO SPARK")
        os.system(f'spark-submit .\get_and_prepare_data.py {date}')
        print("--- MERGING JSON FILES TOGETHER")
        os.system(f'python merge.py {date}')
        print("--- SENDING DATA TO ELASTICSEARCH")
        os.system(f'python elasticsearch_connector.py {date}')
        return (next_start + trigger_delay).strftime("%m/%d/%Y, %H:%M:%S")
    return next_start.strftime("%m/%d/%Y, %H:%M:%S")



next_start = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

if "--test" in sys.argv:
    print("--- ENTERING TEST MODE")
    trigger_delay = datetime.timedelta(minutes = 2)

    for i in range(10, 1, -1):
        next_start = job(next_start, shift=i)
        print(f"Next refresh at : {next_start}")
        t.sleep(60)

else:
    next_start = next_start.replace(hour= 17, minute=0, second=0, microsecond=0)
    trigger_delay = datetime.timedelta(days = 1)

    while True:
        next_start = job(next_start.strftime("%m/%d/%Y, %H:%M:%S"))
        print(f"Next refresh at : {next_start}")
        t.sleep(60)


    
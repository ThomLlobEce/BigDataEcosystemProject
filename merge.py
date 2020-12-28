from datetime import date
import os

date = date.today()

date = str(date.year) + "-" + str(date.month) + "-" + str(date.day-1)

dirs = os.listdir(f"data-{date}")

f = open(f"{date}.json", 'w')
for fil in dirs:
    if fil.endswith(".json"):
        temp = open(f"data-{date}/{fil}", "r")
        f.write(temp.read())
        temp.close()
    os.remove(f"data-{date}/{fil}")
os.rmdir(f"data-{date}")
f.close()



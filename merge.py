from datetime import date
import os, re, sys

if len(sys.argv) > 1:
    date = sys.argv[1]
else:
    date = date.today()

    date = str(date.year) + "-" + str(date.month) + "-" + str(date.day-1)

dirs = os.listdir(f"data-{date}")

content = '['

for fil in dirs:
    if fil.endswith(".json"):
        temp = open(f"data-{date}/{fil}", "r")
        content += temp.read()
        temp.close()
    os.remove(f"data-{date}/{fil}")
os.rmdir(f"data-{date}")

content += "]"

content = re.sub(r'}', '},', content)

content = content[:-3] + content[-2:]

f = open(f"{date}.json", 'w')
f.write(content)
f.close()



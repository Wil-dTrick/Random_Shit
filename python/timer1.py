tasks = { 
    "Check Jira": 15,
    "Duplicate Complaints": 15,
    "Morning Break": 30,
    "Complaints - Upload": 15,
    "Assigned Tasks": 60,
    "Afternoon Break": 30
}

from datetime import datetime


if datetime.now().day < 5:
    tasks.update({[2]"Complaints - SOM": 20})
elif datetime.now().day == 14:
    tasks.update({"Complaints - Last Day": 45})
    tasks.update({"Complaints - Convoke": 45})
else:
    pass

if datetime.today().weekday() == 1:
    tasks.update({"Vendor Forecast": 15})
    tasks.update({"On Demand": 30})
elif datetime.today().weekday() == 4:
    tasks.update({"Make-up File": 15})
else:
    pass

#print(tasks)

import time

for x, y in tasks.items():
    print(x)
    time.sleep(y)

tasks = ["Set up", "Check Jira", "Duplicate Complaints", "Complaints - Upload", "Clean Desk", "Morning Break", "Assigned Tasks", "Afternoon Break", "Assigned Tasks", "Update Jira"]
    
times = [15, 15, 15, 15, 15, 30, 90, 30, 150, 30]
        
def list_update():
    from datetime import datetime
    
    # After Complaints - Upload from 10:00 and 10:45
    
    if datetime.now().day < 4:
        tasks.insert(4,"Complaints - SOM")
        times.insert(4,15)
        if datetime.now().day == 1:
            tasks.insert(5,"Dishes")
            times.insert(5,30)
        elif datetime.now().day == 2:
            tasks.insert(5,"Vacuum")
            times.insert(5,30)
        elif datetime.now().day == 3:
            tasks.insert(5,"Bathroom")
            times.insert(5,30)
        else:
            tasks.insert(5,"Play a Game")
            times.insert(5,30)
    elif datetime.now().day == 14:
        tasks.insert(4,"Complaints - SOM")
        times.insert(4,15)
        tasks.insert(5,"Complaints - Convoke")
        times.insert(5,30)
    elif datetime.now().day == 5:
        tasks.insert(4,"Complaints - Last Day")
        times.insert(4,40)
        tasks.insert(5,"Walk it off")
        times.insert(5,5)
    elif datetime.now().day == 7 and datetine.now().weekday == 0:
        tasks.insert(4,"Complaints - Last Day")
        times.insert(4,45)
    elif datetime.now().day == 8:
        tasks.insert(4,"Hallmark")
        times.insert(4,15)
        tasks.insert(5,"Clean Up Downloads")
        times.insert(5,30)
    else:
        tasks.insert(4,"Practice Work Skill")
        times.insert(4,30)
        tasks.insert(5,"Calesthenics")
        times.insert(5,15)
    
    #11:30 to 12:00 after morning break
    if datetime.today().weekday() == 1: #Tuesday
        tasks.insert(8,"Vendor Forecast")
        times.insert(8,15)
        tasks.insert(9,"On Demand")
        times.insert(9,15)
    elif datetime.today().weekday() == 4: #Friday
        tasks.insert(8,"Make-up File")
        times.insert(8,15)
        tasks.update(9,"On Demand")
        times.insert(9,15)
    else:
        tasks.insert(8,"BAU - Jira")
        times.insert(8,15)
        tasks.insert(9,"Assigned Tasks")
        times.insert(9,15)

def timer():
    import time
    
    for x, y in zip(tasks,times):
        print(x)
        print(y, "minutes")
        time.sleep(y)


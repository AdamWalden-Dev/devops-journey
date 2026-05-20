from datetime import datetime
import sys
import os
import psutil


def get_timestamp():
    timestamp = datetime.now()
    return(f"{timestamp: %B %d, %Y  %I:%M:%S}")

def get_system_info():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent
    return {
        "cpu": cpu_percent,
        "memory": memory_percent,
        "disk": disk_percent
        }
    sys.exit(0)
 
 

def system_report(timestamp, systeminfo):
    try:
        with open(f"logs/report_{timestamp}.txt", "w") as f:
            f.write(f"{timestamp}\n CPU: {systeminfo['cpu']}%\n Memory: {systeminfo['memory']}%\n Disk: {systeminfo['disk']}")
    except Exception as e:
        print(f"Unknown ERROR: {e}")
        sys.exit(1)

report = get_system_info()
time = get_timestamp()
system_report(time,report)

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
    
 
def system_report(timestamp, systeminfo):
    try:
        with open(f"logs/report_{timestamp}.txt", "w") as f:
            f.write(f"{timestamp}\n CPU: {systeminfo['cpu']}%\n Memory: {systeminfo['memory']}%\n Disk: {systeminfo['disk']}")
        sys.exit(0)
    except Exception as e:
        print(f"Unknown ERROR: {e}")
        sys.exit(1)

def check_thresholds(systeminfo):
    warning = 0
    if systeminfo['cpu'] >= 80:
        warning += 1
        print(f"Warning: CPU is at {systeminfo['cpu']}% ")
    else:
        print(f"CPU: {systeminfo['cpu']}% - OK")
    if systeminfo['memory'] >= 80:
        warning += 1
        print(f"Warning: Memory is at {systeminfo['memory']}% ")
    else:
        print(f"Memory: {systeminfo['memory']}% - OK")
    if systeminfo['disk'] >= 90:
        warning += 1
        print(f"Warning: Disk is at {systeminfo['disk']}% ")
    else:
        print(f"Disk: {systeminfo['disk']}% - OK")
    if warning == 0:
        print("System is running without issues.")
    else:
        print(f"System has {warning} warnings, diagnose the problem.")




report = get_system_info()
time = get_timestamp()
check_thresholds(report)
system_report(time,report)

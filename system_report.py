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
print(get_system_info())
 
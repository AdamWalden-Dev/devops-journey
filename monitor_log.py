from datetime import datetime
import sys
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def read_file():
    try:
        with open("servers.csv", "r") as f:
            lines = f.readlines()
            warning_count = 0
            for line in lines:
                line = line.strip()
                data = line.split(',')
                name = data[0]
                status = data[1]
                disk = int(data[2])
                memory = int(data[3])
                location = data[4]
                if disk >= 999:
                    disk_status = "Too High"
                    warning_count += 1
                else:
                    disk_status = "Disk is fine"
                if memory >= 999:
                    memory_status = "Too High"
                    warning_count += 1
                else:
                    memory_status = "Memory is fine"
                print(f"{timestamp} Name:{name} - Status:{status} - Disk: {disk}|{disk_status} - Memory: {memory}|{memory_status} - Location: {location}")
                monitor_log(name,status,disk,disk_status,memory,memory_status,location)
            if warning_count > 0:
                print("TOO MANY WARNINGS")
                sys.exit(1)
            else:
                print("ALL GOOD")
                sys.exit(0)
    except Exception as e:
        print(f"UNKNOWN!! - {e}")


def monitor_log(name,status,disk,disk_status,memory,memory_status,location):
    try:
        with open("monitor_log.txt", "a") as f:
            f.write(f"{timestamp} Name:{name} - Status:{status} - Disk: {disk}|{disk_status} - Memory: {memory}|{memory_status} - Location: {location}\n")
    except Exception as e:
        print(f"Could not Complete. {e}")

read_file()
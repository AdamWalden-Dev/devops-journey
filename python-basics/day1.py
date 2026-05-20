servers = {
    'server1': {'status': 'offline', 'disk_usage': 80},
    'server2': {'status': 'online', 'disk_usage': 20},
    'server3': {'status': 'online', 'disk_usage': 65}
}

def check_server(disk_limit):
    for server in servers:
        status = servers[server]['status']
        disk = servers[server]['disk_usage']
        if disk >= disk_limit:
            disk_status = "Warning"
        else:
            disk_status = "OK"
        
        print(f"{server} is ... {status} Disk: {disk}% - {disk_status}")
        server_log(server, status, disk, disk_status)
    print("Health report saved successfully")

def server_log(server, status, disk, disk_status):
    try:
        with open('health_report.txt', 'a') as f:
            f.write(f"{server} is ... {status} Disk: {disk}% - {disk_status}\n")
    except Exception as e:
        print(f" Failed to write alert {e}")


check_server(80)
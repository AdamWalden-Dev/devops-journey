def servers():
    try:
        with open('servers.csv') as f:
            disk_limit = 80
            memory_limit = 75
            online = 0
            offline = 0
            lines = f.readlines()
            warning = 0
            ok = 0
            for line in lines:
                line = line.strip()
                data = line.split(',')
                name = data[0]
                status = data[1]
                disk = int(data[2])
                memory = int(data[3])
                location = data[4]
                
                if status == 'online':
                    online += 1
                else:
                    offline += 1
                if disk >= disk_limit:
                    disk_status = 'warning'
                    warning = warning + 1
                else:
                    disk_status = 'ok'
                    ok = ok + 1
                if memory >= memory_limit:
                    memory_status = 'warning'
                    warning = warning + 1
                else:
                    memory_status = 'ok'
                    ok = ok + 1
                print(f"Checking..{name} | status: {status} | disk: {disk}% {disk_status}| memory: {memory}% {memory_status}| location: {location}")
                server_report(name, status, disk, memory, location)
            print(f"ok: {ok}")
            print(f"warning: {warning}")
            print(f"online: {online}")
            print(f"offline: {offline}")
    except Exception as e:
        print(f'Uknown error: {e}')
    print("Saved Successfully")
    

def server_report(name, status, disk, memory, location):
    try:
        with open('day3_report.txt', 'a') as f:
            f.write(f"{name} | {status} | Disk: {disk}% | Memory: {memory}% | {location}\n")
    except Exception as e:
        print(f"Not known: {e}")

servers()
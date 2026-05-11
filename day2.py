servers = {
    'server1': {'status': 'online', 'disk_usage': 65, 'mem_usage': 80, 'location': 'us-west'},
    'server2': {'status': 'offline', 'disk_usage': 90, 'mem_usage': 20, 'location': 'us-west'},
    'server3': {'status': 'online', 'disk_usage': 30, 'mem_usage': 74, 'location': 'eu-west'},
    'server4': {'status': 'offline', 'disk_usage': 20, 'mem_usage': 10, 'location': 'eu-west'}
}


        
def server_status(disk_limit, memory_limit):
            warning_count = 0
            online_count = 0
            offline_count = 0
            for server in servers:
                
                status = servers[server]['status']
                disk = servers[server]['disk_usage']
                memory = servers[server]['mem_usage']
                location = servers[server]['location']

                if disk >= disk_limit:
                    disk_status = "Warning"
                    warning_count = warning_count + 1
                else:
                    disk_status = "OK"
                    

                if memory >= memory_limit:
                    memory_status = "Warning"
                    warning_count = warning_count + 1
                else:
                    memory_status = "OK"
                
                if status == 'online':
                     online_count = online_count + 1
                else:
                     offline_count = offline_count + 1
                    
                print(f"Checking {server} | {status} | disk status is..{disk_status} | memory status is..{memory_status}---{location}\n")
                health_report(status,disk,memory,location)
            print(f"Warnings-{warning_count}")
            print(f"Online-{online_count}")
            print(f"Offline-{offline_count}")
            print("Saved to log successfully")
            
            
            

        
def health_report(status,disk,memory,location):
     try:
          with open('health_report2.txt', 'a') as f:
               f.write(f"Status is..{status}, Disk: {disk}% | Memory:{memory} | Location: {location}\n")
     except Exception as e:
          print(f"Unexpected Error: {e}")
     


 


server_status(80, 80)

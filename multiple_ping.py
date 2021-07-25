import os
import time

#multiple ping
with open('hosts.txt', 'r') as file:
    dump = file.read()
    dump = dump.splitlines()
    
for ip in dump:
    os.system('ping ' + ip)
    time.sleep(2)
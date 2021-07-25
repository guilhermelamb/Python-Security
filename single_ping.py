import os
import time

#Single ping
print('#'*80)
ip_or_host = input('Digite IP ou host a ser verificado: ')

os.system('ping -n 6 {}'.format(ip_or_host))


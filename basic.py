import os
import time

time.sleep(3)

print("Haciendo 'curl' a la IP del container")
ip=os.environ.get('host')

time.sleep(1)
out = os.popen('curl ' + ip + ':8080/')
out=out.read()
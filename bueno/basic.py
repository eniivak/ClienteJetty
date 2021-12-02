import os
import time
#import requests


time.sleep(10)
ip=os.environ.get('host')
#url= ip + ':8080/webapps'
#requests.get(url).text
out = os.popen('curl ' + ip + ':8080/webapps')
out=out.read()
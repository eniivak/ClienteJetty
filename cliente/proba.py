import os
import subprocess

imageID = os.popen('docker images | grep lana_web |awk \'{print $3;}\'')
imageID=imageID.read()
imageID = imageID.replace('\n','')

#imageID = str(subprocess.check_output("sudo docker images | grep lana_web  | awk '{print $3}'", shell=True))
#imageID= os.system("sudo docker images | grep lana_web | awk '{print $3}'")
#print(imageID)
containerID = os.popen("docker ps | grep " + imageID + " | awk '{print $1}'")
containerID=containerID.read()
containerID = containerID.replace('\n','')

#print("containerID" + containerID)
resul=os.system("docker exec " + containerID + " ls /var/lib/jetty")
print(resul)


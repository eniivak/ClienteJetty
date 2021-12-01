import os
print("hau da bolumenaren edukia")
imageID = os.popen('ls datuak/jetty')
imageID=imageID.read()
print(imageID)
print("esto despues")
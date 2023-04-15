"""
API Endpoint: https://fdo.rocketlaunch.live/json/launches/next/5
Reference code: https://holypython.com/api-5-space-launch-data/

"""
import threading
import os
import subprocess
import datetime
from datetime import datetime
import json
import urllib.request
import datetime
import shutil
import time
def API():
    #Read the API response
        url = "https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/19.0760/72.8777/14/10/300/&apiKey=6PBQZM-CQEZ6E-V9SVQZ-4ZUR"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())

        satname = result['info']['satname']
        passes = result['info']['passescount']
        print("Name of the satellite: ",satname)
        print("Number of passes in 10 days: ",passes)
        for x in range(0,passes):
            startAz = result['passes'][x]['startAz']
            startAzCompass = result['passes'][x]['startAzCompass']
            startUTC = result['passes'][x]['startUTC']
            maxAz = result['passes'][x]['maxAz']
            maxAzCompass = result['passes'][x]['maxAzCompass']
            maxEl =  result['passes'][x]['maxEl']
            maxUTC = result['passes'][x]['maxUTC']
            endAz = result['passes'][x]['endAz']
            endAzCompass = result['passes'][x]['endAzCompass']
            endUTC = result['passes'][x]['endUTC']
            mag = result['passes'][x]['mag']
            duration = result['passes'][x]['duration']
            startVisibility = result['passes'][x]['startVisibility']

            print("\nPass no." , x+1)
            print("Start Azimuth: ",startAz)
            print("Start Azimuth Compass: ",startAzCompass)
            print("Start Time (Epoch): ", startUTC)
            print("Start Time (UTC): ",datetime.datetime.fromtimestamp(startUTC))
            print("Max Azimuth: ", maxAz)
            print("Max Azimuth Compass: ",maxAzCompass)
            print("Max Elevation: ",maxEl)
            print("Max Time (Epoch): ",maxUTC)
            print("Max Time (UTC): ",datetime.datetime.fromtimestamp(maxUTC))
            print("End Azimuth: ",endAz)
            print("End Azimuth Compass: ",endAzCompass)
            print("End Time (Epoch): ",endUTC)
            print("End Time (UTC): ",datetime.datetime.fromtimestamp(endUTC))
            print("Magnitude: "+ str(mag))
            print("Pass Duration: ",duration)
            print("Start Visibility (UTC): ",datetime.datetime.fromtimestamp(startVisibility))

            file = open("iss_passes.txt", "a")
            print("Name of the satellite: ",satname)
            print("Number of passes in 10 days: ",passes)
            file.write("\n\nPass no."+str(x+1))
            file.write("\nStart Azimuth: "+str(startAz))
            file.write("\nStart Azimuth Compass: "+str(startAzCompass))
            file.write("\nStart Time (Epoch): "+str(startUTC))
            file.write("\nStart Time (UTC): "+str(datetime.datetime.fromtimestamp(startUTC)))
            file.write("\nMax Azimuth: "+str(maxAz))
            file.write("\nMax Azimuth Compass: "+str(maxAzCompass))
            file.write("\nMax Elevation: "+str(maxEl))
            file.write("\nMax Time (Epoch): "+str(maxUTC))
            file.write("\nMax Time (UTC): "+str(datetime.datetime.fromtimestamp(maxUTC)))
            file.write("\nEnd Azimuth: "+str(endAz))
            file.write("\nEnd Azimuth Compass: "+str(endAzCompass))
            file.write("\nEnd Time (Epoch): "+str(endUTC))
            file.write("\nEnd Time (UTC): "+str(datetime.datetime.fromtimestamp(endUTC)))
            file.write("\nMagnitude: "+str(mag))
            file.write("\nPass Duration: "+str(duration))
            file.write("\nStart Visibility (UTC): "+str(datetime.datetime.fromtimestamp(startVisibility)))
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            file.write ("\nCurrent Time: "+str(current_time))
            print("Current Time: ", current_time)
            file.close()
        path_current="./iss_passes_current.txt"
        shutil.move("./iss_passes.txt", path_current)
        time.sleep(5)
        t2.start()

#email trigger
def Mail_Trigger():
    dt = datetime.datetime.now()
    print('Datetime is:', dt)

    # get day of week as an integer
    x = dt.weekday()
    print('Day of the week is:', x)
    if x == 5:
        rawpath = os.getcwd() + "\\mail.py"
        path = rawpath.replace('\\', '/')
        subprocess.call(['python', path])
        print("Mail sent!")
        # time.sleep(172800)
    else:
        print("Mail Not Sent!")
        pass

t1 = threading.Thread(target=API)
t2 = threading.Thread(target=Mail_Trigger)
t1.start()

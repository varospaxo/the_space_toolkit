# import datetime
from datetime import datetime
import json
import urllib.request
from datetime import datetime
from dateutil import tz
import os
import time
import subprocess

#Read the API response
url = "https://fdo.rocketlaunch.live/json/launches/next/5"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

launch_name = result['result'][0]['name'] 
vehicle_name = result['result'][0]['vehicle']['name']
pad_name = result['result'][0]['pad']['name']
pad_location_name = result['result'][0]['pad']['location']['name']    
pad_state = result['result'][0]['pad']['location']['state']
pad_statename = result['result'][0]['pad']['location']['statename']
pad_country = result['result'][0]['pad']['location']['country']
mission_description = result['result'][0]['missions'][0]['description']
launch_description = result['result'][0]['launch_description']
launch_time = result['result'][0]['t0']
quicktext = result['result'][0]['quicktext']
 
#Print in terminal
print("Mission Name: "+launch_name)
print("Vehicle Name: "+vehicle_name)
print("Launchpad Name: "+pad_name)
#print("Launchpad Location: "+str(pad_location_name)+", "+(pad_statename)+", "+(pad_state))
print("Pad State: "+str(pad_state))
print("Pad State Name: "+str(pad_statename))
print("Launchpad Country: "+pad_country)
# print(pad_country)    
print("Mission Description: "+ str(mission_description))
print("Launch Description: "+launch_description)
try:
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Kolkata')
                    # METHOD 2: Auto-detect zones:
                    # from_zone = tz.tzutc()
                    # to_zone = tz.tzlocal()
    IST = datetime.strptime(launch_time, '%Y-%m-%dT%H:%MZ')
    IST = IST.replace(tzinfo=from_zone)
    central = IST.astimezone(to_zone)
    timel = "Launch Time (IST): " + str(central)
    print(timel)
except TypeError:
    timel = "Launch Time: TBD"
    print()
    
print("Tentative Launch Time (UTC): "+str(launch_time))
print("Launch Livestream: "+quicktext)

#Print in file
f = open("./SandBox/launches_Notifier.txt","a")
f.write("Mission Name: "+str(launch_name))
f.write("\nVehicle Name: "+str(vehicle_name))
f.write("\nLaunchpad Name: "+str(pad_name))
#print("Launchpad Location: "+str(pad_location_name)+", "+(pad_statename)+", "+(pad_state))
f.write("\nLaunchpad Location Name: "+str(pad_location_name))
f.write("\nPad State: "+str(pad_state))
f.write("\nPad State Name: "+str(pad_statename))
f.write("\n"+"Launchpad Country: "+str(pad_country))
# f.write("\n"+pad_country)    
f.write("\n"+"Mission Description: "+ str(mission_description))
f.write("\n"+"Launch Description: "+str(launch_description))
f.write("\nTentative Launch Time (UTC): "+str(launch_time))
f.write("\nLaunch Livestream: "+quicktext)
f.write("\n"+timel)
f.close()
#Cache file
path_current="./SandBox/launches_Notifier.txt"
movepath = "./SandBox/launches_Notifier_OP.txt" 
os.replace(path_current, movepath)
time.sleep(15)

try:
    launch = datetime.strptime(launch_time, '%Y-%m-%dT%H:%MZ')
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    current = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
    delta = launch-current
    print (launch)
    print (current)
    print(delta)
    print(delta.total_seconds())
except:
    pass

rangetime = range(13000, 14000, 1)
if (delta.total_seconds()) in rangetime:
        rawpath = os.getcwd() + "\\SandBox\\mail.py"
        path = rawpath.replace('\\', '/')
        subprocess.call(['python', path])
else:
    pass
            

#     try:
#         from_zone = tz.gettz('UTC')
#         to_zone = tz.gettz('Asia/Kolkata')
#                         # METHOD 2: Auto-detect zones:
#                         # from_zone = tz.tzutc()
#                         # to_zone = tz.tzlocal()
#         IST = datetime.strptime(launch_time, '%Y-%m-%dT%H:%MZ')
#         IST = IST.replace(tzinfo=from_zone)
#         central = IST.astimezone(to_zone)
#         print("Launch Time (IST): " + str(central))
#     except TypeError:
#          print("Launch Time: TBD")
# print(launch_time)


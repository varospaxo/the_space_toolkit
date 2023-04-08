"""
API Endpoint: https://fdo.rocketlaunch.live/json/launches/next/5
Reference code: https://holypython.com/api-5-space-launch-data/

"""

import json
import time
import os
import urllib.request
from datetime import datetime
from dateutil import tz
from urlextract import URLExtract

def readapi():
    while True:
        #Read the API response
        url = "https://fdo.rocketlaunch.live/json/launches/next/5"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())


        for x in range(0,5):

            launch_name = result['result'][x]['name'] 
            vehicle_name = result['result'][x]['vehicle']['name']
            pad_name = result['result'][x]['pad']['name']
            pad_location_name = result['result'][x]['pad']['location']['name']    
            pad_state = result['result'][x]['pad']['location']['state']
            pad_statename = result['result'][x]['pad']['location']['statename']
            pad_country = result['result'][x]['pad']['location']['country']
            mission_description = result['result'][x]['missions'][0]['description']
            launch_description = result['result'][x]['launch_description']
            launch_time = result['result'][x]['t0']
            quicktext = result['result'][x]['quicktext']

            print("\nLaunch no.: " + str(x+1))
            print("Mission Name: "+launch_name)
            print("Vehicle Name: "+vehicle_name)
            print("Launchpad Name: "+pad_name)
            #print("Launchpad Location: "+str(pad_location_name)+", "+(pad_statename)+", "+(pad_state))
            print (pad_location_name)
            print(pad_state)
            print(pad_statename)
            print("Launchpad Country: "+pad_country)
            print(pad_country)    
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
            hehe = URLExtract()
            urls = hehe.find_urls(str(quicktext))
            files = "launch"+str(x+1)+".html"
            f = open(str(files),"a")
            f.write("Launch no.: " + str(x+1)+"</br>")
            # f.write("\nMission Name: "+str(launch_name)+"</br>")
            f.write("\n<a href="+urls[0]+">"+"Mission Name: "+str(launch_name)+"</a></br>")
            f.write("\nVehicle Name: "+str(vehicle_name)+"</br>")
            f.write("\nLaunchpad Name: "+str(pad_name)+"</br>")
            #print("Launchpad Location: "+str(pad_location_name)+", "+(pad_statename)+", "+(pad_state))
            # f.write("\n"+str(pad_state))
            # f.write("\n"+str(pad_statename))
            f.write("\n"+"Launch Country: "+str(pad_country)+"</br>")
            # f.write("\n"+pad_country)    
            # f.write("\n"+"Mission Description: "+ str(mission_description))
            f.write("\n"+"Launch Description: "+str(launch_description)+"</br>")

            
            
            # f.write("\n"+"Quicktext: "+str(quicktext))            
            f.write("\n"+timel)
            f.close()
            path_current=str(files)
            rawpath = os.getcwd() + "\\SandBox\\backend_output\\launch"+str(x+1)+"_op.html"
            opfile = rawpath.replace('\\', '/')

            movepath = str(opfile) 
            os.replace(path_current, movepath)
        time.sleep(15)
readapi()
    
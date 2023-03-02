"""
API Endpoint: https://fdo.rocketlaunch.live/json/launches/next/5
Reference code: https://holypython.com/api-5-space-launch-data/

"""

import json
import urllib.request
from datetime import datetime
from dateutil import tz

#Read the API response
url = "https://fdo.rocketlaunch.live/json/launches/next/5"
response = urllib.request.urlopen(url)
result = json.loads(response.read())


for x in range(1,5):

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

    print("\nLaunch no.: " , x+1)
    print("Mission Name: "+launch_name)
    print("Vehicle Name: "+vehicle_name)
    print("Launchpad Name: "+pad_name)
    #print("Launchpad Location: "+str(pad_location_name)+", "+(pad_statename)+", "+(pad_state))
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
        print("Launch Time (IST): " + str(central))
    except TypeError:
         print("Launch Time: TBD")
        
    print("Tentative Launch Time (UTC): "+str(launch_time))
    print("Launch Livestream: "+quicktext)




#Process to fetch API data here
# print (result.valid_auth)

# formatted_result = json.dumps(result, indent=4)


# for x in range(1,5):
#     print("%s: %s" % (x, result[x]))



# #Open the .txt file
# file = open("launches.txt", "w")
# res = str (object = result)
# file.write(res)
# file.close()

#Display file output
# webbrowser.open("launches.txt")

"""
API Endpoint: https://fdo.rocketlaunch.live/json/launches/next/5
Reference code: https://holypython.com/api-5-space-launch-data/

"""

import json
import urllib.request

#Read the API response
url = "https://fdo.rocketlaunch.live/json/launches/next/5"
response = urllib.request.urlopen(url)
result = json.loads(response.read())


for x in range(0,4):

    launch_name = result['result'][x]['name'] 
    vehicle_name = result['result'][x]['vehicle']['name']
    pad_name = result['result'][x]['pad']['name']
    pad_location = { 
                    result['result'][x]['pad']['location']['name'] ,    
                    result['result'][x]['pad']['location']['state'] , 
                    result['result'][x]['pad']['location']['statename'] ,
                    result['result'][x]['pad']['location']['country']
                    }
    mission_description = result['result'][x]['missions'][0]['description']
    launch_description = result['result'][x]['launch_description']
    launch_time = result['result'][x]['t0']
    quicktext = result['result'][x]['quicktext']

    print("\nLaunch no." , x+1)
    print(launch_name)
    print(vehicle_name)
    print(pad_name)
    print(pad_location)
    print(mission_description)
    print(launch_description)
    print(launch_time)
    print(quicktext)




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

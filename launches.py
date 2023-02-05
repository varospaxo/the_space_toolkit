"""
API Endpoint: https://fdo.rocketlaunch.live/json/launches/next/5
JSON formatter (for beautifying JSON response from API Endpoint in browser): https://jsonformatter.org
Reference code: https://holypython.com/api-5-space-launch-data/


Task:
***Extract the following data from the api and save it in a .txt file using Python script -
Launch Name
Provider name
Vehicle name
Pad name
Pad Location - name, state, statename, country
Mission Description (even if null)
Launch Description
Launch t0 (launch time and date)
Quicktext
"""

import json
import urllib.request
import webbrowser

#Read the API response
url = "https://fdo.rocketlaunch.live/json/launches/next/5"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#Process to fetch API data here
print (result)



#Open the .txt file
file = open("launches.txt", "w")
res = str (object = result)
file.write(res)
file.close()

#Display file output
webbrowser.open("launches.txt")

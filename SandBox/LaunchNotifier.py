# import datetime
from datetime import datetime
import json
import urllib.request
from datetime import datetime
from dateutil import tz

#Read the API response
url = "https://fdo.rocketlaunch.live/json/launches/next/5"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
launch_time = result['result'][0]['t0']
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


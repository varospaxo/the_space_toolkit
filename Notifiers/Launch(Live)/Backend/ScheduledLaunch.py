# import datetime.datetime
import datetime
import json
import urllib.request
from dateutil import tz
import requests
import os
import time
import subprocess

while True:
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
        IST = datetime.datetime.strptime(launch_time, '%Y-%m-%dT%H:%MZ')
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
    f = open("./launches_Notifier.txt","a")
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
    path_current="./launches_Notifier.txt"
    movepath = "./launches_Notifier_OP.txt"
    os.replace(path_current, movepath)
    time.sleep(15)

    try:
        launch = datetime.datetime.strptime(launch_time, '%Y-%m-%dT%H:%MZ')
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        current = datetime.datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
        delta = launch-current
        print (launch)
        print (current)
        print(delta)
        print(delta.total_seconds())
    except:
        pass
    try:
        rangetime = range(3600, 3700, 1)
        if (delta.total_seconds()) in rangetime:
                rawpath = os.getcwd() + "\\mail.py"
                path = rawpath.replace('\\', '/')
                subprocess.call(['python', path])
                print("Mail Sent!")
                time.sleep(100)
        else:
            pass
    except:
        pass
    time.sleep(30)
    def scheduler():
        t = time.localtime()
        current_hour = time.strftime("%H", t)
        current_minute = time.strftime("%M", t)
        print(current_hour)
        print(current_minute)
        # t = datetime.time(19, 4)
        t = datetime.time(int(current_hour), int(current_minute))
        # print(t)
        result = datetime.datetime.combine(datetime.date.today(), t) + datetime.timedelta(minutes=2)
        # print(result)
        only_t = result.time()
        # print(only_t)
        timelast = datetime.datetime.strptime(str(only_t), '%H:%M:%S')
        hour = timelast.hour
        minute = timelast.minute
        print (hour)
        print (minute)
        username = 'launchmail'
        token = 'd2e02d0bb23ab2c182949328224fc9df906e5c20'
        host = 'www.pythonanywhere.com'
        # command="python LaunchNotifier.py"
        # enabled='true'
        # interval= "daily"
        description= str(only_t)
        id=356533
        response = requests.patch(f'https://{host}/api/v0/user/{username}/schedule/{id}/'.format(
                host=host, username=username, id=id
            ),
        headers={'Authorization': f'Token {token}'.format(token=token)}, json={'hour': '{hour}'.format(hour=hour), 'minute': '{minute}'.format(minute=minute), 'description' : '{description}'.format(description=description)})
        if response.status_code == 200:
            print(response.content)
        else:
            print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

    scheduler()

    #     try:
    #         from_zone = tz.gettz('UTC')
    #         to_zone = tz.gettz('Asia/Kolkata')
    #                         # METHOD 2: Auto-detect zones:
    #                         # from_zone = tz.tzutc()
    #                         # to_zone = tz.tzlocal()
    #         IST = datetime.datetime.strptime(launch_time, '%Y-%m-%dT%H:%MZ')
    #         IST = IST.replace(tzinfo=from_zone)
    #         central = IST.astimezone(to_zone)
    #         print("Launch Time (IST): " + str(central))
    #     except TypeError:
    #          print("Launch Time: TBD")
    # print(launch_time)


"""
API Endpoint: https://fdo.rocketlaunch.live/json/launches/next/5
Reference code: https://holypython.com/api-5-space-launch-data/

"""
#launches
import json
import time
import os
import urllib.request
from datetime import datetime
from dateutil import tz
from urlextract import URLExtract
import wget
import requests
import ast
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import shutil
import os
import requests
from bs4 import BeautifulSoup
import os
from urlextract import URLExtract

def readapi():
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
        rawpath = os.getcwd() + "\\launches\\launch"+str(x+1)+"_op.html"
        opfile = rawpath.replace('\\', '/')

        movepath = str(opfile) 
        os.replace(path_current, movepath)
readapi()

#apod

def apod():
    url= "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    r = requests.get(url)
    data = ast.literal_eval(r.content.decode('utf-8'))
    try:
        print(data["url"])
        print(data["media_type"])
        if data["media_type"] == "image":
            wget.download(data["url"], "./APOD_temp.jpg")
            # img = plt.imread("./APOD_temp.jpg")
            # plt.imshow(img)
            # plt.show()
            picture_path = "./APOD_current.jpg"
            shutil.move("./APOD_temp.jpg", picture_path)
            rawpath = os.getcwd() + "/APOD_current.jpg"
            path = rawpath.replace('\\', '/')
            # ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
            print(os.getcwd())
            print(rawpath)
            print(path)
            print(picture_path)
        else:
            print("Content not an image!")
            pass
    except:
        print("\nService unreachable!")
apod()

#mpow

def mpow():
    url = "https://mars.nasa.gov/mars2020/multimedia/raw-images/image-of-the-week/"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.find('div', class_="main_image")

    # print(images)
    # image_url = urlparse(str(images))
    extractor = URLExtract()
    urls = extractor.find_urls(str(images))
    print(urls)
    image_data = requests.get(urls[0]).content

    with open("MPOW_current.jpg", "wb") as handler:
        handler.write(image_data)
mpow()

#astonauts
def astronauts():
    astroresponse = requests.get("http://api.open-notify.org/astros.json")
    astrodata = astroresponse.json()
    number = astrodata['number']
    print("Number of people in space = "+str(number))
    for x in range(0, number):
        name = astrodata['people'][x]['name']
        print(name)
        spacecraft = astrodata['people'][x]['craft']
        print(spacecraft)
        files = "astronaut"+str(x+1)+".html"
        f = open(os.getcwd() + "\\Astronauts\\"+str(files),"a")
        f.write("Astronaut no.: " + str(x+1)+"</br>")
        f.write("\nAstronaut Name: "+str(name)+"</br>")
        f.write("\nSpacecraft Name: "+str(spacecraft)) 
        url = "https://bing-image-search1.p.rapidapi.com/images/search"
        astronaut= name+"Astronaut"
        querystring = {"q":"{Astronaut}".format(Astronaut=str(astronaut)),"count":"1"}

        headers = {
            "X-RapidAPI-Key": "7f4205c376mshabb48c2be654f3ep15eb79jsn25209fe5e03b",
            "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        thumbnail= data['value'][0]['thumbnailUrl'] 
        print(thumbnail)
        print('')
        image_data = requests.get(thumbnail).content
        image_name = "Astronaut"+str(x+1)+".jpg"
        with open(os.getcwd() + "\\Astronauts\\"+str(image_name), "wb") as handler:
            handler.write(image_data)
astronauts()
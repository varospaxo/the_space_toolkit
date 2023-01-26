# Dependencies
import turtle
import json
import urllib.request
import subprocess
import geocoder
import time
from shapely import Point

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
    # load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']
    lat = float(lat)
    lon = float(lon)
    print("\nISS Latitude"+str(lat))
    print("\nISS Longitude"+str(lon))
    #GUI
    iss.goto(lon, lat)
    
    #user tracking
    g = geocoder.ip('me')
    # print("\nLatitude "+str(g.lat))
    # print("\nLongitude "+str(g.lng))
    # print("\nLatitude Range "+str(g.lat+100.0000))
    # print("\nLongitude Range "+str(g.lng+100.000))

    #geofencing
    user_area = Point(g.lat, g.lng).buffer(50)
    sat_position = Point(lat, lon)
    #print(user_area)
    #print(sat_position)
    
    #email trigger
    if user_area.contains(sat_position):
        subprocess.call(['python', 'huihui.py'])
        time.sleep(5)
    time.sleep(1)
    

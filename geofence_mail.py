# Dependencies
import subprocess
import geocoder
import time
from shapely import Point

while True:
    
    g = geocoder.ip('me')
    print("\nLatitude"+str(g.lat))
    print("\nLongitude"+str(g.lng))
    print("\nLatitude Wow"+str(g.lat+0.0017))
    print("\nLongitude Wow"+str(g.lng+0.0007))
    user_area = Point(g.lat, g.lng).buffer(1)
    #print(user_area)
    user_position = Point(g.lat+0.0017, g.lng+0.0007)
    if user_area.contains(user_position):
        subprocess.call(['python', 'huihui.py'])
        time.sleep(5)
    time.sleep(5)
    

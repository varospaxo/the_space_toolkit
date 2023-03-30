import wget
import requests
import ast
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import shutil
import os
import ctypes
from wposcross import change_wallpaper

url= "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
r = requests.get(url)
data = ast.literal_eval(r.content.decode('utf-8'))
try:
    print(data["url"])
    print(data["media_type"])
    if data["media_type"] == "image":
        wget.download(data["url"], "./wallpaper_temp.jpg")
        img = plt.imread("./wallpaper_temp.jpg")
        plt.imshow(img)
        plt.show()

        update = input("Update Wallpaper? (y/n) ")
        if update == "y" or update == "yes":
            picture_path = "./wallpaper_current.jpg"
            shutil.move("./wallpaper_temp.jpg", picture_path)
            rawpath = os.getcwd() + "/wallpaper_current.jpg"
            path = rawpath.replace('\\', '/')
            # ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
            change_wallpaper(path)
            print(os.getcwd())
            print(rawpath)
            print(path)
            print(picture_path)
        else:
            os.remove("./wallpaper_temp.jpg")
            print("Wallpaper not updated")
    else:
        print("Content not an image!")
        pass
except:
    print("\nService unreachable!")
import wget
import requests
import ast
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import shutil
import os


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
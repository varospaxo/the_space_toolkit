import wget
import tkinter as tk
from PIL import Image, ImageTk
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

        root = tk.Tk()
        root.geometry("300x300")
        def set_wallpaper():
            rawpath = os.getcwd() + "/wallpaper_current.jpg"
            path = rawpath.replace('\\', '/')
            # ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
            change_wallpaper(path)
            print(os.getcwd())
            print(rawpath)
            print(path)

        img = Image.open("wallpaper_temp.jpg")
        img = img.resize((300, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        panel = tk.Label(root, image=img)
        panel.pack(side="top", fill="both", expand="yes")

        button = tk.Button(root, text="Set as Wallpaper", command=set_wallpaper())
        button.pack(side="bottom", fill="both", expand="yes")

        root.mainloop()
    else:
        print("Content not an image!")
        pass
except:
    print("\nService unreachable!")
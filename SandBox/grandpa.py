import tkinter as tk
from PIL import Image, ImageTk
import ctypes
from wposcross import change_wallpaper
import shutil
import os


def set_wallpaper():
    rawpath = os.getcwd() + "/wallpaper_current.jpg"
    path = rawpath.replace('\\', '/')
    # ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    change_wallpaper(path)

root = tk.Tk()
root.geometry("300x300")

img = Image.open("wallpaper_current.jpg")
img = img.resize((300, 300), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

panel = tk.Label(root, image=img)
panel.pack(side="top", fill="both", expand="yes")

button = tk.Button(root, text="Set as Wallpaper", command=set_wallpaper)
button.pack(side="bottom", fill="both", expand="yes")

root.mainloop()
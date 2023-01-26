# Dependencies
import turtle
import json
import urllib.request
import subprocess
import geocoder
import time
from shapely import Point
import os


rawpath = os.getcwd() + "\\huihui.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])
time.sleep(5)
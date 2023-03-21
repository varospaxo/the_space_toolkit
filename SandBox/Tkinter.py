# import required modules
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
  
  
  
# adjust window
root=tk.Tk()
root.geometry("200x200")

images = ["1.jpg", "2.jpg", "3.jpg"]
# loading the images
for x in range(len(images)):
    print(images[x])
    img=ImageTk.PhotoImage(Image.open(images[x]))

  
l=Label()
l.pack()
  
  
  
# using recursion to slide to next image
x = 1
  
# function to change to next image
def move():
    global x
    if x == 4:
        x = 1
    if x == 1:
        l.config(img)
    elif x == 2:
        l.config(img)
    elif x == 3:
        l.config(img)
    x = x+1
    root.after(2000, move)
  
# calling the function
move()
  
  
  
root.mainloop()
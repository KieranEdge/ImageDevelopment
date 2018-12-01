from tkinter import *
from PIL import Image, ImageTk
import os

def OpenImage():
    ImagePath

# Opening a window for displaying the image
ImageWindow = Tk()

# Defining the path to the local image
ImagePath = r"C:/Users/Public/Pictures/Sample Pictures/Penguins.jpg"

# Opening the image
Penguins = Image.open(ImagePath)

# Opening the image in a Tk friendly format
PenguinsTK = ImageTk.PhotoImage(Image.open(ImagePath))

# Creating the panel for the image
Panel = Label(ImageWindow, image=PenguinsTK)

# Packing the panel into the window
Panel.pack(side="bottom", fill="both", expand="yes")

# Running the window
ImageWindow.mainloop()





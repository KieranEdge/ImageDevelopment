from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import ttk
import os

# Opening a window for displaying the image and options
ImageWindow = Tk()

# Loading the image
ImagePath = "Starting Image.jpg"


# Creating the frames within the window
lf = Frame(ImageWindow)
lf.pack(side=LEFT)

rf = Frame(ImageWindow)
rf.pack(side=RIGHT)

# function to open image with given file path
def OpenImage(imagepath):
    img = Image.open(imagepath)
    imgtk = ImageTk.PhotoImage(img)
    Label(rf, image=imgtk).pack

# Function to fet file path
def RootToImage():
    ImagePath = filedialog.askopenfile()



# Creating the buttons
b1 = ttk.Button(lf, text='Select Image')
b2 = ttk.Button(lf, text='Display Image')

b1.pack()
b1.config(command=RootToImage())

b2.pack()
b2.config(command=OpenImage(ImagePath))

# Running the window
ImageWindow.mainloop()



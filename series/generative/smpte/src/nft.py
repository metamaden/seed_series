import numpy as np
import tensorflow as tf
import matplotlib as mpl
import IPython.display as display
import PIL.Image

import random

# set seed
random.seed(1)

# make new image
np.random.normal(

imgpath=""

from PIL import Image
img = Image.open('sample.jpg')
pixels = img.load()
width, height = img.size 
for col in range(width):
    for row in range(height):
        if pixels[col,row] == (255, 0, 0):
            pixels[col,row] = (0, 0 ,0)

img.show()


from PIL import Image, ImageDraw
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0,128,0)
width=10
height=10
image = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image)
filename = "mylines.jpg"
image.save(filename)

root = tk.Tk()
root.title("drawing lines")
# create the drawing canvas
cv = tk.Canvas(root, width=width, height=height, bg='white')
cv.pack()

# draw horizontal lines
x1 = 0
x2 = 450
for k in range(0, 500, 50):
    y1 = k
    y2 = k
    # Tkinter (visible)
    cv.create_line(x1, y1, x2, y2)
    # PIL (to memory for saving to file)
    draw.line((x1, y1, x2, y2), black)    

# draw vertical lines
y1 = 0
y2 = 450
for k in range(0, 500, 50):
    x1 = k
    x2 = k
    # Tkinter
    cv.create_line(x1, y1, x2, y2)
    # PIL
    draw.line((x1, y1, x2, y2), black)
    
cv.postscript(file="mylines.ps", colormode='color')
filename = "mylines.jpg"
image.save(filename)
root.mainloop()





from PIL import Image
import numpy as np
img1 = Image.open('tv.png')
pixels = np.array(img1)
pixels[np.all(pixels == (255, 0, 0), axis=-1)] = (0,0,0)
img2 = Image.fromarray(pixels)
img2.show()
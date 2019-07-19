#!/usr/bin/env python3

from PIL import Image
from PIL import ImageOps
import xlwt, sys

x = 100
y = 100

im = Image.open("123.jpg")   #load Image
im.resize((x,y)).save('resize.jpg')	#resizing the Image to the dimensions x and

im = Image.open("resize.jpg")
output = ImageOps.grayscale(im)
output.save('resize.jpg')
im = Image.open("resize.jpg")

f = open("image.txt","w")

for pixelx in range(0,x-1):
    f.write('\n')
    for pixely in range(0,y-1):
        color = im.getpixel((pixely,pixelx))
        if color <= 255 and color >= 253:ch = " "
        elif color <= 253 and color >= 250:ch = "."
        elif color <= 250 and color >= 230:ch = ","
        elif color <= 230 and color >= 210:ch = '"'
        elif color <= 210 and color >= 190:ch = '^'
        elif color <= 190 and color >= 170:ch = "%"
        elif color <= 170 and color >= 150:ch = "&"
        elif color <= 150 and color >= 130:ch = "a"
        elif color <= 130 and color >= 110:ch = "o"
        elif color <= 110 and color >= 90:ch = "L"
        elif color <= 90 and color >= 70:ch = 'y'
        elif color <= 70 and color >= 50:ch = 'Y'
        elif color <= 50 and color >= 30:ch = "O"
        elif color <= 30 and color >= 10:ch = "H"
        elif color < 10 and color >= 0:ch = "#"
        else:ch = " "
        f.write(ch)

from tkinter import *
from turtle import color
from PIL import Image, ImageTk
import numpy as np
from pyparsing import col
from Pixel import *
from matplotlib import pyplot as plt

from utils import *
from labelFunc import *
from spatialNeighbors import *

import cv2 as cv

#img = Image.open("Paysage1.jpg")
img = cv.imread('Paysage6.png')
img = img[:, :, [2, 1, 0]]
#img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

h = len(img)
l = len(img[0])

print(img[100, 100])
print(l, h)
N = l * h

app = Tk()
app.geometry("{l}x{h}".format(l = l + 185, h = h))

canvasFunc = Canvas(app, bg='red')
canvasFunc.pack(side = TOP, anchor='nw', fill='both')

canvas = Canvas(app, bg='black')
canvas.pack(side = RIGHT, anchor='nw', fill='both', expand=1)

im = Image.fromarray(img)
imgN = ImageTk.PhotoImage(image=im)

#imgN = ImageTk.PhotoImage(img)
imgShow = canvas.create_image(0, 0, anchor=NW, image=imgN)

colors = ['black', 'blue', 'cyan', 'green', 'magenta', 'red', 'white', 'yellow']
colorsLabel = []

#Dictionnary of coordinates with the key equals to the color (from colors) of the pixel
coordinates = {}
for elem in colors:
    coordinates[elem] = []

#Dictionnary of the average Intensity of the pixels from a same stroke
# with the key equals to the color (from colorsLabel)
labelAverage = {}
averageTab = []

color = [colors[0]]

#To know if the tab L has been created for the pixels, 0 = false, 1 = true
Lcreate = [0]

#Creation of a all the Pixels' objects
Pixels = []
def fillPixels(Pixels):
    for i in range(0, h):
        for j in range(0, l):
            Pixels.append(Pixel(i, j))
fillPixels(Pixels)

#To change color of the rectangle to show the selected color
def changeColor(event, color):
    color[0] = colors[liste.curselection()[0]]
    canvas.itemconfig(rectangle, fill = color)
rectangle = canvas.create_rectangle(50,50,150,150, fill = color)


#To draw in the app
canvas.bind("<Button-1>", lambda event : get_x_y(event, img))
canvas.bind("<B1-Motion>", lambda event : draw(event, color, canvas, coordinates, Pixels, l))

left_frame = Frame(app, bg= 'white')

liste = Listbox(left_frame, selectborderwidth = 10)
 
for i in range(0, len(colors)):
    liste.insert(END, '')
    liste.itemconfig(i , bg = colors[i], selectbackground = colors[i])
 
liste.bind("<<ListboxSelect>>", lambda event: changeColor(event, color))
liste.pack()
left_frame.pack(side = LEFT, fill = Y)


buttonShowCoordinates = Button(canvasFunc, text = "Afficher les coordonnées", bg = 'white', fg = 'blue', command = lambda : showCoordinates(Pixels, coordinates))
buttonShowCoordinates.pack(fill = X)

buttonShowCoordinates = Button(canvasFunc, text = "Set L", bg = 'white', fg = 'blue', command = lambda : setL(Lcreate, colors, coordinates, Pixels, colorsLabel))
buttonShowCoordinates.pack(fill = X)

buttonShowCoordinates = Button(canvasFunc, text = "Average", bg = 'white', fg = 'blue', command = lambda : average(img, coordinates, averageTab, colorsLabel, labelAverage))
buttonShowCoordinates.pack(fill = X)

buttonShowCoordinates = Button(canvasFunc, text = "OMEGAS", bg = 'white', fg = 'blue', command = lambda : OmegaS(img, Pixels, Pixels[getPixelFromCoordinates(img, 315,396)]))
buttonShowCoordinates.pack(fill = X)

buttonShowCoordinates = Button(canvasFunc, text = "MAJOR", bg = 'white', fg = 'blue', command = lambda : majorFunc(img, Pixels))
buttonShowCoordinates.pack(fill = X)

buttonShowCoordinates = Button(canvasFunc, text = "NOT TROLL OPTI", bg = 'white', fg = 'blue', command = lambda : notTroll(app, img, Pixels, colorsLabel, labelAverage))
buttonShowCoordinates.pack(fill = X)

L1 = Label(canvasFunc, text="Coordonnées")
L1.pack(fill = X)
E1 = Entry(canvasFunc, bd =5)
E1.pack(side = LEFT)
E2 = Entry(canvasFunc, bd =5)
E2.pack(side = LEFT)

buttonShowCoordinates = Button(canvasFunc, text = "GET COLOR", bg = 'white', fg = 'blue', command = lambda : getIntensityFromPixel(img, Pixels[getPixelFromCoordinates(img, E1.get(), E2.get())]))
buttonShowCoordinates.pack(fill = X)

buttonShowCoordinates = Button(canvasFunc, text = "CANNY", bg = 'white', fg = 'blue', command = lambda : getCanny(img, Pixels))
buttonShowCoordinates.pack(fill = X)

app.mainloop()
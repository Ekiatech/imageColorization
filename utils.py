#To get the pos(x, y) of the mouse click
from re import I


def get_x_y(event, img):
    global x, y
    x, y = event.x, event.y
    print("TEST")
    print(y, x, " : ", img[y, x])



#To get the pos(x, y) of the mouse click and draw the line
def draw(event, color, canvas, coordinates, Pixels, l):
    print("=======COORDS============")

    global x, y
    canvas.create_line((x, y, event.x, event.y), fill=color[0])
    coordinates[color[0]].append([y, x])
    print("===================")
    print(x, y)
    i = y
    j = x
    Pixels[i * l + j].setColor(color[0]) #FORMULE PAS SURE
    print(Pixels[i  * l + j].getPos())
    x, y = event.x, event.y

#To show the dictionnary of coordinates by the color 
def showCoordinates(Pixels, coordinates):
    for i in Pixels:
        if i.color != -1:
            print(i.getPos(), i.color)
    print(coordinates)
    return 3

def getPixelFromCoordinates(img, x, y):
    l = len(img[0])
    return (int(x) * l + int(y))

def getColorFromPixel(p):
    print(p.color)
    return p.color

def getIntensityFromPixel(img, p):
    print(img[p.getPos()])
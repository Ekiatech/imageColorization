from re import M
from spatialNeighbors import *
from utils import *
import numpy as np
import time
import cv2 as cv
from collections import OrderedDict

#
def posInColorsLabel(color, colorsLabel):
    for i in range(len(colorsLabel)):
        if color == colorsLabel[i]:
            return i

#Debug function to show the color of a pixel
def debug(Pixels):
    n = 0
    for i in Pixels:
        if i.color != -1 and n != 1:
            print(i.x, i.y, i.color, i.L)
            n = 1

#To create the tab L for each pixel
def setL(Lcreate, colors, coordinates, Pixels, colorsLabel):
    if Lcreate[0] == 0:
        numberLabel = setNumberLabel(colors, coordinates, colorsLabel)
        for i in Pixels:
            i.setL(numberLabel, posInColorsLabel(i.color, colorsLabel))
        Lcreate[0] = 1
    debug(Pixels)        
    print(colorsLabel)
    print("L successfully created.")

#To know the number of label
def setNumberLabel(colors, coordinates, colorsLabel):
    numberLabel = 0
    for i in colors:
        if len(coordinates[i]) != 0:
            numberLabel += 1
            colorsLabel.append(i)
    return numberLabel

#To calculate the average of the intensity of the pixels from a same label
def average(img, coordinates, average, colorsLabel, labelAverage):
    for i in colorsLabel:
        n = len(coordinates[i])
        sum = 0
        for j in range(n):
            x = coordinates[i][j][0]
            y = coordinates[i][j][1]
            sum += img[x, y][0]
        average.append(sum//n)
        labelAverage[i] = sum // n
    labelAverage = OrderedDict(sorted(labelAverage.items(), key=lambda x: x[1]))
    print(labelAverage)
    average.sort()
    print(average)

def maxOnTab(T):
    max = T[0]
    k = 0
    for i in range(1, len(T)):
        if T[i] == 1:
            return i
        elif max < T[i]:
            max = T[i]
            k = i
        elif max == T[i]:
            k = -1
    return k

def getTheTrueColor(app, color):
    return (app.winfo_rgb(color)[0] // 256, app.winfo_rgb(color)[1] // 256, app.winfo_rgb(color)[2] // 256)

def colorizeNear(img, p, colorsLabelSorted, labelAverageSorted):
    i = img[p.getPos()][0]
    colorMin = colorsLabelSorted[0]
    colorMax = colorsLabelSorted[-1]

    if i <= labelAverageSorted[colorMin]:
        return colorMin
    elif i >= labelAverageSorted[colorMax]:
        return colorMax
    else:
        for c in range(len(colorsLabelSorted) - 1):
            colorInf = colorsLabelSorted[c]
            colorSup = colorsLabelSorted[c+1]
            if i >= labelAverageSorted[colorInf] and i <= labelAverageSorted[colorSup]:
                if abs(i - labelAverageSorted[colorInf]) < abs(i - labelAverageSorted[colorSup]):
                    return colorInf
                else:
                    return colorSup
    return colorMin

#To define the best proximity of a pixel from the other labels
def notTroll(app, img, Pixels, colorsLabel, labelAverage):
    labelAverageSorted = OrderedDict(sorted(labelAverage.items(), key=lambda x: x[1]))
    colorsLabelSorted = []
    for c in labelAverageSorted:
        colorsLabelSorted.append(c)
    for p in Pixels:
        if p.k == 1:
            colorTrue = getTheTrueColor(app, p.color)
            img[p.getPos()] = colorTrue
        else:
            n = p.indexMaxOfL()
            if n != -1:
                color = colorsLabel[n]
            else:
                color = colorizeNear(img, p, colorsLabelSorted, labelAverageSorted)
            colorTrue = getTheTrueColor(app, color)
            img[p.getPos()] = colorTrue
    
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    cv.imshow('Labelised Image', img)
    k = cv.waitKey(0)
    cv.destroyAllWindows()

def sumWs(img, pixels):
    s = []
    WS = Ws(img, pixels)
    for i in range(len(pixels[1].L)):
        s.append(WS * pixels[1].L[i])
    return s

def sumTab(t1, t2):
    for i in range(len(t1)):
        t1[i] = t1[i] + t2[i]
    return t1

def normalizeVector(v):
    norme = 0
    for i in v:
        norme += i
    normeV = []
    for i in range(len(v)):
        normeV.append(v[i] / norme)
    return normeV

def majorFunc(img, Pixels):
    n = 0
    N = 10
    while(n < N):
        for p in Pixels:
            if p.k != 1:
                L = np.zeros(len(p.L))
                neighbors = OmegaS(img, Pixels, p)
                for q in neighbors:
                    s = sumWs(img, (p, q))
                    L = sumTab(L, s)
                L = normalizeVector(L)
                p.setNewL(L)
        tps1 = time.perf_counter()
        for p in Pixels:
            p.setTrueL()
        tps2 = time.perf_counter()
        times = tps2 - tps1
        print(n, times)
        n += 1
    print("Finished")

def getCanny(img, Pixels):
    edges = cv.Canny(img,200,200)
    tps1 = time.perf_counter()
    Pixel = [Pixels[getPixelFromCoordinates(img, 340, 178)], Pixels[getPixelFromCoordinates(img, 334, 158)]]
    d = setLambda(edges, Pixels, Pixel)
    tps2 = time.perf_counter()
    times = tps2 - tps1
    print(times)
    for i in range(0, len(d)):
        print(d[i][0].getPos(), d[i][1])
    cv.imshow('Labelised Image', edges)
    k = cv.waitKey(0)
    cv.destroyAllWindows()
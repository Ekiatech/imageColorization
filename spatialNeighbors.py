import math
import utils

def OmegaS(img, Pixels, pixel):
    (x, y) = pixel.getPos()
    neighbors = []
    l = len(img[0])
    h = len(img)
    for i in range(x-1, x+2, 1):
        for j in range(y-1, y+2, 1):
            if (not (x == i and y == j) ) and (i >= 0 and i < h and j >= 0 and j < l):
                neighbors.append(Pixels[utils.getPixelFromCoordinates(img, i, j)])
    return neighbors

def Ws(img, pixels):
    p = pixels[0]
    q = pixels[1]
    Ip = int(img[p.getPos()][0])
    Iq = int(img[q.getPos()][0])
    delta = 10
    return math.exp(-(Ip - Iq)**2 / (2 * delta**2))

def lookEdge(img, p, neighbors):
    for q in neighbors:
        if q.getPos() != p.getPos() and img[q.getPos()] == 255:
            return 1
    return 0

def setLambda(img, Pixels, pixel):
    depthTab = []
    a = 0
    for p in pixel:
        print("##################################################################")
        print(p.getPos())
        print("BEGIN")
        neighbors = OmegaS(img, Pixels, p)
        n = 0
        depth = 1
        if img[p.getPos()] == 255:
            n = 1
            depth = 0
        while (n != 1):
            print("---- NEW LOOP ----")
            print(n)
            n = lookEdge(img, p, neighbors)
            if n == 0:
                for q in neighbors:
                    neighbors2 =  OmegaS(img, Pixels, q)
                    n = lookEdge(img, p, neighbors2)
                    if n == 1:
                        depth += 1
                        print("=================")
                        print(q.getPos(), img[q.getPos()])
                        break
                if n == 0:
                    for q in neighbors:
                        print(q.getPos(), img[q.getPos()])
                    neighbors = neighbors2
                    depth += 1
        depthTab.append((p, depth))
        a += 1
        if (a == 3):
            break
    return depthTab
    
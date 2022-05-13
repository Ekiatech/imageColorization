import numpy as np

class Pixel:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.color = -1
        self.k = -1

    def getPos(self):
        return (self.x, self.y)

    def setColor(self, color):
        self.color = color
        self.k = 1

    def setL(self, n, c = 0):
        if self.k == -1:
            N = 1 / n
            self.L = np.tile(N, n)
        else:
            self.L = np.zeros(n)
            self.L[c] = 1

    def setNewL(self, L):
        self.newL = L
        #print("Nouveau L :", self.newL)

    def setTrueL(self):
        if self.k != 1:
            self.L = self.newL
        #print("Nouveau nouveau L:", self.L)
    
    def indexMaxOfL(self):
        maxValue = self.L[0]
        maxIndex = 0
        for i in range(1, len(self.L)):
            if self.L[i] > maxValue:
                maxValue = self.L[i]
                maxIndex = i
            elif self.L[i] == maxValue:
                maxIndex = -1
        return maxIndex


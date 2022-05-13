import numpy as np

from image_colorization import average

class Label:
    def __init__ (self, color):
        self.color = color

    def setAverage(self, average):
        self.average = average
    
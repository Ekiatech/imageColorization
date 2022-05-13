from tkinter import *
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 

"""
img = cv.imread('Paysage4.jpg',0)
edges = cv.Canny(img,200,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
"""
"""
colors = ['black', 'blue', 'cyan', 'green', 'magenta', 'red', 'saddle brown', 'white', 'yellow']


def test(event):
    print(liste.curselection()[0])
 
fenetre = Tk()
 
liste = Listbox(fenetre, selectborderwidth = 5)
liste.pack()
 
for i in range(0, len(colors)):
    liste.insert(END, '')
    liste.itemconfig(i , bg = colors[i], selectbackground = colors[i])
 
liste.bind("<<ListboxSelect>>", test)
 
fenetre.mainloop()"""